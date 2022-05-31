# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    # first check is_earlier
    start_hour = int(A[:2])
    start_min = int(A[3:])
    end_hour = int(B[:2])
    end_min = int(B[3:])

    # start time want to round up
    # ending time need to round down

    if start_min == 0:
        start_min = 0
    elif 0 < start_min <= 15:
        start_min = 15
    elif start_min <= 30:
        start_min = 30
    elif start_min <= 45:
        start_min = 45
    elif start_min <= 59:
        start_min = 0

        if start_hour == 23:
            start_hour = 0
        else:
            start_hour = start_hour + 1

    if 0 <= end_min < 15:
        end_min = 0
    elif end_min < 30:
        end_min = 15
    elif end_min < 45:
        end_min = 30
    elif end_min <= 59:
        end_min = 45

    # now we have successfully modified all the start and end hour and mins
    # we just need to calculate the intervals
    overnight = end_hour < start_hour
    if not overnight:
        return max(0, ((end_hour * 60 + end_min) - (start_hour * 60 + start_min)) // 15)
    end = end_hour * 60 + end_min + 24 * 60
    start = start_hour * 60 + start_min
    result = (end - start) // 15
    return max(0, result)

print(solution('20:00', '06:00'))