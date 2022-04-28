from email.mime.image import MIMEImage
from .models import Contact
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import ContactForm
from .models import Contact
from .tasks import send_spam_email, spam_beat_mail
from django.urls import reverse_lazy


# Create your views here.

class HomeCreateView(CreateView):
    template_name = "mail_celery/home.html"
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy("home")

    def form_valid(self, form, *args, **kwargs):
        form.save()
        send_spam_email.delay(form.cleaned_data["email"])
        send_spam_email.apply_async(
            (form.cleaned_data["email"],), countdown=60)  # starts in 60 seconds
        return super(HomeCreateView, self).form_valid(form, *args, **kwargs)


def add_to_database(request):
    with open("fuckers_emails_1.txt") as file:
        for i, line in enumerate(file.readlines()):
            if i > 10000 and i <= 50000:
                Contact.objects.create(name="Хуйло", email=line)
            elif i == 50001:
                return HttpResponse("done")


def send_mess():
    html_content = render_to_string(
        'mail_celery/message.html', context={"filename": "102.jpg"}).strip()
    # for elem in Contact.objects.all():
    msg = EmailMultiAlternatives("your die message",
                                 html_content, "bookingdjangoprojkpi@gmail.com", ("duhanov2003@gmail.com",))
    msg.content_subtype = 'html'  # Main content is text/html
    # This is critical, otherwise images will be displayed as attachments!
    msg.mixed_subtype = 'related'

    with open("102.jpg", mode='rb') as f:
        image = MIMEImage(f.read())
        msg.attach(image)
        image.add_header('Content-ID', f"<102.jpg>")
    msg.send()


def send_message(request):
    # msg.attach(img)
    spam_beat_mail.delay()
    return HttpResponse("Done")
