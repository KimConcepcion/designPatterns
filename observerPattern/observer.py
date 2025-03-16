from api_v2.user import register_new_user, password_forgotten, reset_password
from api_v2.plan import upgrade_plan

from api_v2.log_listener import setup_log_event_handlers
from api_v2.slack_listener import setup_slack_event_handlers
from api_v2.email_listener import setup_email_event_handlers

# Initialize event structure
setup_log_event_handlers()
setup_slack_event_handlers()
setup_email_event_handlers()

# Register new user
register_new_user("Kain", "1234", "kainLim@something.com")

# Upgrade the plan
upgrade_plan("kainLim@something.com")

# Send a password reset message
reset_code = password_forgotten("kainLim@something.com")

reset_password(reset_code, "kainLim@something.com", "1234")
