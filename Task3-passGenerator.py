import string
import random

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def password_generator():
    print("Password Generator")
    print("-------------------")

    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("\nGenerated Password: ", password)

if __name__ == "__main__":
    password_generator()
