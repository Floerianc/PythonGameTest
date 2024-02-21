import subprocess
import sys
import time
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyQt5'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pathlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'matplotlib'])
print("\n"*30)
print("   ___ _       _     _              _   ")
print("  / __(_)_ __ (_)___| |__   ___  __| |  ")
print(" / _\ | | '_ \| / __| '_ \ / _ \/ _` |  ")
print("/ /   | | | | | \__ \ | | |  __/ (_| |_ ")
print("\/    |_|_| |_|_|___/_| |_|\___|\__,_(_)")
time.sleep(3)
exec(open('fuck_me.py').read())