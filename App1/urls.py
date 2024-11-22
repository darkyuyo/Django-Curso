from django.urls import path
from App1.views import IndexView,AutorView,create_autorView

urlpatterns = [
    path('', IndexView),
    path('autor/<int:id>', AutorView),
    path("create_autores/",create_autorView)
]
