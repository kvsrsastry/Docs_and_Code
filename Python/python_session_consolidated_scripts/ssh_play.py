import paramiko
import getpass
import sys

hostname='bng-lnx-shell3.juniper.net'
username='kvsr'
password=getpass.getpass('Enter password: ')
port=22
command = sys.argv[1]

try:

 client = paramiko.SSHClient()
 client.set_missing_host_key_policy(paramiko.WarningPolicy())

 client.connect(username=username,hostname=hostname,password=password,port=port)
 stdin, stdout, stderr = client.exec_command(command)

 print(stdout.read().decode('ascii'), end='')

except Exception as e:
 print(e)

else:
 client.close()

