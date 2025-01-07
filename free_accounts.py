import random
import os
import time

# Colors for styling
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def get_free_account(service_name):
    try:
        # Define the account and used account file paths
        accounts_file = f"{service_name}_accounts.txt"
        used_accounts_file = f"{service_name}_used_accounts.txt"

        # If the used accounts file doesn't exist, create it
        if not os.path.exists(used_accounts_file):
            open(used_accounts_file, "w").close()

        # Read available accounts from the main file
        with open(accounts_file, "r") as file:
            available_accounts = file.readlines()

        # Read already used accounts
        with open(used_accounts_file, "r") as used_file:
            used_accounts = used_file.readlines()

        # Filter out used accounts from available accounts
        available_accounts = [acc for acc in available_accounts if acc not in used_accounts]

        if available_accounts:
            # Randomly select a new account from available accounts
            account = random.choice(available_accounts).strip()

            # Print the account
            print(f"Your free {service_name} account: {account}")

            # Save the account to the used accounts file
            with open(used_accounts_file, "a") as used_file:
                used_file.write(account + "\n")

            # Return the account
            return account
        else:
            print(f"No accounts available for {service_name}.")
            return None

    except FileNotFoundError:
        print(f"Error: {service_name}_accounts.txt not found.")
        return None

def free_accounts():
    while True:
        print(f"""
        {CYAN}
        ╔══════════════════════════════════════╗
        ║       🎁 FREE ACCOUNTS               ║
        ╚══════════════════════════════════════╝
        {YELLOW}Choose an option to get a free account!{RESET}
        
        [1] Crunchyroll
        [2] Rillabox
        [3] Netflix
        [4] Hulu
        [5] Ubisoft
        [6] Call of Duty
        [7] Exit
        """)

        choice = input(f"{CYAN}Choose an option: {RESET}")
        
        if choice == '1':
            get_free_account('crunchyroll')
        elif choice == '2':
            get_free_account('rillabox')
        elif choice == '3':
            get_free_account('netflix')
        elif choice == '4':
            get_free_account('hulu')
        elif choice == '5':
            get_free_account('ubisoft')
        elif choice == '6':
            get_free_account('call_of_duty')
        elif choice == '7':
            print(f"{RED}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid Option! Try again.{RESET}")
            time.sleep(1)

# Run the free account function
free_accounts()