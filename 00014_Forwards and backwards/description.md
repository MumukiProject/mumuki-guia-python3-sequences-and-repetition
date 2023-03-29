The `[:]` slices and the `[]` indexing operator wouldn't be that useful if we couldn't also count backwards! :arrow_left: This is why Python accept:

 * positive indexes: start at `0` and count elements from first position to last;
 * negative indexes: start at `-1` and count elements from last position to first.

For example, this will let us interpret the string `"hello world"` in two different ways...

<table class="table table-bordered">
<thead>
  <tr>
	<th></th>
	<th>h</th>
	<th>e</th>
	<th>l</th>
	<th>l</th>
	<th>o</th>
            <th></th>
	<th>w</th>
	<th>o</th>
	<th>r</th>
	<th>l</th>
	<th>d</th>
  </tr>
</thead>
<tbody>
  <tr>
	<td>➡️</td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	<td>8</td>
	<td>9</td>
         <td>10</td>
  </tr>
  <tr>
	<td>⬅️</td>
            <td>-11</td>
	<td>-10</td>
	<td>-9</td>
	<td>-8</td>
	<td>-7</td>
	<td>-6</td>
	<td>-5</td>
	<td>-4</td>
	<td>-3</td>
	<td>-2</td>
	<td>-1</td>
  </tr>
</tbody>
</table>

... and perform operations like the following:

```python
ム"hello world"[:5] # the first 5 characters, as we already know
"hello"
ム"hello world"[:-1] # all characters except the last one
hello worl
ム"hello world"[-5:] # the last 5 characters
"world"
ム"hello world"[0] # first character, as we already know
"h"
ム"hello world"[-1] # last character
"d"	 
ム"hello world"[-2] # penultimate character
"d"
```

> Let's put everything we've seen into practice! Define:
>
> * a `no_ends` function that takes a list and returns a similar one but without its first and last elements;
> * an `extremes` function that does the exact opposite: it takes a list and returns another with only the first and last elements.
>
> ```python
> ムno_ends([4, 5, 10, 2, 3])
> [5, 10, 2]
> ムextremes([4, 5, 10, 2, 3])
> [4, 3]
> ```
