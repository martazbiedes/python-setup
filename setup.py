# A function named hello()

def hello():
  print("Hello, Marta!")
  
# Function named pack()

def pack(a,b,c):
  return [a,b,c]

# Function called eat_lunch(). 

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox has ripped!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I cry {my_lst[0]}")
      else:
        print(f"Then I eat {my_lst[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["chicken and veggies again :("])
eat_lunch(["grapes","fruit snacks","pasta","cookie"])
