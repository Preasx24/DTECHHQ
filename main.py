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

# D-TECH Banner
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

# Validate Voucher
def validate_voucher(voucher):
    try:
        response = requests.get(VOUCHER_URL)
        if response.status_code == 200:
            valid_vouchers = response.text.splitlines()
            if voucher in valid_vouchers:
                print(f"{GREEN}Voucher is valid!{RESET}")
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

# Check if Voucher is Used
def is_voucher_used(voucher):
    if not os.path.exists(LOCAL_VOUCHER_FILE):
        open(LOCAL_VOUCHER_FILE, 'w').close()
    
    with open(LOCAL_VOUCHER_FILE, 'r') as file:
        used_vouchers = file.read().splitlines()
    
    if voucher in used_vouchers:
        print(f"{RED}This voucher has already been used!{RESET}")
        return True
    return False

# Mark Voucher as Used
def mark_voucher_as_used(voucher):
    with open(LOCAL_VOUCHER_FILE, 'a') as file:
        file.write(voucher + '\n')

# Voucher Authentication
def voucher_authentication():
    print(f"{YELLOW}Voucher Authentication Required:{RESET}")
    voucher = input(f"{CYAN}Enter your D-TECH Voucher: {RESET}")
    
    if validate_voucher(voucher):
        if not is_voucher_used(voucher):
            mark_voucher_as_used(voucher)
            print(f"{GREEN}Voucher Accepted! Redirecting to Dashboard...{RESET}")
            time.sleep(1)
            os.system('python dashboard.py')  # Call dashboard.py
        else:
            print(f"{RED}Access Denied. Voucher already used.{RESET}")
    else:
        print(f"{RED}Authentication Failed!{RESET}")

# Main Execution
if __name__ == '__main__':
    banner()
    loading_animation()
    voucher_authentication()