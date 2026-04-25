def email_slicer(email):
    username, domain = email.split("@")
    print(f"Username: {username}")
    print(f"Domain: {domain.upper()}")

user_email = input("Enter your email: ").strip()
email_slicer(user_email)
