from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),
    #
    path('', views.home, name="home"),
    path('profile/<str:pk>/', views.user_profile, name="profile"),
    #
    path('edit_profile/<str:pk>/', views.edit_profile, name="edit_profile"),
    path('confirm', views.confirm, name="confirm")
    # path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    # path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    #
    # path('update-user/', views.updateUser, name="update-user"),
    #
    # path('topics/', views.topicsPage, name="topics"),
    # path('activity/', views.activityPage, name="activity"),
]
