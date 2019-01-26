def isnumber(text):
    if len(text) >= 10: #or len(str(text)) >= 10:
        i=0
        for i in range(0,len(text)):
            if text[i].isdecimal() or text[i] == '+' or text[i] == '-' or text[i] == ' ' :
                print("this is number")
                return True
            else:
                print("this is not phone number")
                return False
    else:
        print("some numbers is missing")
        return False
     
print(isnumber("+91 8500-871798"))
isnumber("850-087-1798")
isnumber("8500871798")
isnumber("+918500871798")
isnumber("prasanna10")
#isnumber(8500871798)