
"""
Funcion para la creacion de usuarios comunes y super usuarios
"""
def create_user(usermanager, email, username, password=None):
    if not email:
        raise ValueError('The Email field must be set')

    user = usermanager.model(username=username, email=email)
    email = usermanager.normalize_email(email)
    user.set_password(password)
    user.save(using=usermanager._db)

    return user
