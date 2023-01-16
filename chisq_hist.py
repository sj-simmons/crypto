# chisq_hist.py
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from lcg import prng

sample_size = 12000
bins = 30 # we will split the sampled random numbers into equal bins

def chi_squared_test():
    """Return a chi_square test."""

    #take a binned sample
    sample = [prng()//(2**64//bins) for _ in range(sample_size)]

    # get just the frequences of the occurrences for each bin
    frequencies = dict()  # maps bin to frequency for that bin
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    frequencies = frequencies.values()

    expected_frequency = sample_size/bins

    return sum(map(lambda x: (x-expected_frequency)**2, frequencies))/expected_frequency

results = [chi_squared_test() for _ in range(5000)] # the results of 5000 chi_squared tests

# plot a histogram of the results of the 5000 tests
plt.hist(results, bins = 50, density = True)
x = np.arange(0, 60, 0.001)
plt.plot(x, stats.chi2.pdf(x, df=bins-1), label="degrees of freedom = 29")
plt.legend()
plt.show()
