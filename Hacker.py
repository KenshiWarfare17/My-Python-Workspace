import time
import random
import sys

def fake_loading(text):
    print(text, end="")
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="")
        sys.stdout.flush()
    print(" DONE")

def fake_password_crack():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for _ in range(12):
        time.sleep(0.2)
        password += random.choice(chars)
        print(f"Cracking: {password}")
    print("\nPassword Found: ************")

def main():
    print("Initializing Secure Terminal...")
    time.sleep(1)

    fake_loading("Connecting to server")
    fake_loading("Bypassing firewall")
    fake_loading("Decrypting data")

    print("\nStarting brute force attack...")
    fake_password_crack()

    print("\nAccess Granted!")
    print("Just kidding 😄 This is only a simulation.")

if __name__ == "__main__":
    main()