from cryptography.fernet import Fernet
import json

# Load Fernet key (paste your actual key here)
key = b'-RGeiaE0mPDTD03RwKqHplywjfnlmMFw0I7njNshq-M='

# Load JSON payload
with open("payload.json", "rb") as f:
    data = f.read()

# Encrypt
ciphertext = Fernet(key).encrypt(data)

# Save to challenge file
with open("full_challenge.txt", "w") as f:
    f.write(ciphertext.decode())

