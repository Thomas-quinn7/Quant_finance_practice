from HeadFirstPython.chap6.chap6code import sanitizer
import pickle

class Athlete:
    def __init__(self,a_name,a_DOB=None,a_times=[]):
        self.name = a_name
        self.DOB = a_DOB
        self = a_times
    def top3(self):
        return sorted(set([sanitizer(t) for t in self]))[0:3]


def coach(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readline()
        temp = data.strip().split(',')
        return (Athlete(temp.pop(0), temp.pop(0), temp))
    except IOError as e:
        print("File not found" + str(e))
        return None

class AthleteList:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.DOB = a_dob
        self.extend(a_times)
    def top3(self):
        return str(sorted(set([sanitizer(t) for t in self]))[0:3])

def put_to_store(file_list):
    all_athletes={}
    for file in file_list:
        ath = coach(file)
        all_athletes[ath.name] = ath
    try:
        with open('AthleteList.pickle', 'wb') as handle:
            pickle.dump(all_athletes,handle)
    except IOError as e:
        print("File not found" + str(e))
    return all_athletes

def get_from_store(file_list):
    all_athletes={}
    try:
        with open('AthleteList.pickle', 'rb') as handle:
            all_athletes = pickle.load(handle)
    except IOError as e:
        print("File not found" + str(e))
    return all_athletes

the_files = ["james2.txt","julie2.txt","mikey2.txt","sarah2.txt"]

def names_from_storage():
    athletes = get_from_store()
    response = [athletes[t].name for t in athletes]
    return response