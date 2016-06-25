[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Plotting the pmf:

```python

import thinkstats2
import thinkplot
import random

#generate random set of numbers from 0 - 1 and plotting pmf
rand = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(rand)
thinkplot.Pmf(pmf)
thinkplot.Show()

#plotting cdf
cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(cdf)
thinkplot.Show()

```
Overall, the cdf shows that it is not perfectly random, as there is some variation in the line.  However the overall trend is a straight line where x = y, indicating a general trend of randomness.
