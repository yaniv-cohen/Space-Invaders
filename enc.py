#tgqh 2n lgnmvb jfehlmkt mopp
str = "tgqh 2n lgnmvb jfehlmkt mopp"
output =""
for num in range(26):
    output=""
    for  i,char in enumerate("tgqh 2n lgnmvb jfehlmkt mopp"):
        output +=  chr((ord(char.upper())+num - 65) % 26 + 65)
    print (output)