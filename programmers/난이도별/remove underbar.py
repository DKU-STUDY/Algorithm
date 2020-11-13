
import os, re
path = os.getcwd()

for i in os.listdir(os.getcwd()):
    print(i)
    ori = i
    i = i.replace('_', ' ')
    print(i)
    print(path+'/'+ori, path+'/'+i)
    os.rename(path+'/'+ori, path+'/'+i)

