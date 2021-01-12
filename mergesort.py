def merge_sort(a_list, left, right):
    """Recursive implementation of merge sort. This method
    will split a_list into its appropriate sub-arrays and
    call merge for each"""
    # if left points to same index, or surpasses right,
    # no need to keep splitting the array
    if left >= right:
        return

    # split array in half, into 2 smaller arrays
    mid = (left + right) // 2
    merge_sort(a_list, left, mid)
    merge_sort(a_list, mid + 1, right)
    merge(a_list, left, right, mid)
    return a_list

def merge(a_list, left, right, mid):
    """function that utilizes the series of arrays in order
    to sort the original array, by methodically merging the smaller
    arrays"""
    L = a_list[left:mid+1]
    R = a_list[mid+1:right+1]

    track_left = 0
    track_right = 0

    sorted_thru = left

    while track_left < len(L) and track_right < len(R):
        # actual sorting occurs -- compare left and right indices
        if L[track_left] <= R[track_right]:
            a_list[sorted_thru] = L[track_left]
            # increment left index tracker
            track_left += 1
        else:
            # right is greater
            a_list[sorted_thru] = R[track_right]
            track_right += 1

        sorted_thru += 1

    # it is possible to have more elements in L or R than the other
    # so this section sorts any remaining elements
    while track_left < len(L):
        a_list[sorted_thru] = L[track_left]
        track_left += 1
        sorted_thru += 1
    while track_right < len(R):
        a_list[sorted_thru] = R[track_right]
        track_right += 1
        sorted_thru += 1
    return a_list

with open('data.txt', 'r') as read_data:
    data = read_data.read().splitlines()
    for elem in data:
        lst = elem.split(" ")
        sort_this = []
        for char in range(1, len(lst)):
            if lst[char] != "":
                sort_this.append(int(lst[char]))
        sorted = merge_sort(sort_this, 0, len(sort_this)-1)
        # write to file
        dataOut = open('merge.out', 'w')
        dataOut.write(sorted)
        dataOut.close()
