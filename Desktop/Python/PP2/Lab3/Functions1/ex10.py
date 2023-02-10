def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["1", "1", "1", "2", "2"])

print(mylist)
