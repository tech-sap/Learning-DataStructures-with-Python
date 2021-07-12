import array

def print_arr():
      print("The array is ",end=" ")
      for i in a:
            print(i,end=" ")
      print("\r")
a = array.array('i',[1,2,3])
print_arr()
a.append(5)
print_arr()
a.insert(2,56)
print_arr()




