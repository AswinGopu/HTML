# open("abc.txt","x")
a=open("abc.txt","w")
a.write("jdhhv dhvdiufvbdf ")
a.close()
a=open("abc.txt","r")
print(a.read(5))
a.close()
a=open("abc.txt","a")
a.write("hello world")
a.close()
a=open("abc.txt","w")
a.write("welcome world")