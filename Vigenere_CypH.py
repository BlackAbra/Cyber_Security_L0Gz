
alphabet = "abcdefghijklmnopqrstuvwxyz "


index_Letter_column = dict(zip(alphabet,range(len(alphabet))))
index_Letter_row = dict(zip(range(len(alphabet)),alphabet))


def  Encrypt(message, key):
    encrypted = ""
    split_msg = [
        message[i:i + len(key)] for i in range(0,len(message),len(key))
    ]

    for split_steps in split_msg:
        i = 0 
        for letter in split_steps:
            flag = (index_Letter_column[letter] + index_Letter_column[key[i]]) % len(alphabet)
            encrypted += index_Letter_row[flag]
            i += 1


    return encrypted


def Decrypt(cyhpher , key):
    decrypted = ""
    split_encrypted = [
        cyhpher[i : i + len(key)] for i in range(0,len(cyhpher),len(key))
                      ] 
        
    for split_steps in split_encrypted :
        i = 0
        for letter in split_steps :
            flag = (index_Letter_column[letter] - index_Letter_column[key[i]]) % len(alphabet)
            decrypted += index_Letter_row[flag]
            i += 1

    return decrypted


def main():
    plain_massage = "at first these keys were fun"
    key = "matchstick"
    encrypted_txt  = Encrypt(plain_massage,key)
    decrypted_txt  = Decrypt(encrypted_txt,key)

    print("Primal Source : " + plain_massage)
    print("Encrypted Txt :   " + encrypted_txt)
    print("Decrypted Txt : " + decrypted_txt)
   

main()