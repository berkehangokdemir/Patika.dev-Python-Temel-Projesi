# Patika.dev Python Temel Projesi

## Sorular

1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: `[[1,'a',['cat'],2],[[[3]],'dog'],4,5]`

output: `[1,'a','cat',2,3,'dog',4,5]`

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: `[[1, 2], [3, 4], [5, 6, 7]]`

output: `[[[7, 6, 5], [4, 3], [2, 1]]`



## Cevaplar

### Cevap 1 (Flatten)

#### Fonksiyon:

```python
givenlist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattenedlist = []

def flatten(x):
    for i in x:
        if type(i) == list:
            flatten(i)
        elif type(i) != list:
            flattenedlist.append(i)


flatten(givenlist)
print(flattenedlist)
```

#### Sonuç:

```python
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]
```

##### Alternatif Liste Testi / Fonksiyon:

```python
typedlist = [[3,4], [[["a"]]], "b", 8, ["patika.dev"], 3.4, [["berkehan"]], 11, 12, True]
flattenedlist = []

def flatten(x):
    for i in x:
        if type(i) == list:
            flatten(i)
        elif type(i) != list:
            flattenedlist.append(i)

flatten(typedlist)
print(flattenedlist)
```

##### Alternatif Liste Testi / Sonuç:

```python
[3, 4, 'a', 'b', 8, 'patika.dev', 3.4, 'berkehan', 11, 12, True]
```



### Cevap 2 (Reverse)

 #### Fonksiyon:

```python
givenlist = [[1, 2], [3, 4], [5, 6, 7]]

def reversed(l):
    for i in range(len(l)):
        if type (l[i]) == list:
            l[i] = l[i][::-1]
            reversed(l[i])
    return (l[::-1])

reversedlist = reversed(givenlist)
print (reversedlist)
```

#### Sonuç:

```python
[[7, 6, 5], [4, 3], [2, 1]]
```

##### Alternatif Liste Testi / Fonksiyon:

```python
typedlist = [[1,2,[3,4]],[5],[6,[7,[8,9,10]]]]

def reversed(l):
    for i in range(len(l)):
        if type (l[i]) == list:
            l[i] = l[i][::-1]
            reversed(l[i])
    return (l[::-1])

reversedlist = reversed(typedlist)
print (reversedlist)
```

##### Alternatif Liste Testi / Sonuç:

```python
[[[[10, 9, 8], 7], 6], [5], [[4, 3], 2, 1]]
```



Bu proje [Berkehan Gökdemir](https://www.linkedin.com/in/berkehangokdemir) tarafından, [Patika.dev](https://www.patika.dev)'e teslim edilmiştir.
