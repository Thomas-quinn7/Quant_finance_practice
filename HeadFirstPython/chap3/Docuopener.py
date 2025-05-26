import os
from nester import print_lol

man=[]
other=[]

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_said)=each_line.split(':',1)
            line_said=line_said.strip()
            if role =='Man':
                man.append(line_said)
            elif role =='Other Man':
                other.append(line_said)
        except ValueError:
            pass
    data.close()
except IOError:
    print("File not foun")
try:
    f1 = open('test1.txt','w')
    f2 = open('test2.txt','w')
    print(man,file=f1)
    print(other,file=f2)

except IOError:
    print("File not found")
finally:
    f1.close()
    f2.close()


print_lol(man)