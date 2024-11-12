from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.conf import settings

class SpecializationChoices:
    SCIENTIFIC_MEDICINE = [
        ('cardiology', 'Cardiologie'),
        ('dermatology', 'Dermatologie'),
        ('gastroenterology', 'Gastro-entérologie'),
        ('neurology', 'Neurologie'),
        ('pediatrics', 'Pédiatrie'),
        ('gynecology', 'Gynécologie-Obstétrique'),
        ('oncology', 'Oncologie'),
        ('ophthalmology', 'Ophtalmologie'),
        ('ent', 'Oto-rhino-laryngologie (ORL)'),
        ('pulmonology', 'Pneumologie'),
        ('psychiatry', 'Psychiatrie'),
        ('rheumatology', 'Rhumatologie'),
        ('endocrinology', 'Endocrinologie'),
        ('internal_medicine', 'Médecine Interne'),
        ('nephrology', 'Néphrologie'),
        ('hematology', 'Hématologie'),
        ('general_surgery', 'Chirurgie Générale'),
        ('cardiac_surgery', 'Chirurgie Cardiaque'),
        ('orthopedic_surgery', 'Chirurgie Orthopédique'),
        ('plastic_surgery', 'Chirurgie Plastique et Esthétique'),
        ('urology', 'Urologie'),
        ('nuclear_medicine', 'Médecine Nucléaire'),
        ('radiology', 'Radiologie'),
        ('sports_medicine', 'Médecine du Sport'),
        ('geriatrics', 'Gériatrie'),
        ('infectiology', 'Infectiologie'),
        ('anesthesiology', 'Anesthésiologie'),
        ('allergology', 'Allergologie'),
        ('rehabilitation_medicine', 'Médecine Physique et de Réadaptation'),
        ('emergency_medicine', 'Médecine d\'Urgence'),
    ]
    @classmethod
    def get_choices(cls):
        return cls.SCIENTIFIC_MEDICINE
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(
        max_length=50,
        choices=SpecializationChoices.get_choices()
    )
    bio = models.TextField(blank=True)

class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name="Date de naissance", blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Homme'), ('female', 'Femme'), ('other', 'Autre')],
        verbose_name="Sexe"
    )
    phone_number = models.CharField(max_length=15, verbose_name="Numéro de téléphone", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Adresse", blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, verbose_name="Nom du contact d'urgence", blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, verbose_name="Téléphone du contact d'urgence", blank=True, null=True)
    blood_type = models.CharField(
        max_length=3,
        choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')],
        verbose_name="Groupe sanguin",
        blank=True,
        null=True
    )
    known_allergies = models.TextField(verbose_name="Allergies connues", blank=True, null=True)
    medical_history = models.TextField(verbose_name="Antécédents médicaux", blank=True, null=True)
    current_medications = models.TextField(verbose_name="Médicaments actuels", blank=True, null=True)
    insurance_provider = models.CharField(max_length=100, verbose_name="Fournisseur d'assurance", blank=True, null=True)
    insurance_number = models.CharField(max_length=50, verbose_name="Numéro d'assurance", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Date de création du profil")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Profil Patient"
