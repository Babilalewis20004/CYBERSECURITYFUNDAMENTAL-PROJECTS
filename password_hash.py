import bcrypt

def hash_password(password: str) -> str:
    # Encode the password
    encoded_password = password.encode('utf-8')
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password.decode('utf-8')
