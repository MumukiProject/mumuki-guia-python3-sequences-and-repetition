Otra operación que las listas y strings tienen en común son los _slices_, que podemos traducir como segmentos, secciones, o (de forma más literal y graciosa) rebanadas  :bread:, que nos permite obtener los elementos entre dos límites. 

```python
ム numeros = [10, 20, 30, 40, 50]
ム numeros[2:4]
[30, 40]         # es la lista conformada por el 3er y 4to elemento
ム numeros[0:4]
[10, 20, 30, 40] # es la lista conformada 
                 # por los elementos 1 al 4
ム numeros[:4]
[10, 20, 30, 40] # equivalente al ejemplo anterior; 
                 # si no ponemos el límite inferior, 
                 # trae todos los elementos desde el principio
ム numeros[3:]
[40, 50]         # es la lista conformada 
                 # por todos los elementos partir del 4to  
                 # si no ponemos el límite superior, 
                 # trae todos los elementos hasta el final                 
```


> Probá los ejemplos anteriores pero aplicándolos sobre strings. > ¿Funciona como te lo esperabas?