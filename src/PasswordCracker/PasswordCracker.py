'''
Created on Oct 21, 2018

@author: Wah
'''

import crypt

def test(cryptPass):
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt','r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print('[+] Found Password '+word+'\n')
            return
    print('[-] Password not found. \n')
    
def main():
    passFile = open('passwd','r')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('[+] Cracking Password For: '+user)
            test(cryptPass)

if __name__ == '__main__':
    main()