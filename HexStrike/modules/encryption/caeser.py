import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

while True:
    clear()

    print(r"""
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

                 Caesar Cipher Tool
""")

    print("""
═══════════════════════════════════════════════
                 CAESAR CIPHER
═══════════════════════════════════════════════

[01] ► Encrypt Text
[02] ► Decrypt Text
[00] ► Back

═══════════════════════════════════════════════
""")

    choice = input("Select an option: ")

    if choice == "01":
        text = input("\nEnter plaintext: ")
        shift = int(input("Enter shift value: "))
        result = caesar_encrypt(text, shift)

        print("\n[+] Encrypted Text:")
        print(result)
        input("\nPress Enter to continue...")

    elif choice == "02":
        text = input("\nEnter ciphertext: ")
        shift = int(input("Enter shift value: "))
        result = caesar_decrypt(text, shift)

        print("\n[+] Decrypted Text:")
        print(result)
        input("\nPress Enter to continue...")

    elif choice == "00":
        break

    else:
        input("\n[-] Invalid option. Press Enter to continue...")