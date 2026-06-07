import subprocess

print("██╗  ██╗███████╗██╗  ██╗███████╗████████╗██████╗ ██╗██╗  ██╗███████╗\n██║  ██║██╔════╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝\n███████║█████╗   ╚███╔╝ ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗\n██╔══██║██╔══╝   ██╔██╗ ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝\n██║  ██║███████╗██╔╝ ██╗███████║   ██║   ██║  ██║██║██║  ██╗███████╗\n╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝\nCybersecurity Framework v1.0")

menu = """
[01] ► Reconnaissance
[02] ► Network Analysis
[03] ► Web Security
[04] ► Encryption & Cryptography
[05] ► AI Modules
[06] ► Utilities

[00] ► Exit

"""

print(menu)


while(1):
    choice = input("Select an option: ")

    if choice == "01":
        subprocess.run(["python", "modules/encryption/caeser.py"])
    elif choice == "02":
        subprocess.run(["python", "modules/encryption/caeser.py"])
    elif choice == "00":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")



