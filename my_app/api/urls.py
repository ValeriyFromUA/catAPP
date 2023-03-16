from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.get),
    path('add_user/', views.UserView.post),

]
