import string

def caesar_encrypt(message, key):
    shift = key % 26
    chiper = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(chiper)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    message = encrypted_message.translate(cipher)
    return message

message = 'test aja'
key = 4

encrypted_message = caesar_encrypt(message, key)
print(f"pesan terenkripsi: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"pesan terdekripsi: {decrypted_message}")