import os
import sys
infi = open("ans.txt","w",encoding="utf-8")
infi.close()
path=sys.path[0]
paths=""
FileNames = os.listdir(path+"\\data")
for i in FileNames:
    paths+=(path+"\\data\\"+i+" ")
os.system(".\sim_c++.exe -p "+paths+">> ans.txt")
infi = open("ans.txt","r",encoding="utf-8")
infi2=infi.read()
infi2.replace(path+"\\data\\","")
print(infi2.replace(path+"\\data\\",""))
infi.close()
os.system("del ans.txt")
print("---------------------------")
print("输入回车键关闭")
a=input()