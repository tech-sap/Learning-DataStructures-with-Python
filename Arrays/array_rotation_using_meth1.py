import array
#using temp array
#O(n)
#O(d) --->auxillary space
def print_arr():
      print('The array is ',end=' ')
      for i in arr:
            print(i,end=' ')
      print()

arr = array.array('i',[1,2,3,4,5,6])
print_arr()
n = len(arr)
d = int(input("enter the number of times need to be rotated: "))
d = d%n
temp = arr[:d]
                                          
for i in range(d,n):   #0,1,2,3,4
      arr[i-d] = arr[i]  #1,2,3,4,5,
for i in range(n-d,n):
      arr[i] = temp[i-(n-d)]

print_arr()
