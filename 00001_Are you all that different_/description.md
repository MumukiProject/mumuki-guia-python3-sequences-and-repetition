In previous lessons we have seen several functions, procedures and operators that work with numbers, booleans, lists and so on.

But you may have already noticed that there are two operations in particular that are quite _peculiar_: `len` and `in`. Why? Let's look at the following examples:

```python
ムlen("you cannot eat money, oh, no")
28
ム"new" in "I got new rules, I count 'em"
True
ムlen([4, 8, 15, 16, 23, 42])
6
ム34 in [1, 1, 2, 3, 5, 8, 13, 21, 34]
True
```

`len` and `in` work with both lists and strings!

> Is this just a coincidence? Are there more common operations between these two data types? Let's find out by trying the following expression:
>
> ```python
ム"i was born" + "in Constitucion"
```
>
> ```python
ム"And I'm feeling good"[4]
```
>
> ```python
ム[1, 4] + [4, 5]
```
>
> ```python
ム["what", "about", "us"][2]
```
