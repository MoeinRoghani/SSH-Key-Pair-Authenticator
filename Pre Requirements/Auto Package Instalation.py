# CopyRight hold by © Moein Roghani 

import sys
import subprocess

# Auto installing the required package:

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'paramiko'])


input("Package requirements have been satisfied\nPress Enter to exit...")