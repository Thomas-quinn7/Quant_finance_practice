import chap6code

class Athlete:
    def __init__(self,a_name,a_DOB=None,a_times=[]):
        self.name = a_name
        self.DOB = a_DOB
        self.times = a_times
    def top3(self):
        return(sorted(set([chap6code.sanitizer(t) for t in self.times]))[0:3])
    def add_times(self,time):
        self.times.extend(time)

def coach(filename):
    try:
        with open(filename,'r') as file:
            data = file.readline()
        temp = data.strip().split(',')
        return(Athlete(temp.pop(0),temp.pop(0),temp))
    except IOError as e:
        print("File not found"+str(e))
        return(None)

james = coach('james2.txt')
print(james.name+"'s fastest times"+str(james.top3()))

newtimes=['1.44','3.22','3.69']
james = coach('james2.txt')
james.add_times(newtimes)
print(james.times)
print(james.name+"'s fastest times"+str(james.top3()))

