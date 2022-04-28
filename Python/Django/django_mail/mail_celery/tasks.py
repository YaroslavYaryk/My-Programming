from .services.mail import send_mail_to_user
from django_mail.celery import app
from .models import Contact
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@app.task
def send_spam_email(email):
    send_mail_to_user(email)


@app.task
def spam_beat_mail():
    for elem in Contact.objects.all():
        send_mail(
            subject="revenge",
            message="""It won't take us too long to get u, but kmow ur gonna be next""",
            from_email="bookingdjangoprojkpi@gmail.com",
            recipient_list=[elem.email[:-2]],
            fail_silently=False,
            html_message=render_to_string(
                'mail_celery/message.html')
        )


# @ app.task
# def add(a, b):
#     return a + b


# add.apply_async((10, 10), link=add.s(20))
# # this command after working ADD will start one more time
# # task add requires 2 parameters but we give only one (in the second part)
# # so the result of first part is (10+10=20) will be given as second parameter to next call
# # so the first result will be 20 and second result will be 40


# @ app.task(bind=True, default_retry_delay=5 * 60)
# def add_with_delay(self, a, b):
#     try:
#         return a + b
#     except Exception as exc:
#         # task will try again in 60 seconds
#         raise self.retry(exc=exc, countdown=60)
