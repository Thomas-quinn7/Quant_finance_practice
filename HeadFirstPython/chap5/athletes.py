
def sanitize(time_spring):
    if '-' in time_spring:
        splitter = ('-')

    elif ':' in time_spring:
        splitter = (':')

    else:
        return(time_spring)
    (mins, secs) = time_spring.split(splitter)
    return(mins+'.'+secs)

def opener(filename):
    try:
        with open(filename) as file:
            data=file.read()
            sarah=data.sprit.split(',')
        return sarah
    except IOError as error:
        print('File not found'+ str(error))
        return None

sarah=opener('sarah.txt')
print(sarah)