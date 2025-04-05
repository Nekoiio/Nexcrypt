#!/usr/bin/env python3

import argparse
import os
import getpass
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def encrypt_file(input_file, password, output_file):
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM)

    with open(input_file, "rb") as f:
        plaintext = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    with open(output_file, "wb") as f:
        f.write(salt + cipher.nonce + tag + ciphertext)

    print(f"File encrypted: {output_file}")

def decrypt_file(input_file, password, output_file):
    with open(input_file, "rb") as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        with open(output_file, "wb") as f:
            f.write(plaintext)
        print(f"File decrypted: {output_file}")
    except ValueError:
        print("Decryption failed: Incorrect password or file tampered.")

def main():
    parser = argparse.ArgumentParser(description="nexcrypt - Encrypt or decrypt files using AES-GCM.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encode", "-e", action="store_true", help="Encrypt the file")
    group.add_argument("--decode", "-d", action="store_true", help="Decrypt the file")
    parser.add_argument("-f", "--file", required=True, help="Input file path")
    parser.add_argument("-p", "--password", help="Password (if not provided, you will be prompted securely)")
    parser.add_argument("-o", "--output", help="Output file path")

    args = parser.parse_args()

    password = args.password
    if not password:
        password = getpass.getpass("Enter password: ")

    if args.encode:
        output_file = args.output if args.output else "encrypted.bin"
        encrypt_file(args.file, password, output_file)
    elif args.decode:
        output_file = args.output if args.output else "decrypted.txt"
        decrypt_file(args.file, password, output_file)

if __name__ == "__main__":
    main()
