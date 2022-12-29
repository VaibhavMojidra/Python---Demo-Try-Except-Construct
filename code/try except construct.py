#Try-Except Construct

try:
    n1=int(input('Enter number 1: '))
    n2=int(input('Enter number 2: '))
    print("{}/{} = {}".format(n1,n2,(n1/n2)))
except:
    print("{} cannot be divide by {}".format(n1,n2))
