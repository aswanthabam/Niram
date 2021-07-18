import sys ,getopt
from .__init__ import Colours
if __name__ == "__main__":
    l = sys.argv[1:]
    if len(l)<1:print(Colours().colour(17,"Enter -h or --help to get more info\nEnter -c or --colours to list colours and Responsible number"))
    
    try:
        opts, args = getopt.getopt(l,"ch",['help','colours'])
    except getopt.GetoptError:
        print(Colours().colour(17,"Enter -h or --help to get more info\nEnter -c or --colours to list colours and Responsible number"))
        sys.exit(2)
    for opt,arg in opts:
        
        if opt in ("-c","--colours",):
            Colours().colours_help()
        if opt in ("-h","--help"):
            print(f'''
{Colours().colour(233,"Usage(1):-")}  {Colours().colour(170,"python3 -m Colours <option>")}
-----------------------------------------
Options:     
            -h,--help:-  for help\n
            -c,--colours:- for listing all colours and the responsible number used in your code
\nUsage(2):-\n
---------------
first import ,
    {Colours().colour(170,"From Niram import Colours")}
change colour,
    {Colours().colour(170,"Colours().colour(<colour code(will get in '-c')>,Your text,second=your second colour or background)")}
    
    This will return the formated text!.
            ''')