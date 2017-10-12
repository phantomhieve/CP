for _ in range(input()):
    size=input()
    string=raw_input()
    one=0
    for i in range(size):
        if string[i]=='1':
            one+=1
    print (one*(one+1))/2
