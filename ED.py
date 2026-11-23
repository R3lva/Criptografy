# Module to Encrypt and Decrypt using the Private and Public Key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
def decrypt(private,cifrado):
    descifrado = private.decrypt(
     cifrado,
        padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA256()),
          algorithm=hashes.SHA256(),
         label=None,
        ),
    )
    return descifrado

def encrypt(public,mensaje):
    cifrado = public.encrypt(
      mensaje,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
      ),
    )
    return cifrado