import array
import math
arr = array.array('i',[1,2,3,4,5,6])

def reverse(arr,n):
      for i in range(n//2):
            arr[i] += arr[n-i-1]
            arr[n-i-1] = arr[i] - arr[n-i-1]
            arr[i] = arr[i] - arr[n-i-1]
      
def print_arr(a = arr):
      print("The array is ",end="")
      for i in a:
            print(i,end=" ")
      print()


n = len(arr)
d = int(input("enter the number of elements to be rotated by left:"))%n
print_arr()

a =array.array('i',arr[:d])
b = array.array('i',arr[d:])

reverse(a,len(a))
reverse(b,len(b))
print(a,b)

a.extend(b)
reverse(a, n)
print_arr(a)
