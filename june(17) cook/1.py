for _ in range(input()):
    array=raw_input()
    up,down=0,0
    array+='.'
    for i in xrange(len(array)-1):
        if(array[i]!=array[i+1]):
            if(array[i]=="U"):
                up+=1
            else:
                down+=1
    print min(up,down)
