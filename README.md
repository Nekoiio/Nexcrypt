# 🔐 nexcrypt

A simple command-line file encryption and decryption tool using AES-GCM and a password-based key. Secure and minimal, designed for fast local encryption from the terminal.

---

## ✅ Features

- AES-256-GCM encryption for confidentiality and integrity
- Key derivation using PBKDF2
- Password prompt with hidden input
- CLI interface with flags
- Lightweight and easy to install

---

## 📦 Dependencies

Make sure you have the following installed:

- Python 3.x
- [`pycryptodome`](https://pypi.org/project/pycryptodome/)

You can install it using:

```bash
pip install pycryptodome
```
---

## 🚀 Setup

To install `nexcrypt` as a global command:

1. Clone or download the project folder.
2. Make the setup script executable:

```bash
chmod +x setup.sh
```

3. Run the script:

```bash
./setup.sh
```

After that, you can use `nexcrypt` from anywhere in your terminal.

---

## 🔧 Usage

### Encrypt a file

```bash
nexcrypt --encode -f input.txt -o encrypted.bin
```

You'll be prompted to enter a password securely.

### Decrypt a file

```bash
nexcrypt --decode -f encrypted.bin -o decrypted.txt
```

You can also pass the password directly using `-p`, though it's less secure:

```bash
nexcrypt -e -f input.txt -p mysecretpassword -o encrypted.bin
```

---

## ❌ Uninstall

To remove `nexcrypt` from your system:

```bash
chmod +x remove.sh
./remove.sh
```

---

## 📁 Files

- `nexcrypt.py` – Main Python script
- `setup.sh` – Installation script
- `remove.sh` – Uninstallation script
- `README.md` – This file

---

## 🔒 Disclaimer

This tool was made as a fun project and for casual personal use. Do **not** use it to store or transmit sensitive data without understanding the security implications.
