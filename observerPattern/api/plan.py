from lib.email import send_email
from lib.db import create_new_user, find_user
from lib.log import log
from lib.slack import post_slack_message

def upgrade_plan(email:str):
    # Find user
    user = find_user(email)

    # Upgrade plan
    user.plan = 'premium'

    # Post slack message to sales department
    post_slack_message("sales", 
                    f"User {user.name} ({email}) upgraded to premium plan")

    # Send confirmation email
    send_email(user.name, user.email,
            "Thank you!",
            f"Your plan has been upgraded to premium!")

    # Write log
    log(f"User with email {user.email} upgraded to premium plan")
