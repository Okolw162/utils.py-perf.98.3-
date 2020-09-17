#
# This code can hide all characters in your password/login etc but the last 4 characters
# 
# import os - not obligatory. delete line 8 and 11 to work without this module.
#
# example: 
# == | 1. The user enters data (qwerty123)
# == | 2. code print: #####y123
#

import os

cc = input('enter login/password or data\n(if data < 5 characters - error!!!')
os.system('clear')

def maskify(cc):
    #print(len(cc))
    if int(len(cc)) > 4:
        x = len(str(cc)[:-4])
        z = '*' * int(x)
        v = str(cc)[x:]
        return f'{z}{v}'
    else:
        return cc

print(f'Our data: {maskify(cc)}')
