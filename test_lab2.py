import lab2.lab2split as code


sample = [1,3,2,4,6,9,11,8]

def testminmax():
 x = [1,11]
 assert (code.find_min_max(sample)==x)

def testavg():
 x = 5.5
 assert (code.calc_average(sample)== x)

def testmedian():
 x = 5
 assert (code.calc_median_temperature(sample) == x)