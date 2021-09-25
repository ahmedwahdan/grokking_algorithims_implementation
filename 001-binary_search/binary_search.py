

def binary_search(list, item):
    # calculate the initial index value of low and high of list
    iterations = 0
    low = 0
    high = len(list) - 1
    # loop over the list as long as low <= high, so if low moves right or
    # high moves left, we are sure we are in boundary with this condition
    while(low <= high):
        iterations += 1
        # calculate mid index and get the value of in the list (guess value)
        mid = int((low + high) / 2)
        #print(mid)
        guess = list[mid]
        #print(guess)
        # if the guess value equal the search item, retun mid index
        # else if the seach value > guess value, set low to (mid + 1)
        # else if the seach value < guess value, set high to (mid - 1)
        if(guess == item):
            print(iterations)
            return mid
        elif (item > guess):
            low = mid + 1
        else:
            high = mid - 1
    print(iterations)    
    return None






my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 0))
      
