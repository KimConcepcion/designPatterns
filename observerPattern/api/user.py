from lib.db import create_new_user, find_user
from lib.stringtools import get_random_string
from .event import post_event

def register_new_user(user:str, password:str, email:str):
    # Create entry in database
    user = create_new_user(user, password, email)
    
    post_event(event_type='user_registered', data=user)

def password_forgotten(email:str):
    # Retrieve user
    user = find_user(email)

    # Generate password reset code
    user.reset_code = get_random_string(16)

    post_event(event_type='user_password_forgotten', data=user)

# def register_new_user(user:str, password:str, email:str):
#     # Create entry in database
#     user = create_new_user(user, password, email)

#     # Post slack message to sales department
#     post_slack_message("sales", f"New user registered: {user} ({email}) Please spam this person")

#     # Send welcome email
#     send_email(user.name, user.email,
#             "Welcome",
#             f"Thank you for registering with us, {user.name}!\nRegards, the team")
    
#     # Write log
#     log(f"User registered with email address {user.email}")

# def password_forgotten(email:str):
#     # Retrieve user
#     user = find_user(email)

#     user.reset_code = get_random_string(16)

#     # Send a password reset message
#     send_email(user.name, user.email, 
#             "Reset your password",
#             f"To reset your password, use this ultra secure code: {user.reset_code}\nRegards, the team")
    
#     # Write log
#     log(f"User with email {user.email} requested a password reset")
