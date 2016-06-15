# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are a sequence of values, enclosed in brackets [].  Tuples are also a sequence of values, sometimes  
enclosed in parantheses ().  The major difference between the two is that lists are mutable (can be changed)  
and tuples are immutable (cannot be changed).  Tuples work as keys in dictionaries, and not lists, because  
tuples are hashable and lists are not.  This means that it has a unique ID that does not change, because it  
is immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that they are both a sequence of values, but a set contains unique values, none of them can be the same.  It refers to a set in the mathematical sense, which refers to the unique values in a space.  For example:  
    ``` 
    list1 = ['cat', 'dog', 'mouse', 'cat', 'horse', 'dog', 'cow', 'dog']  
    set1 = ('cat', 'dog', 'mouse', 'horse', 'cow')  
    ```
    Performance for finding an element is faster in a set than a list because a set is hashable and so each value is unique and can be readily called, whereas in a list every element needs to be inspected.
    

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an unbound anonymous function that does not use ```def```.  It is useful in writing simpler code, especially in instances when a function will only be called once.  A lambda function is typically written on only one line, making for cleaner code.  
An example of lambda in the key argument for sorted:  
    ```sorted(['Apple', 'banana', 'donut', 'Carrot'], key = lambda word: word.upper()) ```  
Would return:  
    ```['Apple', 'banana', 'Carrot', 'donut']```  
    
        

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to construct a list using natural language.  For example, if we wanted to construct a list that was the square of all numbers 0 - 5:  
    ``` lc = [x**2 for x in range(6)]```  
    If we wanted to do this with map and lambda it would look like:  
    ```maplist = map(lambda x: x**2, range(6))```  
    If we wanted to do this with filter it would look like:  
    ```filterlist = filter(lambda x: x < 7, maplist)```  
    My understanding is that list comprehension is the most clear and in some cases the fastest way to make a list.  
  
    Set comprehension is similar, except that now you're making a set and not a list, but still using the same natural language to make the set.  
    ``` sc = {x**2 for x in range(6)}```  
    Dictinary comprehension follows the same idea:  
    ``` dc = {x:x**2 for x in range(6)}```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





