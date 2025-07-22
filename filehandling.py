#operations -> read, write, append, delete
#file -> read -> r mode = existing file
#file -> write -> w mode = create new file
#file -> append -> a mode = create new file
#file -> delete -> import os -> os.remove("filename")-> existing file

#mode ="r", "w", "a", "r+", "w+", "a+" -> fs.seek(0)
#delete => OS -> remove
#syntax ->2 with, without

fs1 =open("file/read.txt",mode="r")
readtext = fs1.read()
print(readtext)
#fs1.close()

fs2 =open("file/write.txt",mode="w")
fs2.write("Hello My name is Ayush Himalaya Shrestha")
fs2.close()

fs3 =open("file/write.txt",mode="w+")
fs3.write("Hello World!")
fs3.seek(0)
readdata = fs3.read()
print(readdata)

fs4 =open("file/append.txt", mode="a")
fs4.write(fs1.read())
fs4.close()

# with mode -> with open("filename" , mode ="r") as fs1:
#      readdata =fs1.read()
#      print(readdata)

with open("file/append.txt", mode="r") as fs6:
    readdatas= fs6.read()
    print(readdata)
    fs6.close()

# WAP to print the table from 0 to 10 using for loop and file handling make seprate file for this task



#for i in range(1,11):
 #   with open("file/{i}.txt",mode="w") as fs:
  #   for j in range (1,11):
   #     fs.write(f"{i}*{j}={i*j}\n")

for i in range(0,11):
    with open(f"file/table{i}.txt", mode = "w") as fs7:
        for j in range(1,11):
            fs7.write(f"{i} * {j} = {i*j}\n")
        fs7.close()#

