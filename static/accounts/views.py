from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, DoctorProfileForm, CustomAuthenticationForm, PatientProfileForm, CustomUserCreationForm
from django.http import HttpResponse
from .mail import send_welcome_email
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from .mail import *
def register_doctor(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        profile_form = DoctorProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_doctor = True  # Indique que cet utilisateur est un docteur
            user.save()
            
            # Associer le profil docteur à l'utilisateur
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            send_welcome_email(user.first_name +  ' ' + user.last_name, user.email)
            login(request, user)  # Connexion automatique après inscription
            return redirect("home")  # Redirection vers la page d'accueil ou tableau de bord
    else:
        user_form = CustomUserCreationForm()
        profile_form = DoctorProfileForm()
    
    return render(request, "accounts/register_doctor.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })

def register_patient(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        profile_form = PatientProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_patient = True  # Indique que cet utilisateur est un patient
            user.save()
            
            # Associer le profil patient à l'utilisateur
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            login(request, user)  # Connexion automatique après inscription
            return redirect("home")  # Redirection vers la page d'accueil ou tableau de bord
    else:
        user_form = CustomUserCreationForm()
        profile_form = PatientProfileForm()
    
    return render(request, "accounts/register_patient.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })


def register_choice(request):
    return render(request, "accounts/register_choice.html")




def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def logout_view(request):
    pass
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Retrieves the authenticated user
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})
def send_email_view(request):
    # Example data
    username = "NewUser"
    recipient_email = "newuser@example.com"
    
    # Send the welcome email
    send_welcome_email(username, recipient_email)
    
    return HttpResponse("Welcome email sent successfully!")
