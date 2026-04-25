import random
import string
import re

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_strength(password):
    strength = 0
    if len(password) >= 8: strength += 1
    if re.search(r"[a-z]", password): strength += 1
    if re.search(r"[A-Z]", password): strength += 1
    if re.search(r"\d", password): strength += 1
    if re.search(r"[@$!%*?&]", password): strength += 1
    
    remarks = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    return remarks[strength-1] if strength > 0 else "Invalid"

print("--- Secure Password Tool ---")
new_pass = generate_password()
print(f"Suggested Password: {new_pass}")
print(f"Strength: {check_strength(new_pass)}")
