import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, key, encrypt=True):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    shifted_alphabet = alphabet[key:] + alphabet[:key]
    shifted_numbers = numbers[key % 10:] + numbers[:key % 10]

    cipher_text = ""

    for char in text.lower():
        if char == " ":
            cipher_text += "-"  # Replace space with '-'
        elif char in alphabet:
            index = alphabet.index(char)
            cipher_text += shifted_alphabet[index] if encrypt else alphabet[shifted_alphabet.index(char)]
        elif char in numbers:
            index = numbers.index(char)
            cipher_text += shifted_numbers[index] if encrypt else numbers[shifted_numbers.index(char)]
        else:
            cipher_text += char  # Keep special characters unchanged

    return cipher_text

def get_key():
    """Safely retrieve key input and validate"""
    try:
        key = int(entry_key.get().strip())  # Convert input to integer
        if not (1 <= key <= 26):
            raise ValueError  # Ensures key is within valid range
        return key
    except ValueError:
        messagebox.showerror("Error", "Key must be a number between 1-26")
        return None

def encrypt_message():
    message = entry_message.get()
    key = get_key()
    
    if key is None:
        return  # Stop if key is invalid

    encrypted = caesar_cipher(message, key, encrypt=True)
    label_result.config(text=f"Encrypted Message: {encrypted}")

def decrypt_message():
    message = entry_message.get()
    key = get_key()
    
    if key is None:
        return  # Stop if key is invalid

    decrypted = caesar_cipher(message, key, encrypt=False).replace("-", " ")
    label_result.config(text=f"Decrypted Message: {decrypted}")

# GUI Setup 
root = tk.Tk()
root.title("Caesar Cipher Encryptor")

# Message Label and Entry
tk.Label(root, text="Enter Message:").grid(row=0, column=0, padx=10, pady=10)
entry_message = tk.Entry(root, width=40)
entry_message.grid(row=0, column=1, padx=10, pady=10)

# Key Label and Entry
tk.Label(root, text="Enter Key (1-26):").grid(row=1, column=0, padx=10, pady=10)
entry_key = tk.Entry(root, width=5)  
entry_key.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Encrypt Button
btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message, bg="lightblue")
btn_encrypt.grid(row=2, column=0, padx=10, pady=10)

# Decrypt Button
btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message, bg="lightgreen")
btn_decrypt.grid(row=2, column=1, padx=10, pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run GUI
root.mainloop()
