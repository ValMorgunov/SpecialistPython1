## "Диагонали символами"

### Задание

Даны сторона квадрата. Вывести его диагонали символами #

### Формат входных данных

Дано целое число n, длина стороны квадрата. 1 < n < 20 

### Формат выходных данных

Вывести диагонали квадрата символами # (см. примеры)

#### Примеры

n = 6 
```
#    #
 #  #
  ##
  ##
 #  #
#    #
```
n = 3
```
# #
 #
# #
```
### Решение задачи

```python
side = int(input("Введите сторону квадрата: "))
i = 0
if side % 2 == 0:
    count = side // 2-1
else:
    count = side // 2
row = ""
paint = "#"
void = " "
while count > i:
    row = void*(i)+paint+void*(side-(i+1)*2)+paint
    print(row)
    i += 1
if side % 2 == 0:
    row=void*(count)+paint*2
    print(row)
    print(row)
else:
    row = void * (count) + paint
    print(row)
while i>0:
    row = void * (i-1) + paint + void * (side - (i) * 2) + paint
    print(row)
    i -= 1
```
