import json
from eth_account import Account
from mnemonic import Mnemonic
from datetime import datetime
import os

# Enable unaudited HD wallet features
Account.enable_unaudited_hdwallet_features()

def generate_wallets(num_wallets):
    """Generate the specified number of Ethereum wallets."""
    wallets = []
    mnemo = Mnemonic("english")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for i in range(num_wallets):
        # Generate a random mnemonic phrase
        mnemonic_phrase = mnemo.generate(strength=256)
        
        # Generate an Ethereum account from the mnemonic phrase
        account = Account.from_mnemonic(mnemonic_phrase)

        # Store wallet information
        wallet_info = {
            "index": i + 1,
            "timestamp": timestamp,
            "mnemonic": mnemonic_phrase,
            "private_key": account._private_key.hex(),
            "public_key": account.address
        }
        
        wallets.append(wallet_info)

    return wallets

def save_to_json(wallets, filename='wallets.json'):
    """Save wallet information to a JSON file."""
    try:
        with open(filename, 'w') as json_file:
            json.dump(wallets, json_file, indent=4)
        print(f"Wallets saved to {filename}")
    except Exception as e:
        print(f"Error saving to JSON file: {str(e)}")

def save_to_txt(wallets, filename='wallets.txt'):
    """Save wallet information to a formatted text file."""
    try:
        with open(filename, 'w') as txt_file:
            txt_file.write(f"Generated on: {wallets[0]['timestamp']}\n")
            txt_file.write("=" * 70 + "\n\n")
            
            for wallet in wallets:
                txt_file.write(f"Wallet #{wallet['index']}\n")
                txt_file.write("-" * 70 + "\n")
                txt_file.write(f"Private Key: {wallet['private_key']}\n")
                txt_file.write(f"Mnemonic Phrase: {wallet['mnemonic']}\n")
                txt_file.write(f"Public Address: {wallet['public_key']}\n")
                txt_file.write("\n" + "=" * 70 + "\n\n")
        print(f"Wallets saved to {filename}")
    except Exception as e:
        print(f"Error saving to text file: {str(e)}")

def validate_filename(filename):
    """Validate and sanitize the filename."""
    if not filename:
        return False
    try:
        # Remove any directory path
        filename = os.path.basename(filename)
        # Check if the filename is valid
        return '.' in filename and len(filename) > 1
    except:
        return False

def main():
    """Main execution function with error handling."""
    try:
        # Get number of wallets
        num_wallets = int(input("Enter the number of Ethereum wallets to generate: "))
        if num_wallets <= 0:
            print("Please enter a positive integer.")
            return

        # Optional custom filenames
        json_filename = input("Enter JSON filename (press Enter for default 'wallets.json'): ")
        txt_filename = input("Enter TXT filename (press Enter for default 'wallets.txt'): ")

        # Validate filenames
        json_filename = 'wallets.json' if not json_filename else json_filename
        txt_filename = 'wallets.txt' if not txt_filename else txt_filename

        if not validate_filename(json_filename) or not validate_filename(txt_filename):
            print("Invalid filename provided. Using default filenames.")
            json_filename = 'wallets.json'
            txt_filename = 'wallets.txt'

        # Generate and save wallets
        wallets = generate_wallets(num_wallets)
        save_to_json(wallets, json_filename)
        save_to_txt(wallets, txt_filename)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
