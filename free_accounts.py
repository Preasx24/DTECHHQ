import os
import random
import time
import sys

# Colors
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Temporary lock file
TEMP_LOCK_FILE = "temp_free_access.lock"

def mark_access():
    with open(TEMP_LOCK_FILE, "w") as file:
        file.write("locked")

def has_accessed():
    return os.path.exists(TEMP_LOCK_FILE)

def clear_access():
    if os.path.exists(TEMP_LOCK_FILE):
        os.remove(TEMP_LOCK_FILE)

def get_free_account(service_name):
    try:
        with open(f"{service_name}_accounts.txt", "r") as file:
            accounts = file.readlines()
            if accounts:
                account = random.choice(accounts).strip()
                print(f"\n{GREEN}Your free {service_name} account: {CYAN}{account}{RESET}")
                return account
            else:
                print(f"{RED}No accounts available for {service_name}.{RESET}")
                return None
    except FileNotFoundError:
        print(f"{RED}Error: {service_name}_accounts.txt not found.{RESET}")
        return None

def free_accounts():
    if has_accessed():
        print(f"{RED}\nYou have already accessed free accounts in this session. Returning to the main menu...{RESET}")
        time.sleep(2)
        clear_access()  # Unlock access after returning to main.py
        os.system("python main.py")  # Redirect back to main.py
        sys.exit()

    mark_access()  # Lock access for this session

    while True:
        os.system('clear')
        print(f"""
{CYAN}
╔══════════════════════════════════════╗
║          🎁 FREE ACCOUNTS            ║
╚══════════════════════════════════════╝
{YELLOW}Choose an option to get a free account!{RESET}
        
[1] Crunchyroll
[2] Rillabox
[3] Ubisoft
[4] Netflix
[5] Call of Duty
[6] Exit
""")

        choice = input(f"{CYAN}Choose an option: {RESET}")
        
        if choice == '1':
            get_free_account('crunchyroll')
        elif choice == '2':
            get_free_account('rillabox')
        elif choice == '3':
            get_free_account('ubisoft')
        elif choice == '4':
            get_free_account('netflix')
        elif choice == '5':
            get_free_account('callofduty')
        elif choice == '6':
            print(f"{GREEN}Returning to the main menu...{RESET}")
            clear_access()  # Unlock access after normal exit
            time.sleep(1)
            os.system("python main.py")  # Redirect back to main.py
            sys.exit()
        else:
            print(f"{RED}Invalid Option! Try again.{RESET}")
            time.sleep(1)