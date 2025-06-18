f=open("‪D:\\38MCA\\py\\demo.txt","r")
print("the filepointer is at byte:",tell())
content=f.read();
print("After reading, the filepointer is at:",f.tell())
