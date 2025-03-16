from lib.db import find_user
from .event import post_event

def upgrade_plan(email:str):
        # Find user
        user = find_user(email)

        # Upgrade plan
        user.plan = 'premium'

        post_event(event_type='user_plan_upgraded', data=user)
