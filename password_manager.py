from cryptography.fernet import Fernet

# Uncomment and run this ONCE to create a key file:
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    with open("key.key", "rb") as file:
        return file.read()

key = load_key()
fer = Fernet(key)

def view():
    with open("password.text", 'r') as f:
        for line in f:
            data = line.strip()
            if not data:
                continue
            parts = data.split("|")
            if len(parts) != 3:
                print("Skipping invalid line:", data)
                continue
            site, user, enc_pass = parts
            try:
                decrypted = fer.decrypt(enc_pass.encode()).decode()
            except Exception as e:
                decrypted = "ERROR decrypting: " + str(e)
            print(f"Site: {site} | User: {user} | Password: {decrypted}")

def add():
    site = input("Enter website name: ")
    user = input("Enter username: ")
    password = input("Enter password: ")
    encrypted = fer.encrypt(password.encode()).decode()
    with open("password.text", "a") as f:
        f.write(f"{site}|{user}|{encrypted}\n")
    print("Password added successfully.")

while True:
    mode = input("Do you want to view or add a password? (view/add), or press Q to quit: ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid input.")
