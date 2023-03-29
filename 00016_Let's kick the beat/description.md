Lucky we found you, we thought you were leaving! Could you stay a little longer in this lesson? It so happens that Umi and Dani have asked us to help them keep track of their statistics.

For now, Umi has already defined this function...

```python
def how_many_times_beat_goal(times):
  count = 0
 
  for time in times:
	if time < 3:
  		count += 1
    
  return count
```

...which is very similar to the one we had already defined, but it has a novelty: now we count **how many times** the goal was exceeded. And for that we need an `if`, with some new features:

  * On the one hand, it is inside the `for`, tabulated, and it returns nothing;
  * on the other hand, it has no `else`: if the condition is not met, it does _nothing_.

This kind of `if` is also very common when programming in those situations that instead of returning a thing or another, we just need to **perform some effect** based on a condition.  In our example, in each iteration if the condition `duration < 3` is met, the `times` accumulator will be incremented, otherwise it will stay the same.



> Knowing this, now let's help Dani define ``, which returns the number of times she trained for more than 30 minutes.
>
> ```python
> ムhow_many_times_trained_enough([35, 40, 32, 60])
> 4 # every day practiced more than 30 minutes
> ムhow_many_times_trained_enough([15, 45, 90, 0])
> 2 # only two days trained more than 30 minutes
> ```
