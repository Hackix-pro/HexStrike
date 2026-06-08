import subprocess
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_ui():
    print("""
██╗  ██╗███████╗██╗  ██╗███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
██║  ██║██╔════╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝
███████║█████╗   ╚███╔╝ ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗
██╔══██║██╔══╝   ██╔██╗ ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝
██║  ██║███████╗██╔╝ ██╗███████║   ██║   ██║  ██║██║██║  ██╗███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝

Cybersecurity Framework v1.0
""")

    print("""
[01] ► Encryption
[02] ► --
[03] ► --
[04] ► --
[05] ► --
[06] ► --

[00] ► Exit
""")

while True:
    clear()
    show_ui()

    choice = input("Select an option: ")

    if choice == "01":
        subprocess.run(["python", "modules/encryption/main.py"])

    elif choice == "02":
        subprocess.run(["python", "modules/encryption/caeser.py"])

    elif choice == "00":
        print("Exiting...")
        break

    else:
        input("Invalid option. Press Enter...")