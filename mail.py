import re
import time
import sys
import os
from colorama import Fore, init

# Initialize colorama
init()

def print_banner():
    # Clear the terminal for a clean look
    os.system('clear')

    # Display a nice, simple banner
    print(f"{Fore.CYAN}===============================")
    print(f"  e-mail: password extractor  ")
    print(f"==============================={Fore.RESET}")

    # Simulate a loading bar
    print(f"\n{Fore.GREEN}Loading data...", end="")
    sys.stdout.flush()
    for i in range(30):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"{Fore.RESET}\n")

def extract_email_password(text):
    pattern = re.compile(r'(\S+@\S+)\s*:\s*(\S+)')
    matches = pattern.findall(text)
    return matches

def process_accounts():
    # Display the banner
    print_banner()

    # Prompt user to input the file path
    input_file_path = input(f'{Fore.GREEN}Enter the path to the input file: {Fore.RESET}')
    
    try:
        with open(input_file_path, 'r') as infile:
            content = infile.read()
            results = extract_email_password(content)
            if results:
                print(f"\n{Fore.GREEN}Extracting email:password pairs...\n{Fore.RESET}")
                time.sleep(1)  # Brief pause before displaying results
                for email, password in results:
                    print(f"{Fore.YELLOW}{email}:{password}{Fore.RESET}")
            else:
                print(f"{Fore.RED}No valid email:password pairs found.{Fore.RESET}")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{input_file_path}' not found.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Fore.RESET}")

# Run the processing function
process_accounts()