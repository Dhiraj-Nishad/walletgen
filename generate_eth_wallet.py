import json
import os
from eth_account import Account
from mnemonic import Mnemonic

# Enable unaudited HD wallet features
Account.enable_unaudited_hdwallet_features()

def generate_wallets(num_wallets):
    wallets = []
    mnemo = Mnemonic("english")

    for _ in range(num_wallets):
        # Generate a random mnemonic phrase
        mnemonic_phrase = mnemo.generate(strength=256)
        seed = mnemo.to_seed(mnemonic_phrase)
        
        # Generate an Ethereum account from the seed
        account = Account.from_mnemonic(mnemonic_phrase)

        # Store wallet information
        wallet_info = {
            "mnemonic": mnemonic_phrase,
            "private_key": account.privateKey.hex(),
            "public_key": account.address
        }
        
        wallets.append(wallet_info)

    return wallets

def save_to_json(wallets, filename='wallets.json'):
    with open(filename, 'w') as json_file:
        json.dump(wallets, json_file, indent=4)
    print(f"Wallets saved to {filename}")

def main():
    try:
        num_wallets = int(input("Enter the number of Ethereum wallets to generate: "))
        if num_wallets <= 0:
            print("Please enter a positive integer.")
            return
        
        wallets = generate_wallets(num_wallets)
        save_to_json(wallets)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
