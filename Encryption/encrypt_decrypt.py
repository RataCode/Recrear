from Encryption.Libs.lib import *
from Encryption.Libs.vars import *
from base64 import b64decode
from typing import Tuple
import sys

def derive_key(key: str, salt: bytes) -> bytes:
    # Key derivation
    kdf = PBKDF2HMAC(
        algorithm= hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1000,
        backend=default_backend()
    )
    return kdf.derive(key.encode())

def aes_gcm_encrypt(texto: str, key: str) -> bytes:
    # Encryption
    nonce = os.urandom(12)
    header = texto.encode('utf-8')
    key_bytes = derive_key(key, salt=b'salt')
    aesgcm = AESGCM(key_bytes)
    ciphertext = aesgcm.encrypt(nonce, header, None)
    return nonce + ciphertext

def aes_gcm_decrypt(cipher_text: bytes, key: str) -> str:
    # Decryption
    nonce = cipher_text[:12]
    ciphertext = cipher_text[12:]
    key_bytes = derive_key(key, salt=b'salt')
    aesgcm = AESGCM(key_bytes)
    plain_text = aesgcm.decrypt(nonce, ciphertext, None)
    plain_text = plain_text.decode('utf-8')
    return plain_text

if __name__ == "__main__":
    # cipher_text = aes_gcm_encrypt("hola", key)
    # print(cipher_text)
    data = sys.argv[2]
    data = b64decode(data)
    print(data)
    plain_text = aes_gcm_decrypt(data, key)
    print(plain_text)

