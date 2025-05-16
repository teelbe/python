def simon_say(list1, list2):
    #check if second list is the first list shifted to the right
    return list1[:-1] == list2[1:]
print(simon_say([1,2],[5,1]))
print("----    ----    ----    ----")
print(simon_say([1,2],[5,5]))
print("----    ----    ----    ----")
print(simon_say([1,2,3,4,5],[0,1,2,3,4]))
print("----    ----    ----    ----")
print(simon_say([1,2,3,4,5],[5,5,1,2,3]))
