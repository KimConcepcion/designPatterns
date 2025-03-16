from .event import subscribe
from lib.slack import post_slack_message

def handle_user_registered_event(user):
    post_slack_message("sales", f"New user registered: {user.name} with email ({user.email}) Please spam this person!")

def handle_user_plan_upgraded_event(user):
        post_slack_message("sales", 
                        f"User {user.name} ({user.email}) upgraded to premium plan")

def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_plan_upgraded", handle_user_plan_upgraded_event)
