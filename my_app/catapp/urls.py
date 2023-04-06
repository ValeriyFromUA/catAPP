from django.urls import path

from catapp.views import (HomeView, UserProfileView, PostView, DeletePostView, RegistrationView, ConfirmView,
                          EditProfileView, LoginView, LogoutView, NewPostView, AboutView)

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegistrationView.as_view(), name="register"),
    # #
    path('', LoginView.as_view(), name="login"),
    path('profile/<str:pk>/', UserProfileView.as_view(), name="profile"),
    # #
    path('edit_profile/<str:pk>/', EditProfileView.as_view(), name="edit_profile"),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path('new_post/', NewPostView.as_view(), name="new_post"),
    path('post/<str:pk>/', PostView.as_view(), name="post"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

]
