import chap6code
from HeadFirstPython.chap6.chap6code import sanitizer


class Athlete:
    def __init__(self,a_name,a_DOB=None,a_times=[]):
        self.name = a_name
        self.DOB = a_DOB
        self = a_times
    def top3(self):
        return(sorted(set([chap6code.sanitizer(t) for t in self]))[0:3])


def coach(filename):
    try:
        with open(filename,'r') as file:
            data = file.readline()
        temp = data.strip().split(',')
        return(Athlete(temp.pop(0),temp.pop(0),temp))
    except IOError as e:
        print("File not found"+str(e))
        return(None)


class AthleteList:
    def __init__(self,a_name,a_dob=none,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.DOB = a_dob
        self.extend(a_times)
    def top3(self):
        return(str(sorted(set([sanitizer(t) for t in self]))[0:3]))



