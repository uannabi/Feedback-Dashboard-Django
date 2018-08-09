from django.shortcuts import render, redirect
from .models import Article
from webapp.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['zahid.adivagraphics@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "webapp/home.html", {'form': form})
    # return render(request, 'webapp/home.html')


def bio(request):
    return render(request, 'webapp/bio.html')


def mindset(request):
    return render(request, 'webapp/mindset.html')


def life(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'webapp/life.html', {'articles': articles})


def article_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'webapp/post.html', {'article': article})


def signup(request):
    return render(request, 'webapp/signup.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['zahid.adivagraphics@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "webapp/contact.html", {'form': form})


def success(request):
    return HttpResponse('Success! Thank you for your message.')
