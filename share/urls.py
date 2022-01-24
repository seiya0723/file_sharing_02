from django.urls import path
from . import views

app_name    = "share"
urlpatterns = [ 
    path('', views.index, name="index"),
]

#ここに複数ページ(個別ページも実装)
