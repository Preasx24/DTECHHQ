import os
import time
import sys

# Colors
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def extra_tools_menu():
    while True:
        os.system('clear')
        print(f"""
{CYAN}
╔══════════════════════════════════════╗
║           🔧 D-TECH EXTRA TOOLS      ║
╚══════════════════════════════════════╝
{YELLOW}Choose an extra tool to use!{RESET}

[1] Email:Password Extractor
[2] More tools coming soon...
[3] Exit to Main Menu
""")
        
        choice = input(f"{CYAN}Choose an option: {RESET}")
        
        if choice == '1':
            print(f"{GREEN}Launching Email:Password Extractor...{RESET}")
            time.sleep(1)
            os.system("python3 mail.py")
        elif choice == '2':
            print(f"{YELLOW}Stay tuned! More tools are coming soon...{RESET}")
            time.sleep(2)
        elif choice == '3':
            print(f"{GREEN}Returning to the main menu...{RESET}")
            time.sleep(1)
            os.system("python3 main.py")
            sys.exit()
        else:
            print(f"{RED}Invalid Option! Please try again.{RESET}")
            time.sleep(1)

if __name__ == '__main__':
    extra_tools_menu()