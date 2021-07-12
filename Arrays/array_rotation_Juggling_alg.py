import array
import math

def print_arr():
      print("The array is ",end="")
      for i in arr:
            print(i,end=" ")
      print()

arr = array.array('i',[1,2,3,4,5,6])
n = len(arr)
d = int(input("enter the number of elements to be rotated by left:"))%n
print_arr()
sets = math.gcd(n,d)
for i in range(0,sets):
      temp = arr[i]
      j = i
      while True:
            k = (j+d)%n
            if k==i:
                  break
            arr[j ] = arr[k]
            j = k
      arr[j] = temp
print_arr()
