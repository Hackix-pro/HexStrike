import os
import subprocess

def clear():
    os.system("cls" if os.name == "nt" else "clear")



while True:

    clear()

    print(r"""
    ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
    ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
    █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║
    ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║
    ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║
    ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝

                Encryption & Cryptography Suite
    """)

    menu = """
    ═══════════════════════════════════════════════
                  ENCRYPTION TOOLS
    ═══════════════════════════════════════════════

    [01] ► Caesar Cipher
    [02] ► Vigenère Cipher
    [03] ► XOR Cipher
    [04] ► Base64 Encoder/Decoder
    [05] ► Hash Generator
    [06] ► AES Encryption
    [07] ► RSA Encryption

    [99] ► Back to Main Menu

    ═══════════════════════════════════════════════
    """

    print(menu)


    choice = input("    Select an option: ")

    if choice == "01":
        print("Launching Caesar Cipher...")
        subprocess.run(["python", "modules/encryption/caeser.py"])

    elif choice == "02":
        print("Launching Vigenère Cipher...")

    elif choice == "03":
        print("Launching XOR Cipher...")

    elif choice == "04":
        print("Launching Base64 Tool...")

    elif choice == "05":
        print("Launching Hash Generator...")

    elif choice == "06":
        print("Launching AES Encryption...")

    elif choice == "07":
        print("Launching RSA Encryption...")

    elif choice == "99":
        break

    else:
        print("Invalid option.")