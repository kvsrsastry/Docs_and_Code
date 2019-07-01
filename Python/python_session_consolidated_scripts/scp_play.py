# SCP
import paramiko
import getpass

hostname = 'bng-lnx-shell3'
username = 'kvsr'
password = getpass.getpass('Enter Password: ')
port = 22
dest = '/homes/kvsr/python/consolidated/ssh_play.py'
src = '/homes/kvsr/ssh_played.py'

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username,password=password)
    client = paramiko.SFTPClient.from_transport(t)
    #client.put(src, dest)
    client.get(src, dest)
except Exception as e:
    print(e)
else:
    t.close()
    client.close()
