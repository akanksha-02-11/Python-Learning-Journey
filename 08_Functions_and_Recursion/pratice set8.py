# def greatest(a,b,c):
#     if(a>b and a>c):                 #PROBLEM NO 1
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c


# a =1
# b =5
# c =9

# print(greatest(a,b,c))





# def f_to_c(f):                       #PROBLEM NO 2
#     return 5*(f-32)/9

# f = int(input("Enter temperature in F: "))
# c = f_to_c(f)
# print(F"{round(c,2)}degree c")



# print("a")                    #PROBLEM NO 3
# print("b")
# print("c", end="")
# print("d", end="")



# def sum(n):                    #PROBLEM NO 4
#     if(n==1):
#         return 1
#     return sum(n-1) + n
# print(sum(6))



# def pattern(n):                   #PROBLEM NO5
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(3)




# def inch_to_cm(inch):                   #PROBLEM NO 6
#     return inch * 2.54
# n = int(input("Enter value in inches: "))

# print(f"the corresponding value in cms is {inch_to_cm(n)}")




# def rem(l, word):                       #PROBLEM NO 7
#     n = []

#     for item in l:
#         l.remove(word)
#         return l

# l = ["hitler","saksham","akanksha","an"]

# print(rem(l,"an"))


# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#         return n

# l = ["hitler","saksham","akanksha","an"]

# print(rem(l,"an"))


# def multiply(n):                        #PROBLEM NO 8
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")

# multiply(5)