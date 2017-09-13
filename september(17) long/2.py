from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    num = int(stdin.readline())
    array= range(1,(num+1))
    for i in range(0,num-(int(num%2!=0)),2):
        array[i],array[i+1]=array[i+1],array[i]
    if(num%2!=0):
        array[-1],array[-2]=array[-2],array[-1]
    for i in range(num):
        stdout.write(str(array[i])+" ")
    stdout.write("\n")
        
