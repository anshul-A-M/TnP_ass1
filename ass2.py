# Anshul mahajan
# 0103IS231029
# batch 5 / 10:30 to 12:10
logged_user = ''
logged = False
students = {}

def register():
    print("\n-- Registration --")
    username = input("Username: ")
    if username in students:
        print("Username already exists!\n")
        return
    password = input("Password: ")
    name = input("Full Name: ")
    age = input("Age: ")
    email = input("Email: ")
    phone = input("Phone: ")
    course = input("Course: ")
    roll = input("Roll No: ")
    address = input("Address: ")
    dob = input("Date of Birth: ")

    students[username] = {
        "password": password, "name": name, "age": age, "email": email,
        "phone": phone, "course": course, "roll": roll,
        "address": address, "dob": dob
    }
    print("Registered successfully!\n")

def login():
    global logged, logged_user
    print("\n-- Login --")
    u = input("Username: ")
    p = input("Password: ")
    if u in students and students[u]["password"] == p:
        logged, logged_user = True, u
        print(f"Welcome {students[u]['name']}!\n")
    else:
        print("Invalid credentials!\n")

def show_profile():
    if not logged: 
        print("Login first!\n"); return
    print("\n-- Profile --")
    for k, v in students[logged_user].items():
        if k != "password":
            print(f"{k}: {v}")
    print()

def update_profile():
    if not logged: 
        print("Login first!\n"); return
    print("\n-- Update Profile --")
    for k, v in students[logged_user].items():
        if k != "password":
            new = input(f"{k} ({v}): ")
            if new: students[logged_user][k] = new
    print("Profile updated!\n")

def logout():
    global logged, logged_user
    if logged:
        print(f"{logged_user} logged out!\n")
        logged, logged_user = False, ''
    else:
        print("No user logged in!\n")

def terminate():
    print("Goodbye!"); exit()

def main():
    while True:
        choice = input('''\n      LNCT Menu       
1. Register
2. Login
3. Show Profile
4. Update Profile
5. Logout
6. Exit
Choose (1-6): ''')
        if choice == '1': register()
        elif choice == '2': login()
        elif choice == '3': show_profile()
        elif choice == '4': update_profile()
        elif choice == '5': logout()
        elif choice == '6': terminate()
        else: print("Invalid choice!\n")

main()
