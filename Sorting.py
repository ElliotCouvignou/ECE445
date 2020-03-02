# code was taken from https://stackabuse.com/sorting-algorithms-in-python/ but
# modified to do extra Transcript bookeeping


def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # At this poimt i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot)
        nums[i], nums[j] = nums[j], nums[i]

        


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)



# new modified functions 

def partition_T(transcript, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = transcript.timestamps[(low + high) // 2][0]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while transcript.timestamps[i][0] < pivot:
            i += 1

        j -= 1
        while transcript.timestamps[j][0] > pivot:
            j -= 1

        if i >= j:
            return j

        # At this poimt i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot)
        transcript.swap(i, j)
        
        


def quick_sort_T(transcript):
    # Create a helper function that will be called recursively
    def _quick_sort(transcript, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(transcript, low, high)
            _quick_sort(transcript, low, split_index)
            _quick_sort(transcript, split_index + 1, high)

    _quick_sort(transcript, 0, len(transcript.timestamps) - 1)

# Verify it works
random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)