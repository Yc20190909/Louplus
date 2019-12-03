for num in range(1,101):
    strnum = str(num).find('7')
    if strnum==-1 and num%10!=7:
        print(num)
