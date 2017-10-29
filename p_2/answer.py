#--code-utf8--

max = 4000000


def countNext(a,b):
    return a+b

def do_main():
    a = 1
    b = 2

    next = b
    next_1 = a
    sum  = 0
    while next <= max:
        if next%2 == 0 :
            sum+= next
        # print "%d \t %d \t %d"%(next_1,next,sum)
        next_new = countNext(next_1,next)
        next_1 = next
        next = next_new

    print sum

if __name__ == '__main__':
    do_main()
