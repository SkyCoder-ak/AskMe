from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from AskMe import settings

# Create your views here.
def AboutView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        sender = 'beyondhorrizon7@gmail.com'
        recipients = ['motheakash321@gmail.com']
        mail_message = f"Name: {name}\nEmail:{email}\nMessage:{message}"

        sent = send_mail('Contact from AskMe', mail_message, sender, recipients, fail_silently=False,auth_user=settings.EMAIL_HOST_USER,auth_password=settings.EMAIL_HOST_PASSWORD)
        if sent == 1:
            messages.add_message(request, messages.SUCCESS, "We will shortly in touch with you.", extra_tags='message_sent')
            return redirect("aboutpage")
        else:
            messages.add_message(request, message.SUCCESS, "Sorry something went wrong, Try again.")
    return render(request, 'aboutus/aboutus.html', {'nav_about':'activeTopNav'})


def BadgesView(request):
    return render(request, 'aboutus/badges.html')