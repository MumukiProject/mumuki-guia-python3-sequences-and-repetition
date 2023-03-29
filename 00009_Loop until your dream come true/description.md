_But `for` is not just about numbers! For example we could also use it to accumulate a boolean result._ :open_mouth:

:person_swimming: Umi wants to know if in any of her last swimming times she beated her personal goal of 3 minutes:

```python
ムever_accomplished_goal([3.2, 3.4, 3.01, 3.08])
False # all her times were over 3 minutes
ムever_accomplished_goal([3.1, 3.2, 2.9, 3.1])
True # one of her times (2.9) was less than 3 minutes
```

And for that she defined the following function:

```python
def ever_accomplished_goal(times):
  accomplished = False # initially, the < 3 minute goal was not accomplished
 
  for time in times:
	  # but if any of them is less than 3 minutes,
    # then it will have passed it
	  accomplished = accomplished or time < 3 
  
  return accomplished
```

As we can see, here the local variable that we are using for _accumulator_ is boolean, and in each _iteration_ (that is, each time we visit a `time`) we will update its value, to know if that `time` or any of the previous ones was less than 3.


> Now it's your turn! Dani also doesn't want to lose her daily soccer practice :soccer: and needs a function `in_a_streak` that receives a list of how many minutes she practiced each day, and returns if her daily practice was always longer than 30 minutes:
>
>
> ```python
> ムin_a_streak([35, 40, 32, 60])
> True # every day she practiced more than 30 minutes
> ムin_a_streak([15, 45, 90, 0])
> False # a day she practiced only 15 minutes, and another day she didn't practice at all
>```
>
> Again, we leave you the function template to serve as a starting point.
