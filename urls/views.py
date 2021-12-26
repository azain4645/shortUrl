from django.shortcuts import redirect, render, get_object_or_404
from .forms import MainForm
from .models import Url
from urls.module.common import ShortURL

def index(request):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            url = form.save()
            return redirect('urls:shorted', url.num)
    else:
        form = MainForm
        return render(request, 'urls/index.html', {'form':form })

def shorted(request, num):
    shortURL = ShortURL() 
    code = shortURL.encode(num = num)
    context = {'code': code}
    return render(request, 'urls/shorted.html', context)

def redirectTo(request, key):
    shortURL = ShortURL() 
    decodedNum = shortURL.decode(key = key)
    url = get_object_or_404(Url, num= decodedNum)
    return redirect(url.url)