# ArgParse
import argparse

args = argparse.ArgumentParser(description='sample script with argparse', prog='args_play')
args.add_argument('--one', type=int)
args.add_argument('--two', '-e', type=int, required=True)
args.add_argument('--three', type=int, choices=range(10))
args.add_argument('--four', type=int, nargs='?', default=23, const=42)
args.add_argument('-five', type=int, default=23)
args.add_argument('--six', type=int, default=argparse.SUPPRESS)
args.add_argument('--seven', type=int, nargs=1, default=23)
args.add_argument('--eight', type=int, nargs='*', default=23)
args.add_argument('--nine', type=int, nargs='+')
args.add_argument('ten', type=int)
args.add_argument('eleven', type=int, nargs='+')
args.add_argument('--version', action='version', version='%(prog)s 1.0')

print(vars(args.parse_args()))

class arg():
    pass

ar = arg()
args.parse_args(namespace=ar)
print(ar.ten)
