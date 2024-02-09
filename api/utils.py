from django.core.mail import send_mail as sm
from accounts.models import User

from itsdangerous import URLSafeSerializer

serializer = URLSafeSerializer(secret_key="hello world")

def encrypt_user_id(user_id):
    encrypted = serializer.dumps(user_id)
    return encrypted

def decrypt_user_id(encrypted_id):
    try:
        decrypted = serializer.loads(encrypted_id)
        return decrypted
    except Exception as e:
        print("Ошибка при дешифровании:", e)
        return None


def send_mail(user: User):
    user_id = encrypt_user_id(user.id)
    link = f"http://127.0.0.1:8000/api/auth/confirm/{user_id}"
    data = {
        "subject": "Registration",
        "message": f"Here's registrations link {link}",
        "from_email": "dasifueng@gmail.com",
        "recipient_list": [user.email]
    }
    sm(**data)