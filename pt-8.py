import os

def soldier(str, file, type):
    os.chdir(str)
    a = os.listdir()
    i = 1
    with open(file, "r") as f:
        filelist = f.read().split("\n")
    for file in a:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == type:
            os.rename(file, f"{i}{type}")
            i += 1
            

if __name__ == '__main__':
    path = input("Enter your folder's path: \n")
    file = input("Enter the name of txt file: \n")
    type = input("Enter a type that we cant change: \n")
    soldier(path, file, type)
