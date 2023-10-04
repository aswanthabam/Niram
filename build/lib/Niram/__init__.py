import sys, getopt,platform, os

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
    def __print_help__(self):
        terminal_width = os.get_terminal_size().columns
        text = " #     #  ###  ######      #     #     # "
        left_padding = (terminal_width - len(text)) // 2 
        p = '-' * left_padding
        self.print('-'*(((terminal_width - len(text)) // 2 )*2+len(text)),23)
        self.print('-'*(((terminal_width - len(text)) // 2 )*2+len(text)),23)
        self.print([p,"                                         ",p],[23,187,23],seperator="")
        self.print([p," #     #  ###  ######      #     #     # ",p],[23,187,23],seperator="")
        self.print([p," ##    #   #   #     #    # #    ##   ## ",p],[23,115,23],seperator="")
        self.print([p," # #   #   #   #     #   #   #   # # # # ",p],[23,67,23],seperator="")
        self.print([p," #  #  #   #   ######   #     #  #  #  # ",p],[23,56,23],seperator="")
        self.print([p," #   # #   #   #   #    #######  #     # ",p],[23,19,23],seperator="")
        self.print([p," #    ##   #   #    #   #     #  #     # ",p],[23,218,23],seperator="")
        self.print([p," #     #  ###  #     #  #     #  #     # ",p],[23,25,23],seperator="")
        self.print([p,"                                         ",p],[23,187,23],seperator="")

        txt1 = " Developed By "
        txt1 += '-' * ((left_padding - len(txt1)) //2)
        pad1 = terminal_width - len(txt1) - 1
        txt1 = '-' * pad1 + txt1
        txt2 = " Aswanth V C "
        txt2 += '-' * ((left_padding - len(txt2)) //2)
        pad2 = terminal_width - len(txt2) - 1
        txt2 = '-' * pad2 + txt2
        self.print(txt1,23)
        self.print(txt2,23)
        self.print('-'*(((terminal_width - len(text)) // 2 )*2+len(text)),23)
        # Print help
        print(f'''
{self.colour(233,"Usage :-")}  {self.format(["$"," python3","-m","Niram","<options>"],[98,30,33,21,33],end="")}
{self.colour(23,"-----------")}
    {self.colour(226,"Options: ")}
            {self.format(["-h",",","--help",": ","For help"],[113,23,113,23,233],end="",seperator="")}
            {self.format(["-c",",","--colours",": ","for listing all colours and the responsible number used in your code"],[113,23,113,23,233],end="",seperator="")}
{self.colour(233,"Example :-")}
{self.colour(23,"-----------")}
    {self.format(["form","Niram","import","Colours","# import Colours module"],[144,200,144,200,23],end="")}
    {self.format(["obj.","print","(",'"Your_text"',",","110",")"," # Print coloured text"],[23,200,23,130,23,224,23,23],seperator="")}
    
{self.format(["----","For more example and usage checkout :","https://github.com/aswanthabam/Niram"],[286,23,54],end="")}
                    ''')
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
            obj.__print_help__()