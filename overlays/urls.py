from django.urls import path

from . import views

app_name = 'overlays'
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('<int:overlay_id>', views.show, name='show'),
    path('<int:overlay_id>.json', views.show, name='json_show'),
]