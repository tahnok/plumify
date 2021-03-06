from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django.forms.models import model_to_dict

from .models import Overlay
from .forms import OverlayForm

def index(request):
    overlays = Overlay.objects.all()
    context = {'overlays': overlays}
    return render(request, 'overlays/index.html', context)

def new(request):
    if request.method == 'POST':
        overlay_form = OverlayForm(request.POST, request.FILES)
        if overlay_form.is_valid():
            overlay = overlay_form.save(commit=False)
            overlay.process_and_save()
            return HttpResponseRedirect(reverse('overlays:show', args=(overlay.id,)))
    else:
        overlay_form = OverlayForm()
    return render(request, 'overlays/new.html', {'overlay_form': overlay_form})

def show(request, overlay_id):
    overlay = get_object_or_404(Overlay, pk=overlay_id)
    if request.path.endswith(".json"):
        return JsonResponse(overlay.as_dict())
    else:
        return render(request, 'overlays/show.html', {'overlay': overlay})