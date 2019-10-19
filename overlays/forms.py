from django.forms import ModelForm

from overlays.models import Overlay

class OverlayForm(ModelForm):
    class Meta:
        model = Overlay
        fields = ['name', 'latitude', 'longtitude', 'plume']
