# SMTP
import smtplib
import base64

sender = 'kvsr@juniper.net'
recv = 'kvsr@juniper.net'
filename = '/homes/kvsr/python/consolidated/ssh_play.py'

filecontent = ''
with open(filename) as fh:
 filecontent = filecontent + fh.read()

marker = 'AUNIQUEMARKER'

part1 = '''From: kvsr@juniper.net
To: kvsr@juniper.net
Subject: omgamganapathayenamaha
MIME-Version: 1.0
Content-type: multipart/mixed; boundary=%s

--%s
''' % (marker, marker)

part2 = '''Content-type: text/plain
Content-Transfer-Encoding:8bit

Ganesh is the pratham pujya
--%s
'''% (marker)

part3 = '''
Content-type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
'''% (filename, filename, filecontent, marker)

message = part1 + part2 + part3

try:
    client = smtplib.SMTP('localhost')
    client.sendmail(sender, recv, message)
    print('Successfully sent the E-Mail !!!')

except Exception as e:
    print('Not able to send the E-Mail !!!')
    print(e)
