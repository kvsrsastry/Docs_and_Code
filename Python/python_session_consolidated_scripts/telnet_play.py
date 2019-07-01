# Telnet
import telnetlib

host = 'r0d'
tel = telnetlib.Telnet(host=host)
#tel.set_debuglevel(100)

tel.read_until(b'login: ')
tel.write('regress'.encode('ascii') + b'\n')
tel.read_until(b'Password:')
tel.write('MaRtInI'.encode('ascii') + b'\n')

tel.read_until(b'% ')
tel.write('cli'.encode('ascii') + b'\n')

tel.read_until(b'regress@r0d> ')
tel.write('show chassis hardware | no-more'.encode('ascii') + b'\n')
out = tel.read_until(b'regress@r0d> ')
tel.write('exit'.encode('ascii') + b'\n')
tel.read_until(b'% ')
tel.write('exit'.encode('ascii') + b'\n')
tel.close()

print(out.decode('ascii'), end='')
