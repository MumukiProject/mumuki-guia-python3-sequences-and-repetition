As we once ever said, programming gives us great power: **it allows us to automate repetitive and boring tasks**.

But what does _repetitive_ mean? Let's see an example! How would we create a function that adds the first 5 elements of a list? Do you recognize a _pattern_ - something that repeats over and over again? 🥱

```python
def sum_five(a_list):
  return a_list[0] + a_list[1] + a_list[2] + a_list[3] + a_list[4]
```

Yeah, we're doing exactly the same thing 4 times: _access an element by index and then add it_. No doubt it would be much more convenient if the computer did that for us... otherwise we'd be lying to you about automating! :expressionless:

In this lesson we are going to learn how to tell the computer to repeat the same task several times, and some other tricks, too.
