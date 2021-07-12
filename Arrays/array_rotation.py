#own method of array rotation
import array


def print_arr():
      print("The array is ",end='')
      for i in arr:
            print(i,end=" ")
      print("\r")

arr = array.array('i',[1,2,3,4,5])
print_arr()

n = int(input())

for i in range(n):
      arr.append(arr.pop(0))

print_arr()
