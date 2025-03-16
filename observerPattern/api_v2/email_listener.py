from .event import subscribe
from lib.email import send_email

def handle_user_registered_event(user):
    # Send welcome email
    send_email(user.name, user.email,
            "Welcome",
            f"Thank you for registering with us, {user.name}!\nRegards, the team")

def handle_user_password_forgotten_event(user):
    # Send a password reset message
    send_email(user.name, user.email, 
            "Reset your password",
            f"To reset your password, use this ultra secure code: {user.reset_code}\nRegards, the team")

def handle_user_password_reset_event(user):
    # Inform that password has been reset
    send_email(user.name, user.email, 
            "Password was reset",
            f"Hello {user.name} your password was reset!\nRegards, the team")

def handle_user_plan_upgraded_event(user):
        # Send confirmation email
        send_email(user.name, user.email,
                "Thank you!",
                f"Your plan has been upgraded to premium!")

def setup_email_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_password_reset", handle_user_password_reset_event)
    subscribe("user_plan_upgraded", handle_user_plan_upgraded_event)
