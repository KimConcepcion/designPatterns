from hashlib import blake2b

# The datebase of users
users = []

class User:
    def __init__(self, name:str, password:str, email:str):
        self.name = name
        self.password = blake2b(password.encode('UTF-8')).hexdigest()
        self.email = email
        self.plan = 'basic'
        self.reset_code = ''

    def __repr__(self):
        return f"NAME: {self.name}, EMAIL: {self.email}, PASSWD: {self.password}"
    
    def reset_password(self, code:str, new_password:str):
        if code != self.reset_code:
            raise Exception('Invalid reset code...')
        self.password = blake2b(new_password.encode('UTF-8')).hexdigest()
    
def create_new_user(user:str, password:str, email:str):
    new_user = User(user, password, email)
    users.append(new_user)
    return new_user

def find_user(email:str):
    for user in users:
        if user.email == email:
            return user
    raise Exception(f'User with email {email} not found...')
