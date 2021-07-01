import statistics

statistics.mean([2,5,6,9]) # 5.5
statistics.median([1,2,3,8,9])   # 3    middle value of numeric data in a list
statistics.median([1,2,3,7,8,9]) # 5.0
statistics.mode([2,5,3,2,8,3,9,4,2,5,6]) 		# 2  	most common data point in the list
statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]) 	#  1.3693063937629153    standard deviation


def test_statistics():
    """Statistics.

    The statistics module calculates basic statistical properties (the mean, median,
    variance, etc.) of numeric data.
    """

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

    assert statistics.mean(data) == 1.6071428571428572
    assert statistics.median(data) == 1.25
    assert statistics.variance(data) == 1.3720238095238095
