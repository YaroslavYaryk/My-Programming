from django.core.mail import send_mail

def send_mail_to_user(email):

    send_mail(
        subject="this is subject",
        message="here is some text",
        from_email="duhanov2003@gmail.com",
        recipient_list=[email],
        fail_silently=False
    )