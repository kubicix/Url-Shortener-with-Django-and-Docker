# views.py

from django.shortcuts import render, redirect
from .forms import ShortenURLForm
from .models import ShortenedURL

def shorten_url(request):
    shortened_url = None

    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            # Eğer form geçerliyse, URL'yi veritabanına kaydet
            shortened_url = form.save()
    else:
        form = ShortenURLForm()

    return render(request, 'index.html', {'form': form, 'shortened_url': shortened_url})

def redirect_original(request, short_url):
    # Kısaltılmış URL'ye yönlendirme yap
    shortened_url = ShortenedURL.objects.get(short_url=short_url)
    return redirect(shortened_url.original_url)
