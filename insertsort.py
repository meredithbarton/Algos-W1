def insert_sort(a_list):
    """sorts an array by insertion"""
    for i in range(1, len(a_list)):
        key = a_list[i]
        j = i - 1
        while j >= 0 and a_list[j] > key:
            a_list[j+1] = a_list[j]
            j = j - 1
        a_list[j + 1] = key
    return a_list


with open('data.txt', 'r') as read_data:
    data = read_data.read().splitlines()
    # get lines in proper form for sorting
    for elem in data:
        lst = elem.split(" ")
        sort_this = []
        # leave out first number, since it serves
        # as a description of the data set
        for char in range(1, len(lst)):
            if lst[char] != "":
                # don't add empty spaces to the data set
                sort_this.append(int(lst[char]))
        # sort
        sorted = insert_sort(sort_this)
        # write to file
        dataOut = open('insert.out', 'w')
        dataOut.write(sorted)
        dataOut.close()

