¿Y si ahora quisieramos juntar listas de strings, pero indicando además un _separador_? Por ejemplo: 

```python
ム juntar(" ", ["Nicki", "Nicole"])
"Nicki Nicole"
ム juntar(",", ["Esposito", "Lali"])
"Esposito,Lali"
ム juntar("", ["W", "O", "S"])
"WOS" # podemos seguir uniendo sin separadores si pasamos 
      # la lista vacía como argumento
```

> ¡Mejoremos nuestra funcion anterior! Modificá `juntar` para que podamos recibir también un separador. El separador es lo que va a ir entre cada string.
