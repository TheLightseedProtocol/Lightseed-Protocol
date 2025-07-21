import sympy, hashlib, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# --- 1. Generate primes -------------------------------------------------
p = sympy.randprime(2**1024, 2**1025)
q = sympy.randprime(2**1024, 2**1025)
n = p * q

# --- 2. Derive hash and Fernet key --------------------------------------
p_bytes = p.to_bytes((p.bit_length() + 7) // 8, "big")
hash_p = hashlib.sha512(p_bytes).hexdigest()

salt = b'lightseed-v1-salt'
info = b'lightseed-fernet-key'

kdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    info=info,
    backend=default_backend()
)

key32 = kdf.derive(p_bytes)
fernet_key = base64.urlsafe_b64encode(key32)

# --- 3. Load payload ----------------------------------------------------
with open("payload.json", "rb") as f:
    payload = f.read()

# --- 4. Encrypt and save ------------------------------------------------
encrypted_b64 = Fernet(fernet_key).encrypt(payload).decode()

with open("full_challenge.txt", "w") as f:
    f.write(encrypted_b64)

# --- 5. Output to paste into metadata -----------------------------------
print("p =", p)
print("q =", q)
print("n =", n)
print("sha512_p =", hash_p)
print("fernet_key =", fernet_key.decode())
print("encrypted_payload =", encrypted_b64)

