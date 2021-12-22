from django.shortcuts import redirect, render
from .models import Students,feedback,stories
from django.core.mail import send_mail, message
from django.conf import settings


def about(request):
 return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name= request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        stud = Students(name=name, phone=phone, subject=subject, email=email, message=message)
        stud.save()

        data = {
                'name' : name,
                'email' : email,
                'subject' : subject,
                'message' : message,
        }
        subject = f'Thank You For Contacting Us For {subject}'
        message = f'message: {message}\n Hi {name}, Thank you for contacting us. Our representative will contact you within 24hr'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        
        return redirect("home")
    return render(request, 'contact.html')

def home(request):
 return render(request, 'home.html')

def send(request):
    if request.method=="POST":
        name= request.POST.get('name')
       
        email=request.POST.get('email')
       
        message=request.POST.get('message')
        feed = feedback(name=name, email=email, message=message)
        feed.save()
    return render(request, 'feedback.html') 

def story(request):
    if request.method=="POST":
        mes=request.POST.get('message')
        stor = stories(mes=mes)
        stor.save()
    return render(request, 'stories.html')

def gallery(request):
    return render(request, 'gallery.html')


def work(request):
    return render(request, 'work.html')

def donation(request):
    return render(request, 'donation.html')

def video(request):
    return render(request, 'video.html')