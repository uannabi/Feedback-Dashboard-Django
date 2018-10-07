from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Csr
from django.views.generic import ListView


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
    


def bio(request):
    return render(request, 'webapp/bio.html')


def mindset(request):
    return render(request, 'webapp/mindset.html')




def csr_list(request):
    object_list = Csr.published.all()
    paginator = Paginator(object_list, 3)  # 4 post per page
    page = request.GET.get('page')
    try:
        csrs = paginator.page(page)
    except PageNotAnInteger:
        # if page ins not an inteer deliver the first page
        csrs = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        csrs = paginator.page(paginator.num_pages)
    # csrs = Csr.published.all()
    return render(request, 'webapp/csr.html', {'page': page, 'csrs': csrs})



def csr_detail(request, slug):
    object_list = Csr.published.all()
    # print(object_list)
    csr = Csr.objects.get(slug=slug)
    return render(request, 'webapp/post.html', {'csr': csr, 'csrs': object_list })


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
