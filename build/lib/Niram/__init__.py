import sys, getopt,platform

class Colours:
    normal = u"\u001b[0m"
    
    def __init__(self):
        g = []
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                ll = u"\u001b[38;5;" + code + "m"
                g.append(ll)
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                ll = u"\u001b[48;5;" + code + "m"
            g.append(ll)
        self.all_colours = g
        dict1 = {}
        for x in self.all_colours:
            i+=1
            dict1[i] = x
        self.colours = dict1
        ms = {
            "green":dict1[62],
            "red":dict1[212],
            "pink":dict1[180],
            "white":dict1[31]
        }
        if platform.system() == "Windows":
            for x in self.colours.items():
                self.colours[x] = ""
            self.normal = ""
    def colours_help(self):
        dict1 = {}
        print("--------------------------------\nUse The Responsible Number:-\n--------------------------------")
        for i,x in self.colours.items():
            dict1[i] = x
            sys.stdout.write(x+str(i).ljust(4)+self.normal)
        sys.stdout.write(self.normal+"\n")
    def colour(self,colour,text,**kwargs):
        cc = ""
        for key,value in kwargs.items():
            if key == "second":cc = self.colours[value].replace(" ","")
            else:continue
        if colour > max([x for x,y in self.colours.items()]) or colour < 1:
            raise Exception(self.colours[176]+"Wrong Colour code\nPlease Execute: python3 -m Colours -colour"+self.normal)
        
        return cc+self.colours[colour]+text+self.normal

if __name__ == "__main__":
    l = sys.argv[1:]
    if len(l)<1:print(Colours().colour(17,"Enter -h or --help to get more info\nEnter -c or --colours to list colours and Responsible number"))
    
    try:
        opts, args = getopt.getopt(l,"ch")
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