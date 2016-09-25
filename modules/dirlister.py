import os

def run(**args):
    
    print "[*] IN dirlister module."
    files = os.listdir(".")
    
    #return str(files)
    return "['somefile.zip', 'Somefolder']"
