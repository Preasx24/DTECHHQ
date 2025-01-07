import os
import time
import sys
import requests

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Voucher Config
VOUCHER_URL = "https://raw.githubusercontent.com/Preasx24/D-TECH_CHAT/refs/heads/main/voucher.txt"
LOCAL_VOUCHER_FILE = "vou.txt"

# Clear screen
os.system('clear')

# D-TECH HQ Sleek Banner
def banner():
    print(f"""{CYAN}{BOLD}
      ╔══════════════════════════════════════════════════╗
      ║                                                  ║
      ║            🌐 WELCOME TO D-TECH HQ 🌐            ║
      ║        Advanced Terminal Control System         ║
      ║                                                  ║
      ╚══════════════════════════════════════════════════╝
      {YELLOW}          Prepare to Enter the D-TECH Realm...{RESET}
    """)

# Loading Animation
def loading_animation():
    print(f"{GREEN}Initializing D-TECH Systems...{RESET}")
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
                 "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", 
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in animation:
        time.sleep(0.3)
        sys.stdout.write(f"\r{CYAN}{i} {RESET}")
        sys.stdout.flush()
    print(f"\n{GREEN}System Ready!{RESET}\n")

# Step 1: Voucher Validation
def validate_voucher(voucher):
    try:
        response = requests.get(VOUCHER_URL)
        if response.status_code == 200:
            valid_vouchers = response.text.splitlines()
            if voucher in valid_vouchers:
                print(f"{GREEN}Voucher is valid! Proceeding to Step 2...{RESET}")
                return True
            else:
                print(f"{RED}Invalid Voucher! Access Denied.{RESET}")
                return False
        else:
            print(f"{RED}Failed to verify voucher. Try again later.{RESET}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error: {e}{RESET}")
        return False

# Step 2: Check if Voucher is Used
def is_voucher_used(voucher):
    if not os.path.exists(LOCAL_VOUCHER_FILE):
        open(LOCAL_VOUCHER_FILE, 'w').close()
    
    with open(LOCAL_VOUCHER_FILE, 'r') as file:
        used_vouchers = file.read().splitlines()
    
    if voucher in used_vouchers:
        print(f"{RED}This voucher has already been used!{RESET}")
        return True
    return False

# Save Used Voucher
def mark_voucher_as_used(voucher):
    with open(LOCAL_VOUCHER_FILE, 'a') as file:
        file.write(voucher + '\n')

# Authentication Prompt (Fake for Style)
def fake_login():
    username = input(f"{YELLOW}Username: {RESET}")
    password = input(f"{YELLOW}Password: {RESET}")
    print(f"{CYAN}Verifying Credentials...{RESET}")
    time.sleep(1.5)
    print(f"{GREEN}Access Granted! Welcome, {username}.{RESET}\n")
    time.sleep(1)

# Voucher Check System
def voucher_check():
    print(f"{YELLOW}Voucher Authentication Required:{RESET}")
    voucher = input(f"{CYAN}Enter your D-TECH Voucher: {RESET}")
    
    if validate_voucher(voucher):
        if not is_voucher_used(voucher):
            mark_voucher_as_used(voucher)
            print(f"{GREEN}Voucher Accepted! Access Granted.{RESET}\n")
            return True
        else:
            print(f"{RED}Access Denied. Voucher already used.{RESET}")
            return False
    else:
        return False

# About D-TECH
def about_dtech():
    os.system('clear')
    print(f"""{CYAN}
    ╔════════════════════════════════╗
    ║         📚 ABOUT D-TECH         ║
    ╚════════════════════════════════╝
    {YELLOW}
    D-TECH is an advanced toolkit designed for 
    automation, account validation, and network analysis.
    Developed with precision and innovation, D-TECH is 
    your gateway to powerful tools and seamless operations.
    {RESET}
    """)
    input(f"{CYAN}Press Enter to return to the menu...{RESET}")

# Checkers Menu
def checkers():
    os.system('clear')
    print(f"""{CYAN}
    ╔══════════════════════════╗
    ║        🛠️ CHECKERS        ║
    ╚══════════════════════════╝
    {YELLOW}Coming Soon: Advanced Account Checkers!{RESET}
    """)
    input(f"{CYAN}Press Enter to return to the menu...{RESET}")

# Free Accounts
def free_accounts():
    os.system('clear')
    print(f"""{CYAN}
    ╔══════════════════════════════╗
    ║       🎁 FREE ACCOUNTS        ║
    ╚══════════════════════════════╝
    {YELLOW}Netflix, Disney+, and more...{RESET}
    """)
    input(f"{CYAN}Press Enter to return to the menu...{RESET}")

# Extra Tools
def extra_tools():
    os.system('clear')
    print(f"""{CYAN}
    ╔═════════════════════════╗
    ║       ⚙️ EXTRA TOOLS       ║
    ╚═════════════════════════╝
    {YELLOW}VPN Connector, SSH Automation, and more!{RESET}
    """)
    input(f"{CYAN}Press Enter to return to the menu...{RESET}")

# Main Menu
def main_menu():
    while True:
        os.system('clear')
        banner()
        print(f"""{YELLOW}
[1] 📚 About D-TECH
[2] 🛠️ Checkers
[3] 🎁 Free Accounts
[4] ⚙️ Extra Tools
[5] 🚪 Exit
{RESET}""")
        choice = input(f"{CYAN}Choose an option: {RESET}")
        if choice == '1':
            about_dtech()
        elif choice == '2':
            checkers()
        elif choice == '3':
            free_accounts()
        elif choice == '4':
            extra_tools()
        elif choice == '5':
            print(f"{RED}Exiting D-TECH HQ. Goodbye!{RESET}")
            exit()
        else:
            print(f"{RED}Invalid Option! Try again.{RESET}")
            time.sleep(1)

# Run the script
if __name__ == '__main__':
    banner()
    loading_animation()
    if voucher_check():
        fake_login()
        main_menu()