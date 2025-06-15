import sys

def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
    for each_tem in the_list:
        if isinstance(each_tem, list):
            print_lol(each_tem,indent,level+1,fh)

        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="",file=fh)
            print(each_tem,file=fh)

help(print_lol)