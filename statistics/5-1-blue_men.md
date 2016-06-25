[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>  Finding percentage of population between 5'10 and 6'1:
    
```python

import scipy.stats

#set parameters for distribution
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc = mu, scale = sigma)

#how many people between 5'10 and 6'1
fiveten = dist.cdf(177.8)
sixone = dist.cdf(185.4)
fiveten, sixone, sixone-fiveten

```
34.2% of the sample are between 5'10 and 6'1.
