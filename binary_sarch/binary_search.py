def binary_search(list, element):
    middle=0
    start=0
    end=len(list)
    steps=0
    while start<=end:
        print("Step",steps, ":", list[start:end+1], "with middle element", list[middle], "and start and end", start, end)
        middle=(start+end)//2
        if list[middle]==element:
            return middle
        elif list[middle]>element:
            end=middle-1
        else:
            start=middle+1
        steps+=1
    return -1

list=[1,2,3,4,5,6,7,8,9,10]
target=5
binary_search(list, target)