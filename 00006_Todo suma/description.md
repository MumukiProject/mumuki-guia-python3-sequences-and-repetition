Las cosas se ponen aún más interesantes cuando combinamos todo lo anterior. Por ejemplo, esta función `sumatoria`...

```python
def sumatoria(numeros):
  suma = 0
  
  for numero in numeros: 
    suma += numero
    
  return suma
```

... calcula la suma de todos los elementos de una lista de números...

```python
ム sumatoria([10, 5, 20])
35 # porque es 10 + 5 + 20
```

...o incluso de un rango: 

```python
ム sumatoria(range(1, 6))
15 # porque es 1 + 2 + 3 + 4 + 5
```






