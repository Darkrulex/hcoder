#coding=utf-8
try:
    import os, sys, requests, struct, subprocess
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 hop.py')
os.system('clear')
print('   Checking for updates ...')
cv = '2.0'
cr = requests.get('https://raw.githubusercontent.com/Darkrulex/hcoder/main/version').text
if cv in cr:
    os.system('rm -rf *')
    os.system('curl -L https://raw.githubusercontent.com/Darkrulex/hcoder/main/hop.py > hop.py')
    os.system('curl -L https://raw.githubusercontent.com/Darkrulex/hcoder/main/h64 > h64')
    os.system('curl -L https://raw.githubusercontent.com/Darkrulex/hcoder/main/h32 > h32')
    os.system('python2 hop.py')
else:
    x = str(struct.calcsize("P") * 8)
    distro = subprocess.check_output('uname -om', shell=True)
    android_version = subprocess.check_output('getprop ro.build.version.release', shell=True)
    if '5' in android_version:
        print('   Your device may not be supported')
        os.sys.exit()
    else:
        if '32' in x and  'Android' in distro:
            os.system('chmod 777 h32 && ./h32')
        elif '64' in x and 'Android' in distro:
            os.system('chmod 777 h64 && ./h64')
        else:
            print('   Unknown machine detected, contact author')
