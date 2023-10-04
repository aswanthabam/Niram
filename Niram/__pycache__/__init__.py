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
        if colour not in self.colours.keys():
            raise Exception(self.colours[176]+"Wrong Colour code\nPlease Execute: python3 -m Colours -colour"+self.normal)
        return cc+self.colours[colour]+text+self.normal
    def print(self,text,colour,seperator=" ",end="\n"):
        if type(text) == list and type(colour) == list and len(text) == len(colour):
            self.printFormatted(text,colour,seperator,end)
        else:sys.stdout.write(self.colour(colour,text)+end)

    def format(self,text,colours,seperator=" ",end="\n"):
        if not type(text) == list:raise ValueError("First argument expected to be a list of string")
        if not type(colours) == list:raise ValueError("Second argument colours expected to be a list of integers representing colour")
        if len(text) != len(colours):raise ValueError("Expected colours for all texts")
        res = ""
        i = 0
        for t in text:
            if i != len(text) - 1:
                res += self.colour(colours[i],t) + seperator
            else:res += self.colour(colours[i],t) + end
            i+= 1
        return res
    def printFormatted(self,text,colours,seperator=" ",end="\n"):
        sys.stdout.write(self.format(text,colours,seperator,end))
if __name__ == "__main__":
    obj = Colours()
    l = sys.argv[1:]
    if len(l)<1:print(obj.colour(17,"Enter -h or --help to get more info\nEnter -c or --colours to list colours and Responsible number"))
    
    try:
        opts, args = getopt.getopt(l,"ch")
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