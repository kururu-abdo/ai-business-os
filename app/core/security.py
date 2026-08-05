from cryptography.fernet import Fernet
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def hash_password(plain_password):
    
    hash = password_hash.hash(plain_password)
    return hash


def verify_password(hashed_password, plain_password):
    result = password_hash.verify(plain_password, hashed_password)
    return result



def encrypt_password(plain_password):
    plain_text_utf_8 = plain_password.encode('utf-8')
    cipher_text = cipher_suite.encrypt(plain_text_utf_8)
    return cipher_text


def decrypt_password(encrypted_password, plain_password):
    decrypted_text = cipher_suite.decrypt(encrypted_password)
    return decrypted_text.decode('utf-8')==plain_password

    


    


