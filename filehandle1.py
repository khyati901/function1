myobject=open("myfile123.txt",'a')
print("file created if not exist")
print("*************************")
myobject.seek(5)
print(myobject.tell())
myobject.close()

