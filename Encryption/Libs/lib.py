from Encryption.Libs.Mongo_Connection import *
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
#from Crypto.Random import get_random_bytes
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend