Things get even more interesting when we combine all these tools. For example, this `summation` function...

```python
def summation(numbers):
  result = 0
 
  for number in numbers:
    result += number
    
  return result
```

...calculates the sum of all elements given a list of numbers, by adding them, one by one, to our `sum` variable - which is usually called an _accumulator_:

```python
ムsummation([10, 5, 20])
35 # because it is 10 + 5 + 20
ムsummation([])
0 # because the sum of an empty list is 0
```

It also works with ranges:

```python
ムsummation(range(1, 6))
15 # because it is 1 + 2 + 3 + 4 + 5
```

> Let's see if it is clear: complete the definition of the `product` function which, like `summation`, takes a sequence of numbers, but instead of adding them all, it multiplies them:
>
> ```python
> ムproduct([10, 2, 3])
> 60# because it's 10*2*3
> ムproduct([3, 3, 2, 4])
> 72# because it is 3*3*2*4
> ムproduct([8])
> 8 # because the product of a number is that same number
> ムproduct([])
> 1 # because the product of an empty list is 1
> ```
>
