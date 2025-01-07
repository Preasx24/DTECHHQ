import os
import time
import sys

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Clear screen
os.system('clear')

# D-TECH HQ Banner
def banner():
    print(f"""{CYAN}{BOLD}
      ╔══════════════════════════════════════════════════╗
      ║                                                  ║
      ║            🌐 WELCOME TO D-TECH HQ 🌐            ║
      ║       Your Gateway to Advanced Operations       ║
      ║                                                  ║
      ╚══════════════════════════════════════════════════╝
      {YELLOW}          Explore the Power of D-TECH Tools...{RESET}
    """)

# Loading Animation
def loading_animation():
    print(f"{GREEN}Loading Dashboard...{RESET}")
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
                 "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", 
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in animation:
        time.sleep(0.2)
        sys.stdout.write(f"\r{CYAN}{i} {RESET}")
        sys.stdout.flush()
    print(f"\n{GREEN}Welcome to the Dashboard!{RESET}\n")

# Menu Options
def main_menu():
    while True:
        os.system('clear')
        banner()
        print(f"""{YELLOW}
[1] 📚 ABOUT D-TECH
[2] 🛠️ ACCOUNT CHECKERS
[3] 🎁 FREE ACCOUNTS
[4] ⚙️ EXTRA TOOLS
[5] 🚪 EXIT
{RESET}""")
        choice = input(f"{CYAN}Choose an option: {RESET}")
        
        if choice == '1':
            print(f"{GREEN}Redirecting to ABOUT D-TECH...{RESET}")
            time.sleep(1)
            os.system('python about.py')
        elif choice == '2':
            print(f"{GREEN}Redirecting to ACCOUNT CHECKERS...{RESET}")
            time.sleep(1)
            os.system('python checker.py')
        elif choice == '3':
            print(f"{GREEN}Redirecting to FREE ACCOUNTS...{RESET}")
            time.sleep(1)
            os.system('python free_accounts.py')
        elif choice == '4':
            print(f"{GREEN}Redirecting to EXTRA TOOLS...{RESET}")
            time.sleep(1)
            os.system('python extra_tools.py')
        elif choice == '5':
            print(f"{RED}Exiting D-TECH HQ. Goodbye!{RESET}")
            time.sleep(1)
            exit()
        else:
            print(f"{RED}Invalid Option! Try again.{RESET}")
            time.sleep(1)

# Run the Dashboard
if __name__ == '__main__':
    banner()
    loading_animation()
    main_menu()
