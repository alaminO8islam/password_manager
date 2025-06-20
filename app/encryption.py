from cryptography.fernet import Fernet
import base64
import os
import bcrypt

def generate_key(master_password: str) -> bytes:
    salt = b'static_salt'  # Should be more dynamic in production
    key = bcrypt.kdf(
        password=master_password.encode(),
        salt=salt,
        desired_key_bytes=32,
        rounds=100
    )
    return base64.urlsafe_b64encode(key)

def encrypt_password(key: bytes, plain_text: str) -> str:
    return Fernet(key).encrypt(plain_text.encode()).decode()

def decrypt_password(key: bytes, cipher_text: str) -> str:
    return Fernet(key).decrypt(cipher_text.encode()).decode()
