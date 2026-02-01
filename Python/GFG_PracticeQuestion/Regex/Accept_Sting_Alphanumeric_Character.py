import re


regex = '[a-zA-Z0-9]$'

def check(string):
    if(re.search(regex,string)):
        print("Accept")
    else:
        print("Not Accept")



if __name__ == '__main__':
    string = "ankiraio"
    check(string)
    stirgn = "ankitrai326"
    check(string)
    strnig = "greekforgreeks"
    check(string)