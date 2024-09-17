# Simple ransomware script using python

> [!NOTE]
> This script is not a real ransomware, it just encrypts the files in the directory where it is executed. It is for educational purposes only.

## Requirements

- Python 3.x
- `cryptography` library

You can install the required dependencies using:

```bash
pip install cryptography
```

## Features

- Encrypts files in a specified folder and its subfolders.
- Decrypts the encrypted files using a predefined key.
- Skips banned files and folders.
- Easy to use and customizable.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/dangkhoaw/ransomware.git
```

2. Change the directory:

```bash
cd ransomware
```

3. Run the script:

```bash
python main.py
```
