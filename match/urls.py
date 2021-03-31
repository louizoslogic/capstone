from django.urls import path
from . import views

app_name = "match"

urlpatterns = [

    path('', views.match, name="match"),
    path('updatedb', views.updatedb, name='update')

]
