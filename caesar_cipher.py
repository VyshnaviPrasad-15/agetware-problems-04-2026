def caesar_cipher(message, shift):
    result = []
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

def encode(message, shift):
    return caesar_cipher(message, shift)

def decode(message, shift):
    return caesar_cipher(message, -shift)

if __name__ == "__main__":
    while True:
        print("\n=== Caesar Cipher ===")
        print("1. Encode")
        print("2. Decode")
        
        choice = input("Enter your choice (1/2): ").strip()
        
        if choice not in ['1', '2']:
            print("Invalid choice! Please enter 1 or 2.")
        else:
            message = input("Enter the message: ")
            try:
                shift = int(input("Enter the shift value: "))
            except ValueError:
                print("Invalid shift! Please enter an integer.")
                continue
            
            if choice == '1':
                result = encode(message, shift)
                print(f"Encoded message: {result}")
            elif choice == '2':
                result = decode(message, shift)
                print(f"Decoded message: {result}")

        cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            print("Goodbye!")
            break
