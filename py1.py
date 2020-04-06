a_list = [10, 12, 14, 14, 16, 28, 28, 30]


def removeDuplicates():
	result=[]
	for i in a_list:
		if i not in result:
			result.append(i)
	print(result)


def sortList():
    sortedList = sorted(a_list)
    for item in sortedList:
        print(item)


print("Sorting List")
sortList()


print("Removing Dups on a_list...")
print("Clean list is:")
removeDuplicates()
