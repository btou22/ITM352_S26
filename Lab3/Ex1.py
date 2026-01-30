from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encoded_text = cipher_suite.encrypt(b"This is a really secret message")
print(f"Encoded text: {encoded_text}")

# Use the cryptography library to encode and decode a message
decoded_text = cipher_suite.decrypt(encoded_text)
print(f"Decoded text: {decoded_text.decode('utf-8')}")
