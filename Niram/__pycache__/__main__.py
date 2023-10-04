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
            print(f'''
{obj.colour(233,"Usage :-")}  {obj.format(["$"," python3","-m","Niram","<options>"],[98,30,33,21,33],end="")}
{obj.colour(32,"-----------")}
    {obj.colour(226,"Options: ")}
            {obj.format(["-h",",","--help",": ","For help"],[113,32,113,32,163],end="",seperator="")}
            {obj.format(["-c",",","--colours",": ","for listing all colours and the responsible number used in your code"],[113,32,113,32,163],end="",seperator="")}
{obj.colour(233,"Example :-")}
{obj.colour(32,"-----------")}
    {obj.format(["form","Niram","import","Colours","# import Colours module"],[144,200,144,200,32],end="")}
    {obj.format(["obj.","print","(",'"Your_text"',",","110",")"," # Print coloured text"],[23,200,23,130,23,224,23,32],seperator="")}
    
{obj.format(["----","For more example and usage checkout :","https://github.com/aswanthabam/Niram"],[286,32,54],end="")}
            ''')