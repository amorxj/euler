#--code-utf8--



def isMuilt(x,l):
    for v in l:
        if x%v == 0:
            return True
    return False

def count(r,mlist):
    sum = 0
    if r <0:
        return 0
    for x  in range(0,r):
        if isMuilt(x,mlist):
            sum+=x
    return sum

print count(1000,[3,5])
