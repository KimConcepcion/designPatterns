from .event import subscribe
from lib.log import log

def handle_user_registered_event(user):
    log(f"User registered with email address {user.email}")

def handle_user_password_forgotten_event(user):
    log(f"User with email {user.email} requested a password reset")

def handle_user_password_reset_event(user):
    log(f"User with email {user.email} password was reset")

def handle_user_plan_upgraded_event(user):
    log(f"User with email {user.email} upgraded to premium plan")

def setup_log_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_password_reset", handle_user_password_reset_event)
    subscribe("user_plan_upgraded", handle_user_plan_upgraded_event)
