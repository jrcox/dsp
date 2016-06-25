[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> See below for code and answers:

```

import matplotlib
import thinkstats2
import thinkplot

#make pmf of number of kids per household
resps = chap01soln.ReadFemResp()
pmfnumkdhh = thinkstats2.Pmf(resps.numkdhh)

#make plot of pmf
thinkplot.Pmf(pmfnumkdhh, label = 'number of kids per hh')
thinkplot.Show()

#find mean of actual number of children per hh
pmfnumkdhh.mean()
```

The mean number of children under 18 in a household is 1.024

```

#look at biased pmf
def BiasPmf(pmf, label = ''):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x,x)
    new_pmf.Normalize()
    return new_pmf

#make biased pmf of children per hh
biasedpmf = BiasPmf(pmfnumkdhh, label = 'biased')

#plot both pmfs
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmfnumkdhh, biasedpmf])
thinkplot.Show()

#find mean of biasedpmf
biasedpmf.mean()
```
The mean number of children in the biased pmf is 2.403.



