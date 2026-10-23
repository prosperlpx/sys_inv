#!/usr/bin/python3

import os, sys

def main():
    #check the argv passed before running other code block
    if not check_argv():
        print("Provide a path argument")
        sys.exit(1)

    path=sys.argv[1]
    if not os.path.isdir(path):
        print("path specified is not valid")
        sys.exit(2) #2 exit code means path is invalid

    files = os.listdir(path)
    counter=0

    for file in files:
        file_path=os.path.join(path, file)
        if file.endswith(".py") and os.path.isfile(file_path):
            counter+=1
    
    print(f"Number of python file is {counter}")

def check_argv():
    return len(sys.argv) == 2 


if __name__=="__main__":
    main()

   
