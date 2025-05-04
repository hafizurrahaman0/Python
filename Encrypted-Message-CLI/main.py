from cryptography.fernet import Fernet

# Generate a key (keep this secret and secure)
key = Fernet.generate_key()
f = Fernet(key)

while True:
    # Ask the user if they want to encrypt or decrypt a message
    action = input("Do you want to encrypt or decrypt a message? (e/d/q to quit): ").strip().lower()
    if action not in ['e', 'd', 'q']:
        # If the input is not valid, prompt the user again
        print("Invalid input. Please enter 'e' to encrypt or 'd' to decrypt.")
        continue
    elif action == 'e':
        # User input for the message to encrypt
        message = input("Enter the message to encrypt: ")
        # Encrypt the message
        encrypted_message = f.encrypt(message.encode())
        print("Encrypted message:", encrypted_message.decode())
    elif action == 'd':
        # User input for the encrypted message to decrypt
        encrypted_message = input("Enter the encrypted message to decrypt: ")
        try:
            # Decrypt the message
            decrypted_message = f.decrypt(encrypted_message.encode()).decode()
            print("Decrypted message:", decrypted_message)
        except Exception as e:
            print("Error decrypting the message:", e)
    else:
        print("Exiting the program.")
        break