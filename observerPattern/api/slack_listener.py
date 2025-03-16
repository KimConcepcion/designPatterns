from .event import subscribe
from lib.slack import post_slack_message

def handle_user_registered_event(user):
    post_slack_message("sales", f"New user registered: {user.name} with email ({user.email}) Please spam this person!")

def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
