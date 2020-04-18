from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        names = request.POST['names']
        from_email = request.POST['from-email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject, message, from_email, ['kibussystemltd@gmail.com'])

        return render(request, 'contact.html', {'names': names})
    else:
        return render(request, 'contact.html', {})


def ministries(request):
    return render(request, 'ministries.html', {})


def sermons(request):
    return render(request, 'sermons.html', {})
