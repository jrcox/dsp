[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>  Below is code and process for answering question 2.4:
    
```
#first import data necessary
#make data set of pregnancy data
preg = nsfg.ReadFemPreg()
#make dataset of live births
live= preg[preg.outcome ==1]
#make dataset of first borns and not first borns
firsts = live[live.birthord ==1]
others = live[live.birthord !=1]

#make weight variable for two groups
weightfirst = firsts.totalwgt_lb
weightothers = others.totalwgt_lb

#make preg length variable for two groups
lengthfirst = firsts.prglngth
lengthothers = others.prglngth

#write function to compute cohens d 
def cohensd(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooledvar = (n1*var1 + n2*var2) / (n1 + n2)
    d = diff / math.sqrt(pooledvar)
    return d
    
cohensd(weightfirst, weightothers)
cohensd(lengthfirst, lengthothers)    
```
Answer:  The difference in the means of weight between firstborn and other chilren is -0.088, which means that firstborn children are slightly lighter (they are entered first into the function and so the number is with respect to firsts).  The computed Cohen's d for the effect estimate of pregnancy length between these two groups is 0.029 standard deviations.  So the effect estimate of weight is relatively larger than pregnancy length.  However, both of the effect estimates are less than 0.1, making them very small effect estimates.  In this case, it would not be appropriate to make much of this effect estimate for difference in weight.
