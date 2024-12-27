# Listas

Listas são bastante similares as tuplas e a maioria das operações que podemos fazer com tuplas também podemos fazer com as listas, uma das grandes diferenças está na implementação de protocolos de edição dos elementos, portanto as listas são mutáveis e permitem que incluamos novos itens, permitem a remoção de itens existentes e a reordenação.

As listas são criadas usando os literais ```[ ]``` ou a chamada para a classe ```list```.

Criando uma lista vazia

```python
colors = []  # forma preferida
# ou
colors = list()
```

Adicionando elementos ao final da lista

```python
colors.append("green")
```

Adicionando elementos ao inicio da lista

```python
colors.insert(0, "red")
```

Adicionando em uma posição especifica

```python
colors.insert(2, "blue")
```

Obtendo o tamanho da lista

```python
len(colors)
```

Acessando elementos via indice

```python
button_color = colors[0]
```

Desempacotamento (igual as tuplas)

```python
red, green, blue = colors
```

E também é possível já iniciar uma lista com valores.

```python
>>> colors = ["red", "green", "blue"]
>>> colors[0]
"red"
```

Podemos somar 2 listas (criando uma nova lista como resultado)

```python
>>> nova_lista = colors + ["yellow"]
>>> print(nova_lista)
["red", "green", "blue", "yellow"]
```

E podemos extender uma lista ```in-place```

```python
>>> colors.extend(["purple"])
>>> print(colors)
["red", "green", "blue", "purple"]

# Ou usando um operador de acréscimo
>>> colors += ["purple"]
>>> print(colors)
["red", "green", "blue", "purple"]
```

Remover elementos

```python
colors.remove("purple")
# ou
colors.pop()
```

Contar elementos

```python
>>> colors.count("green")
1=
```

Mais uma vez vos digo que existe uma infinidade de coisas interessantes para fazermos com a lista e faremos tudo em nossos exericios e projetos durante o treinamento.
