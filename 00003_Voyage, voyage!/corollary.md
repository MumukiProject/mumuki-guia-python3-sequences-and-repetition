Several things have just happened! First, _ranges_ have entered the stage, which are another Python data type representing a sequence of numbers that can be:

* correlative, as in `range(1, 10)`, which is nothing more than the sequence of numbers from `1` to `9` (yes, the last is not included :exclamation:)
* with jumps, as in `range(0, 10, 3)`, which are the numbers from `0` to `9` jumping by a _step_ of 3: `0`, `3`, `6`, `9`

On the other hand, we have just learned that the `for ... in` lets us "visit" each element of a list, string or range of numbers, and do something with it. To do this, this control structure has three parts:

  1. `in` allows us to specify which sequence of elements to loop through;
  2. `for` allows us to choose a name which will refer to **each** element of the sequence;
  3. and after the `:` we will have one or more actions that will be executed when visiting each element. :warning: ⚠️ Watch out! **They have to be indented with respect to the `for` line**

When writing `print_each_element` we decided to:

  1. loop through each element of the `elements` parameter:
  2. call each of those elements `element`;
  3. print each of those elements using `print`.


Very nice, but it doesn't look like we did anything useful here :confused:. Can we do more than just display items?
