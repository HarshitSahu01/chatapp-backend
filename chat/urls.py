from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('chat', views.chat, name = 'chat'),
    path('apis/<str:type>', views.apis, name = 'apis'),
]