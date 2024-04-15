from django.shortcuts import  render, redirect
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
            alreadyexists = URL.objects.filter(link=link).exists()
            if alreadyexists:
               getLink = URL.objects.filter(link=link).first()
               new_Model = getLink
               new_Model.short_link = 'http://localhost:8000/' + getLink.short_link
               return render(request,'shortUrl.html',{'new_model':new_Model})
            else:
                random_character = string.ascii_letters + string.digits
                random_text = ''.join(random.choice(random_character) for _ in range(6))
                short_url =  random_text
                new_Model = URL(link=link, short_link=short_url)
                new_Model.save() 
                new_Model.short_link = 'http://localhost:8000/' + short_url
                return render(request,'shortUrl.html', {'new_model':new_Model})
    else:
        form = formInput()
        return render(request,'home.html',{'form':form})


def get_view(request,short_link):
    # print(short_link)
    link = URL.objects.filter(short_link = short_link).first()
    print("model link:" + link.link)
    return redirect(link.link)