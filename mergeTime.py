import time
import random
import functools

def sort_timer(func):
    """Returns the time needed for a function to operate"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        result = stop - start
        return result
    return wrapper

@sort_timer
def merge_sort(a_list, left=None, right=None):
    """Recursive implementation of merge sort. This method
    will split a_list into its appropriate sub-arrays and
    call merge for each"""
    if left is None:
        left = 0
    if right is None:
        right = len(a_list) - 1
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

def generate_merge_time():
    trial_avgs = []
    for x in range(1, 8):
        merge_times = []
        storing_list = []
        # generate random numbers to be stored in list
        for y in range(3000*x):
            storing_list.append(random.randint(-10000, 10000))
        # copy randomized list to be sorted by merge-sort
        for repeat in range(4):
            merge_list = list(storing_list)
            merge_timer = merge_sort(merge_list)
            merge_times.append(merge_timer)
        trial_avg = 0
        for trial in range(len(merge_times)):
            trial_avg += merge_times[trial]
        trial_avg /= len(merge_times)
        trial_avgs.append(trial_avg)

        dataOut = open('mergePlot.txt', 'w')
        dataOut.write(str(trial_avgs))
        dataOut.close()


generate_merge_time()