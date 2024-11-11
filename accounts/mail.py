from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(username, recipient_email):
    # Load and render the HTML template with context
    html_message = render_to_string('emails/welcome_email.html', {'username': username})
    
    # Create the email message
    subject = "Welcome to Our Website!"
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient_email],
    )
    
    # Set content type to HTML
    email.content_subtype = "html"
    
    # Send the email
    email.send()

def send_reset_password_token_email(username, recipient_email):
    # Load and render the HTML template with context
    html_message = render_to_string('emails/welcome_email.html', {'username': username})
    
    # Create the email message
    subject = "Welcome to Our Website!"
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient_email],
    )
    
    # Set content type to HTML
    email.content_subtype = "html"
    
    # Send the email
    email.send()

def send_acrivate_account_email(username, recipient_email):
    # Load and render the HTML template with context
    html_message = render_to_string('emails/welcome_email.html', {'username': username})
    
    # Create the email message
    subject = "Welcome to Our Website!"
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient_email],
    )
    
    # Set content type to HTML
    email.content_subtype = "html"
    
    # Send the email
    email.send()