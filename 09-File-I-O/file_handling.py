# f = open("file.txt","r")          # OPEN FOR READING
# data = f.read()
# print(data)                 # file.text me jo bhi likha hai wo yaha dekhi ga
# f.close()


# st = " Hey hitler you are amazing"
# f = open("myfile.txt","w")        #OPEN FOR WRITING

# f.write(st)

# f.close()



# f = open("myfile.txt")

# # line = f.readlines()
# #print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))         # READING OR WRITING MEANING LINES

# line4 = f.readline()
# print(line4, type(line4))

# f.close()

# f = open("myfile.txt")

# line = f.readline()
# while(line !=" "):
#     print(line)
#     line = f.readling()
# f.close()






# st = " Hey hitler you are amazing"
# f = open("myfile.text","a")        #OPEN FOR APPENDING MEANS ADDING

# f.write(st)

# f.close()


f = open("file.txt")
print(f.read())
f.close()

#the same can be written using statement like  this
 
with open("file.txt") as f:
    print(f.read())

    #  you dont have to explictitly close the file