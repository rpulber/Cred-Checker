import pexpect

ip = input("IP: ")
user = input("User: ")
password = input("Pass: ")

# RPC LOGIN
rpc_command = ["rpcclient", "-U", f"'{user}'", ip]
print(f"Trying out RPC with command: 'rpcclient -U '{user}' {ip}'")

rpc_login = pexpect.spawn(" ".join(rpc_command))

try:
    # Expect the "Password for" prompt and send the password
    rpc_login.expect("Password for", timeout=15)
    rpc_login.sendline(password)

    # Expect the rpcclient prompt and print a success message
    if rpc_login.expect(["rpcclient \$>", pexpect.EOF, pexpect.TIMEOUT], timeout=15) == 0:
        print("Successfully logged in! RPC client prompt detected.")
    else:
        print("RPC client prompt not detected. Something went wrong.")

except pexpect.exceptions.TIMEOUT:
    print("Timeout occurred. RPC client not running or connection issue.")
except pexpect.EOF:
    print("No RPC running. End of file reached.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    rpc_login.close()


# SMBCLIENT
smbclient_command = ["smbclient", "-U", f"'{user}'", "-L", f"\\\\{ip}\\"]
smbclient_login = pexpect.spawn(" ".join(smbclient_command))

print(f"Trying out SMB with command: 'smbclient -U '{user}' -L \\\\{ip}\\'")
try:

    # Expect the "Password for" prompt and send password with 15 seconds to spare
    smbclient_login.expect("Password for", timeout=15)
    smbclient_login.sendline(password)

        #If successfully logged in expect the smb prompt
    if smbclient_login.expect(["Sharename", pexpect.EOF, pexpect.TIMEOUT], timeout=15) == 0:
        print("Successfully logged into SMB using smbclient! Shares detected!")

    elif smbclient_login.expect(["do_connect:", pexpect.EOF, pexpect.TIMEOUT], timeout=15) == 0:
        print("No SMB running")

    else:
        print("Username and password are invalid")
except pexpect.exceptions.EOF:
    print("No SMB running timeout of 15 seconds hit")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    smbclient_login.close()


# SSH
ssh_command = ["ssh", "-q", "-o", "StrictHostKeyChecking=no", f"{user}@{ip}"]
ssh_login = pexpect.spawn(" ".join(ssh_command))

print(f"Trying out SSH with command: 'ssh -q -o StrictHostKeyChecking=no {user}@{ip}")
try:
    # Expect the password prompt and send the password
    ssh_login.expect("password:", timeout=15)
    ssh_login.sendline(password)

    # Expect indication of successful login (checking for user's home directory)
    if ssh_login.expect([f"{user}@{ip}", pexpect.EOF, pexpect.TIMEOUT], timeout=15) == 0:
        print("Credentials are not valid for ssh!")
    else:
        print("SSH Successfully logged in!")

except pexpect.exceptions.TIMEOUT:
    print("Timeout occurred. SSH not running or connection issue.")
except pexpect.EOF:
    print("SSH connection closed unexpectedly.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    ssh_login.close()
