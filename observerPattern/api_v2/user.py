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

    # Return generated reset code
    return user.reset_code

def reset_password(code:str, email:str, password:str):
    # Retrieve user
    user = find_user(email)

    # Reset password
    user.reset_password(code, password)

    post_event(event_type='user_password_reset', data=user)
