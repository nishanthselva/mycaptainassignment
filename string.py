most_frequent=input("please enter a string:")
list=[]
for i in most_frequent:
    if i not in list:
        list.append(i)
        print(i,"=",most_frequent.count(i))