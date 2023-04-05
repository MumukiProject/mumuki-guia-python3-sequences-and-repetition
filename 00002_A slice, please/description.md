:bread: _Slices_ are another set of operations lists and strings share, which allows us to get a segment of elements between two limits:

```python
ムnumbers = [10, 20, 30, 40, 50]
ムnumbers[0:2]
[10, 20]     	# is the list made up of the 1st and 2nd element;
             	# ⚠️ remember that indexes in Python count from 0
ムnumbers[2:4]
[30, 40]     	# is the list made up of the 3rd and 4th element
ムnumbers[0:4]
[10, 20, 30, 40] # the list composed by elements 1 to 4
ムnumbers[:4]
ム[10, 20, 30, 40] # equivalent to the previous example;
             	# if we don't put the lower limit,
             	# it gets all the elements from the beginning
ムnumbers[3:]
[40, 50]     	# is the list composed
             	# by all elements from the 4th position
             	# if we don't put the upper bound,
             	# it brings all elements to the end	 
```

> Let's apply what we've just learned to strings! We already loaded in the console a variable of type string called `first_verse`. 🔨 Using our new tools, do the following:
>
> 1. Find out how many characters `first_verse` has
> 2. Get a string with the first 23 characters of `first_verse`
> 3. Get a string with the last 25 characters of `first_verse`
