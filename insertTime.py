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
def insert_sort(a_list):
    for i in range(1, len(a_list)):
        key = a_list[i]
        j = i - 1
        while j >= 0 and a_list[j] > key:
            a_list[j+1] = a_list[j]
            j = j - 1
        a_list[j + 1] = key
    return a_list

def generate_insert_time():
    trial_avgs = []
    for x in range(1, 8):
        insertion_times = []
        storing_list = []
        # generate random numbers to be stored in list
        for y in range(3000*x):
            storing_list.append(random.randint(-10000, 10000))
        # copy randomized list to be insertion-sorted
        for repeat in range(4):
            insertion_list = list(storing_list)
            insertion_timer = insert_sort(insertion_list)
            insertion_times.append(insertion_timer)
        trial_avg = 0
        for trial in range(len(insertion_times)):
            trial_avg += insertion_times[trial]
        trial_avg /= len(insertion_times)
        trial_avgs.append(trial_avg)

        dataOut = open('insertPlot.txt', 'w')
        dataOut.write(str(trial_avgs))
        dataOut.close()


generate_insert_time()