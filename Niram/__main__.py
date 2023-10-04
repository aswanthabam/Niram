import sys ,getopt
from .__init__ import Colours
if __name__ == "__main__":
    l = sys.argv[1:]
    obj = Colours()
    if len(l)<1:print(obj.colour(17,"Enter -h or --help to get more info\nEnter -c or --colours to list colours and Responsible number"))
    
    try:
        opts, args = getopt.getopt(l,"ch",['help','colours'])
    except getopt.GetoptError:
        print(obj.colour(17,"Enter -h or --help to get more info\nEnter -c or --colours to list colours and Responsible number"))
        sys.exit(2)
    for opt,arg in opts:
        
        if opt in ("-c","--colours",):
            obj.colours_help()
        if opt in ("-h","--help"):
            obj.__print_help__()