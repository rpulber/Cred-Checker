# Cred-Checker

# Multi-Connection Automation Script

This script automates connections to remote systems using RPC, SMB, and SSH.

## Introduction

The Multi-Connection Automation Script provides an easy-to-use solution for automating connections to remote systems using RPC, SMB, and SSH. This script is designed to simplify the login process and provide feedback on the status of each connection attempt.

## Features

- Automated login to remote systems using RPC, SMB, and SSH.
- Clear feedback on the success or failure of each connection attempt.
- Support for handling timeouts and unexpected situations.

## Usage

1. Run the script and provide the required information when prompted (IP, User, Password).
2. The script will attempt to connect using RPC, SMB, and SSH.
3. Check the console output for the status of each connection attempt.

```bash
# Example usage
python3 cred-checker.py
```

# Requirements
Python 3
pexpect library (install using pip install expect)
smbclient
rpcclient

# Installation
git clone https://github.com/rpulber/Cred-Checker.git

# Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
