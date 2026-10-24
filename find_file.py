#!/usr/bin/python3

import sys, os

def main():
    path=sys.argv

    check_argv_result=check_argv(path) #this func returns 1 if it is just one argument value, the argv_result if it receives a valid dir path and False if it does not

    if check_argv_result == 1:
        print("No other argument is provided")
        sys.exit(1)
    
    if check_argv_result == 2:
        print("More than the required argument passed")
        sys.exit(2)

    #handles the files in the dir
    run_files(check_argv_result)

def check_argv(argvs):
    if len(argvs) == 1: return 1
    if len(argvs) != 2: return 2 #if argvs passed is more than the required number 

    path=argvs[1]
    is_dir=os.path.isdir(path)
    return False if not is_dir else path


def run_files(path):
    path_content=os.listdir(path)

    py_files=[]
    for file in path_content:
        file_path=os.path.join(path,file) #filepath saved to var so it can be used to test

        if os.path.isfile(file_path) and file.endswith(".py"):
            py_files.append(file)
     
    if not py_files:
        print(f"no python file exist in {path} {py_files}")
    else:
        print(f"The python files that exist are {py_files}")


if __name__=="__main__":
    main()
