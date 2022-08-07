nums = [23,18,28,17,-18,-17,-23,-28]
print("original numbers in thre list :",nums)
new_nums = list(filter(lambda x:x>0,nums))
print (" positive numbers in the list:",new_nums)