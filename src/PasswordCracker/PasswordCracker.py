'''
Created on Oct 21, 2018

@author: Wah
'''

import crypt

def testCrack(cryptPass):
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt','r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print('[+] Found Password \''+word+'\'\n')
            return
    print('[-] Password not found. \n')
    
def crackSHA512(cryptPass):
    print('[*] This is SHA-512 Hash '+cryptPass)
    
def main():
    passFile = open('PasswordShadow','r')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('[*] Cracking Password For: '+user)
            if (cryptPass[0:3] == '$6$' ):
                crackSHA512(cryptPass)
            else:
                testCrack(cryptPass)

if __name__ == '__main__':
    main()