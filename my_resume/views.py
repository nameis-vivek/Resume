from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        return render(request,'my_resume/index.html',{'form':form})