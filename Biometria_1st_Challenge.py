
from random import sample as Generate


n1 = input("Type first Number of the set:")

n2 = input("Type second Number of the set:")

num = input("Type how many distint numbers do you want:")
        

print(Generate(range(int(n1), int(n2) + int(1)),int(num)))


