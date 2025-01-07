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

# Clear Screen
os.system('clear')

# D-TECH Banner
def banner():
    print(f"""{CYAN}{BOLD}
      ╔══════════════════════════════════════════════════╗
      ║                                                  ║
      ║              🌐 ABOUT D-TECH HQ 🌐              ║
      ║      Innovation, Technology, and Excellence      ║
      ║                                                  ║
      ╚══════════════════════════════════════════════════╝
      {YELLOW}Your Gateway to Advanced Tools and Technology{RESET}
    """)

# About D-TECH
def about_dtech():
    print(f"""{GREEN}
D-TECH is an innovative tech hub focused on developing advanced tools, 
automation scripts, and digital utilities. Our mission is to empower users 
with cutting-edge tools while maintaining simplicity and efficiency.

Key Focus Areas:
- Account Management Tools (e.g., Netflix, Disney+ Checkers)
- Security and Ethical Hacking Tools
- Web Development and Hosting Solutions
- Advanced Terminal Tools and Utilities

Connect with us:
{CYAN}YouTube:{RESET} {YELLOW}https://youtube.com/@d-tech_services?si=GawSKGaSNPctQOfi{RESET}
{CYAN}Telegram:{RESET} {YELLOW}https://t.me/DTECHXPORT{RESET}
{CYAN}Admin Contact:{RESET} {YELLOW}@PREASX24{RESET}

Join us on our journey towards redefining the tech landscape.
    """)

# Fun Trick Options
def fun_tricks():
    while True:
        print(f"""{CYAN}
Select a Fun Trick to Execute:
{YELLOW}[1]{RESET} Play Classic Snake Game
{YELLOW}[2]{RESET} Display D-TECH in Figlet Style
{YELLOW}[3]{RESET} Display D-TECH in Toilet Style
{YELLOW}[4]{RESET} System Info with Neofetch
{YELLOW}[5]{RESET} Fire Animation with Cacafire
{YELLOW}[6]{RESET} Open Joke Website
{YELLOW}[7]{RESET} Matrix Animation
{YELLOW}[8]{RESET} Exit to Main Menu

{YELLOW}Note:{RESET} {GREEN}If you want to return to this menu after launching a trick, press {YELLOW}CTRL + C{RESET}.
        """)
        choice = input(f"{CYAN}Choose an option: {RESET}")
        
        if choice == '1':
            print(f"{GREEN}Launching Classic Snake Game...{RESET}")
            os.system("pkg install nsnake -y && nsnake")
        elif choice == '2':
            print(f"{GREEN}Displaying D-TECH in Figlet Style...{RESET}")
            os.system("pkg install figlet -y && figlet D-TECH")
        elif choice == '3':
            print(f"{GREEN}Displaying D-TECH in Toilet Style...{RESET}")
            os.system("pkg install toilet -y && toilet -f mono12 -F gay D-TECH")
        elif choice == '4':
            print(f"{GREEN}Displaying System Info with Neofetch...{RESET}")
            os.system("pkg install neofetch -y && neofetch")
        elif choice == '5':
            print(f"{GREEN}Launching Fire Animation...{RESET}")
            os.system("pkg install libcaca -y && cacafire")
        elif choice == '6':
            print(f"{GREEN}Opening Joke Website...{RESET}")
            os.system("termux-open-url https://icanhazdadjoke.com/")
        elif choice == '7':
            print(f"{GREEN}Launching Matrix Animation...{RESET}")
            os.system("pkg install cmatrix -y && cmatrix")
        elif choice == '8':
            print(f"{YELLOW}Returning to Main Menu...{RESET}")
            time.sleep(1)
            os.system('python main.py')
            break
        else:
            print(f"{RED}Invalid option. Please try again.{RESET}")
            time.sleep(1)

# Main Execution
if __name__ == '__main__':
    banner()
    about_dtech()
    input(f"{CYAN}Press Enter to explore Fun Tricks...{RESET}")
    fun_tricks()