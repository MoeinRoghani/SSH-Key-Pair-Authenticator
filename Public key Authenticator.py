# CopyRight hold by © Moein Roghani 

import subprocess, paramiko
from getpass import getpass


host = "Host IP Address"
username = "Host Username"

#---------------------------------------Generating public and private pairs on current machine---------------------------------------
destination_path = ":Desktop" + '\\' + "id_rsa.pub %USERPROFILE%" + '\\' + ".ssh"

command = "ssh-keygen"
subprocess.Popen(command, shell=True, stderr=subprocess.PIPE).communicate()

exc = "scp %USERPROFILE%" + '\\' + ".ssh" + '\\' +"id_rsa.pub  " + username+'@'+host + destination_path
subprocess.Popen(exc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

user = input("Public and Private key pairs generated successfully\nPress Enter to Proceed...")


#---------------------------------------Adding public key to authorized keys on server machine---------------------------------------
password = getpass("Enter the host password: ")
command = "type " + "%USERPROFILE%" + '\\' + ".ssh"  + '\\' + "id_rsa.pub >> " + "%USERPROFILE%" + '\\' + ".ssh"  + '\\' + "authorized_keys"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()

user = input("Public key successfully stored on the host\nPress Enter to exit...")
