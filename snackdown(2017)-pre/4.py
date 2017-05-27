def is_between(val, A, B):
    return A <= val  and  val <= B
 
 
def main():
    N = input()
    
    while(N > 0):
        X1, Y1, X2, Y2 = map(int, raw_input().split())
        X3, Y3, X4, Y4 = map(int, raw_input().split())
        found = False
 
        if(Y1 == Y2  and  Y3 == Y4  and  Y1 == Y3):
            if(is_between(X3, min(X1, X2), max(X1, X2))  or  is_between(X4, min(X1, X2), max(X1, X2))  or
            is_between(X1, min(X3, X4), max(X3, X4))  or  is_between(X2, min(X3, X4), max(X3, X4))):
                found = True
            else:
                found = False
 
        elif(X1 == X2  and  X3 == X4  and  X1 == X3):
            if(is_between(Y3, min(Y1, Y2), max(Y1, Y2))  or  is_between(Y4, min(Y1, Y2), max(Y1, Y2))  or
            is_between(Y1, min(Y3, Y4), max(Y3, Y4))  or  is_between(Y2, min(Y3, Y4), max(Y3, Y4))):
                found = True
            else:
                found = False
       
        else:
            if((X1 == X3  and  Y1 == Y3)  or  (X1 == X4  and  Y1 == Y4)  or
            (X2 == X3  and  Y2 == Y3)  or  (X2 == X4  and  Y2 == Y4)):
                found = True
 
        print "yes" if(found) else "no"
        N -= 1
