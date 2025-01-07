import os
import time
import sys

# Colors
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def account_checker_menu():
    while True:
        os.system('clear')
        print(f"""
{CYAN}
╔══════════════════════════════════════╗
║       🔍 D-TECH ACCOUNT CHECKERS     ║
╚══════════════════════════════════════╝
{YELLOW}Choose an option to check accounts!{RESET}

[1] Crunchyroll Premium Account Checker
[2] Ubisoft Account Checker
[3] Rillabox Account Checker
[4] Panda Account Checker
[5] More Coming Soon...
[6] Exit to Main Menu
""")
        
        choice = input(f"{CYAN}Choose an option: {RESET}")
        
        if choice == '1':
            print(f"{GREEN}Launching Crunchyroll Premium Account Checker...{RESET}")
            time.sleep(1)
            os.system("python3 crunchyroll.py")
        elif choice == '2':
            print(f"{GREEN}Launching Ubisoft Account Checker...{RESET}")
            time.sleep(1)
            os.system("python3 ubisoft.py")
        elif choice == '3':
            print(f"{GREEN}Launching Rillabox Account Checker...{RESET}")
            time.sleep(1)
            os.system("python3 rillabox.py")
        elif choice == '4':
            print(f"{GREEN}Launching Panda Account Checker...{RESET}")
            time.sleep(1)
            os.system("python3 panda.py")
        elif choice == '5':
            print(f"{YELLOW}Stay tuned! More tools are coming soon...{RESET}")
            time.sleep(2)
        elif choice == '6':
            print(f"{GREEN}Returning to the main menu...{RESET}")
            time.sleep(1)
            os.system("python3 main.py")
            sys.exit()
        else:
            print(f"{RED}Invalid Option! Please try again.{RESET}")
            time.sleep(1)

if __name__ == '__main__':
    account_checker_menu()