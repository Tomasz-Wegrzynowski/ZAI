
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from zaiapp.models import Film
from zaiapp.forms import FilmForm


def wszystkie(request):
    template = loader.get_template("zaiapp/wszystkie.html")
    wszystkie_filmy = Film.objects.all()
    context = {'wszystkie_filmy':wszystkie_filmy,}
    return HttpResponse(template.render(context, request))

def szczegoly(request,film_id):
    template = loader.get_template("zaiapp/szczegoly.html")
    film = Film.objects.get(id=film_id)
    context = {'film': film}
    return HttpResponse(template.render(context,request))


def nowy(request):
    nowyform = FilmForm(request.POST or None)
    if nowyform.is_valid():
        nowyform.save()
        return redirect(wszystkie)
    return render(request, 'zaiapp/c.html', {'nowyform': nowyform})


def edycja(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    form = FilmForm(request.POST or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(wszystkie)
    return render(request, 'zaiapp/u.html', {'form':form})


def usun(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method=="POST":
        film.delete()
        return redirect(wszystkie)
    return render(request, 'zaiapp/usun.html', {'film': film})