import os as s


# current directory
print(s.getcwd())
#change directory
s.chdir(f"E:\\XPSC Level-1")
print(s.getcwd())

#make a folder, 
directory = "RKTesting"
paths = "E:/XPSC Level-/"
di = s.path.join(paths,directory)
s.makedirs(di, exist_ok=True)
print(s.getcwd())
print(s.listdir())

#macking a file
name = "hellow.py"
paths = "E:/XPSC Level-/"
di = s.path.join(paths,name)
s.makedirs(di)
