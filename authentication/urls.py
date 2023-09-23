from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
    ), name='logout'),
    # path('signup/', views.signup, name='signup'),

]
