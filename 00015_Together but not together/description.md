Now what if we need to join lists of strings, but indicating a _separator_? For example:

```python
ムjoin_strings(" ", ["Nicki", "Nicole"])
"Nicki Nicole"
ムjoin_strings(",", ["Esposito", "Lali"])
"Esposito,Lali"
ムjoin("", ["W", "O", "S"])
"WOS" # we can still join without separators if we pass
  	# the empty string as argument
```

> Let's improve our previous function! Modify `join` so that we also receive a separator as first argument. The separator is a string that will go between each string.
