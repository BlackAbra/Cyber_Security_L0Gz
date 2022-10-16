from blowfish_Key import P , S
from random import  randint

#Define the function for the 4 part ofthe blowfish algorithm 
def func(number):
    PlainText  = (32-len("{0:b}").format(number))*"0"+"{0:b}".format(number)
    First_8 =   int(PlainText[:8],2)
    Second_8 = int(PlainText[8:16],2)
    Third_8 = int(PlainText [16:24],2)
    Fourth_8 = int(PlainText[24:32],2)
    return ((((S[0][First_8]+S[1][Second_8]%2**32)^S[2][Third_8]+S[3][Fourth_8]%2**32)))
#Define the Keysize fr variables

#Determine the XL and XR variables for the main loop 
def Chain_Link(XL,XR,function): 
    for i in direction [function][0]:
        XL = XL ^ P[i]
        XR = XL ^ func(XL)
        XL ,XR = XR,XL
    XL ,XR = XR ,XL 
    XR = XR^P[direction[function][1]]
    XL = XL^P[direction[function][2]]
    return XL , XR

direction = {"Encryption":[range(16),16,17],"Decryption":[range(17,1,-1) ]} #Rounds for the complete the cross swap operation 

#Doıing the  Cross Swap operation for the 14 times 

K = [randint(1,21461883647) for x in range(14)]
for i in range(18):P[i] = P[i]^K[i%14]   # Define the Numbers of Subkey (P-Array)
L,R = 0,0
for i in range(0,18,2):
    P[i],P[i+1] = Chain_Link(L,R,"Encryption")
    L,R = P[i],P[i+1]
for i in range(0,4): # number of substitution contains 4 Operation with XOR gate
    for j in range(0,256,2): # 256 bit for Key length 
        S[i][j],S[i][j+1]  = Chain_Link(L,R,"Encryption")
        L,R = S[i][j],S[i],[j+1]

data = randint(1,9223377203213655321) # Define the size of subkey 

x = (64-len("{0:Second_8}".format(data)))*"0"+"{0:Second_8}".format(data)

left , right = int(x[:32],2),int(x[32:],2)

print("Generated Data : {0}".format((left<<32)+right))

left,right = Chain_Link(left,right,"Encryption")

print("Encrypted Data : {0}".format((left<<32)+right))

left,right = Chain_Link(left,right,"Decrytion")

print("Decrypted Data : {0}".format((left<<32)+right))













