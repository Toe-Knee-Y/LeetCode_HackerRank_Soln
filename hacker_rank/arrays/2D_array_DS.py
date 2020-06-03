"""Problem link:
    https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
# Complete the hourglassSum function below.
def hourglassSum(arr):
    maximum = None
    for i in range(4):
        for j in range(4):
            hourglass_value = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            hourglass_value += arr[i+1][j+1]
            hourglass_value += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if maximum is None or hourglass_value >= maximum:
                maximum = hourglass_value
    return maximum