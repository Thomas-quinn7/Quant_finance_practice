def sanitizer(time_strings):
    if '-' in time_strings:
        splitter = '-'
    elif ':' in time_strings:
        splitter = ':'
    else:
        return(time_strings)
    (mins,secs) = time_strings.split(splitter)
    return(mins+'.'+secs)

def coach_file(filename):
    try:
        with open(filename,'r') as file:
            data = file.readline()
            f = data.strip().split(',')
            file_dict={}
            file_dict['name'] = f.pop(0)
            file_dict['DOB'] = f.pop(0)
            file_dict['times']=f
            print(file_dict['name']+"'s fastest times"+ str(sorted(set([sanitizer(t) for t in file_dict['times']]))[0:3]))
        return(file_dict)

    except IOError as e:
        print("file not found"+str(e))
        return(None)


