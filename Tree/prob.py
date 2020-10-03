# x=0
# var=1
# l1=[i for i in range(1,6)]
# l2=[i for i in range(5,0,-1)]

# while i<5:
#     for i in l1:
#         print(i,end=' ')
#     for i in l2:
#         print(i,end=' ')
#     i+=1
# for i in l1:
#     print(i,end=' ')
# for i in l2:
#     print(i,end=' ')
# print("\n")
# while x<5:
#     print("|")
#     i+=1

num = int(input("Enter num: "))
for i in range(1, num+1):
    for j in range(i, num + 1):
        print(j, end="")
    print((i-1)* 2 *" ", end="")
    for k in range(num - i + 1, 0, -1):
        print(k, end="")
    print("")
