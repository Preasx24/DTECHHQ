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

# Voucher Instructions
def voucher_instructions():
    print(f"""{YELLOW}
If you don't have a voucher, follow these steps to get one:

1. Visit our website: {CYAN}www.dtech24.co.za{YELLOW}
2. Click on the "{GREEN}ETC{YELLOW}" option.
3. Select the "{GREEN}Next Page{YELLOW}" option.
4. Click on the "{GREEN}D-TECH Voucher{YELLOW}" button.
5. Press "{GREEN}Claim{YELLOW}" and copy the provided voucher.

Or watch our video tutorial:
{CYAN}https://youtube.com/shorts/rRSRa6p68AA?si=gO-2uUe011HTFQHX{RESET}

Once you have your voucher, paste it below to gain access.
    """)
    input(f"{CYAN}Press Enter to continue...{RESET}")

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

# Main Program
if __name__ == '__main__':
    banner()
    loading_animation()
    while True:
        print(f"{YELLOW}Do you have a voucher?{RESET}")
        print(f"{GREEN}[1] Yes, I have a voucher.{RESET}")
        print(f"{CYAN}[2] No, I need instructions on how to get one.{RESET}")
        choice = input(f"{CYAN}Select an option: {RESET}")
        
        if choice == '1':
            if voucher_check():
                fake_login()
                os.system('python dashboard.py')
                break
        elif choice == '2':
            voucher_instructions()
        else:
            print(f"{RED}Invalid option. Please try again.{RESET}")
            time.sleep(1)