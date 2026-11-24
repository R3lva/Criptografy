from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization
import ED as module
import Validate as va
# Generate RSA KEYS
clave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
clave_publica = clave_privada.public_key()

mensaje = b"RSA DEFEND"
publica = clave_publica.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
cifrado = module.encrypt(clave_publica,mensaje)
print("RSA: ", publica)
print("Original:", module.decrypt(clave_privada,cifrado).decode("utf-8"))
va.validate("", publica)