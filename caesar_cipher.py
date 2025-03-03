def caesar_cipher(text, shift, mode):
    result = ""
    
    # Iterate through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65) if mode == 'encrypt' else chr((ord(char) - shift - 65) % 26 + 65
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 97) % 26 + 97) if mode == 'encrypt' else chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, leave it unchanged
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Choose an option (1 or 2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == '1':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
