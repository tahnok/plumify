from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Overlay

def index(request):
    overlays = Overlay.objects.all()
    context = {'overlays': overlays}
    return render(request, 'overlays/index.html', context)

def new(request):
    return render(request, 'overlays/new.html')

def create(request):
    overlay = Overlay(name=request.POST['name'])
    overlay.save()
    return HttpResponseRedirect(reverse('overlays:show', args=(overlay.id,)))

def show(request, overlay_id):
    overlay = get_object_or_404(Overlay, pk=overlay_id)
    return render(request, 'overlays/show.html', {'overlay': overlay})