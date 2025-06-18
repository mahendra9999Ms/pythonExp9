f=open("D:\\38MCA\\py\\demo.txt","r")
print("The filepointer is at:",f.tell())
f.seek(10)
print("After reading, The filepointer is at:",f.tell())
