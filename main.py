import csv
import json
from eth_account import Account

def get_address(private_key):
    try:
        account = Account.from_key(private_key)
        return account.address
    except ValueError as e:
        print(f"Error processing private key: {private_key}. Reason: {str(e)}")
        return None

def save_to_json(data):
    filename = f'all_data.json'
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

def save_to_csv(data):
    filename = "all_data.csv"
    fields = ["private_key", "wallet_address"]

    with open(filename, mode="w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

def main():
    print("-------------------------------------------")
    print("****************Oblakov_0372***************")
    print()
    all_data = []
    
    with open('./private_keys.txt', 'r') as file:
        private_keys = file.read().splitlines()

    for private_key in private_keys:
        wallet_address = get_address(private_key)
        if wallet_address is not None:
            all_data.append({"private_key": private_key, "wallet_address": wallet_address})

    save_to_json(all_data)
    save_to_csv(all_data)

if __name__ == '__main__':
    main()
