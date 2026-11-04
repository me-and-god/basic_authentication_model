"""This file hashes the incoming password when signed up and the verify the hashed 
password when logged in """

from pwdlib import PasswordHash

Hasher = PasswordHash.recommended()

def hash_password( 
        password: str
) -> str:
    return Hasher.hash(password=password)


def verify_password(
        plain_pass : str,
        hashed_pass : str
) -> bool:

    return Hasher.verify(plain_pass, hashed_pass)