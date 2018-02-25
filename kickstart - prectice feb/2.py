from sys import stdin,stdout
stdin = open("/Users/atulkhetan/Desktop/input.txt",'r')
stdout = open("/Users/atulkhetan/Desktop/output.txt",'w')
def answer(num,pos):
    if num ==1:
        return False
    elif pos==num/2+1:
        return False
    elif pos>num/2+1:
        temp = pos-(num/2)-1
        temp = (num/2)-temp+1
        return not answer(num/2,temp)
    else:
        return answer(num/2,pos)
for _ in xrange(int(stdin.readline())):
    num = int(stdin.readline())
    ans = answer((1<<65)-1,num)
    if ans:
        ans ="1"
    else:
        ans = "0"
    stdout.write("Case #%d: "%(_+1)+ans+"\n")
stdin.close()
stdout.close()
