from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from . import views

urlpatterns = [
    path("register/", views.register_choice, name="register"),
    path("register/patient/", views.register_patient, name="register_patient"),
    path("register/doctor/", views.register_doctor, name="register_doctor"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/forgot_password.html',
        email_template_name='password_reset_email.html',
        success_url=reverse_lazy('password_reset_done'),
        token_generator=default_token_generator
    ), name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/forgot_password.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
