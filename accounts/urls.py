from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    path('login/url/', views.RequestLoginViaUrlView.as_view(), name='request_login_via_url'),
    path('login/<uidb64>/<token>/', views.login_via_url, name='login_via_url'),

    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),

    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(
    #          template_name='accounts/password_change_done.html'
    #      ),
    #      name='password_change_done'),

    path('password_reset/', views.MyPasswordResetView.as_view(), name = 'password_reset'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
