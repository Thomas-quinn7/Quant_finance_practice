cast = ["Joe","John","Ryan"]
print(cast)
print(len(cast))
print(cast[0])
cast.append("Rayna")
print(cast)
cast.pop()
print(cast)
cast.extend(['Roe','pia'])
print(cast)
cast.remove("Roe")
print(cast)
cast.insert(0,'Rayna')
print(cast)


movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
print(movies)

movies1 = ["The Holy Grail",1975, "The Life of Brian",1979, "The Meaning of Life",1983]
print(movies1)

movies2 = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies2)
for item in movies2:
    print(item)

names = ['Harry','Ryan','Joe']

for each_item in movies2:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)

            else: print(nested_item)

    else:
        print(each_item)


"""Function named print_lol used to print list as individual items"""
def print_lol(the_list):
    for each_tem in the_list:
        if isinstance(each_tem, list):
            print_lol(each_tem)

        else:
            print(each_tem)

print_lol(movies)
