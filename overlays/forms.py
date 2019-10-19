from django.forms import ModelForm

from overlays.models import Overlay

class OverlayForm(ModelForm):
    class Meta:
        model = Overlay
        fields = '__all__'
