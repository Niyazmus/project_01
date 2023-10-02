# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]

def vibor(lst):
  n = len(lst)
  i = 0
  while i < n - 1:
    m = i
    j = i + 1
    while  j < n:
      if lst[j] < lst [m]:
        m = j
      j += 1
    lst[i],lst[m] = lst[m],lst[i]
    i += 1
  return lst


def minimum(arr):
    print ('МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    print ('Сортировка выбором')
    
    for lst in arr:
      print ('Минимальное значение из списка', lst, vibor(lst)[0])
    
    
def maximum(arr):
    print ('МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ')
    print ('Сортировка выбором')
    
    for lst in arr:
      print ('Максимальное значение из списка', lst,vibor(lst)[-1])
    
   

def main():
  print (minimum(arr))
  print (maximum(arr))

main()
  