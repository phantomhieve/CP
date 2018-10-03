from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    size=int(stdin.readline())
    array=list()
    for _ in range(size):
        array.append(list(map(int,stdin.readline().split()))[1:])
    ans1=abs(max(array[0])-min(array[1]))
    ans2=abs(min(array[0])-max(array[1]))
    ans3=abs(min(array[0])-min(array[1]))
    ans4=abs(max(array[0])-max(array[1]))
    stdout.write('%d\n'%(max(ans1,ans2,ans3,ans4)))
