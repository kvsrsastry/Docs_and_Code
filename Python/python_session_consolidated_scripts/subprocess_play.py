# Subprocess
import subprocess
import shlex
import sys

try:
    cmd = sys.argv[1]
    cp_obj = subprocess.run(shlex.split(cmd), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(cp_obj.stdout.decode('ascii'), end = '')
except Exception as e:
    print(e)

