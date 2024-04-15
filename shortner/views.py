from django.shortcuts import get_object_or_404, render, redirect
from .models import URL
from .form import formInput
import string
import random
# Create your views here.

def form_view(request):
    if request.method == 'POST':
        form = formInput(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            random_character = string.ascii_letters + string.digits
            random_text = ''.join(random.choice(random_character) for _ in range(6))
            short_url = 'http://localhost:8000/'+ random_text
            new_Model = URL(link=link, short_link=short_url)
            new_Model.save() 
            return render(request,'home.html', {'form':new_Model})
    else:
        form = formInput()
        return render(request,'home.html',{'form':form})


def get_view(request,short_link):
    link = get_object_or_404(URL, short_link=short_link)
    print(link.link)