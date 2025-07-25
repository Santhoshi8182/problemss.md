def caesar_cipher(text, shift, encode=True):
    if not encode:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

# Example usage:
encoded = caesar_cipher("Hello, World!", 3, encode=True)
decoded = caesar_cipher(encoded, 3, encode=False)
print("Encoded:", encoded)
print("Decoded:", decoded)
