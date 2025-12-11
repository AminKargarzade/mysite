from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsLetterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')
def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'There was an error sending your message. Please try again.')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



def test_view(request):
# sourcery skip: no-conditionals-in-tests, remove-unnecessary-else, swap-if-else-branches
    if request.method == 'POST':
        form = ContactForm(request.POST)
# sourcery skip: no-conditionals-in-tests
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('Boro baba')
        
    form = ContactForm()
    return render(request, 'website/test.html', {'form': form})