print("Hey every one , I am Debashis")

def chai (n):
  print(n)

chai("Lemon tea")

# using : from importlib import reload
#         reload(file_name)  ----> we can reload any file in terminal
# We can import any module by just typing ----> import module_name
# Then we can use the functions in this module ----> module_name.function_name()

chai_one = "Lemon tea"
chai_two = "Mint tea"
chai_three = "Masala chai"

# Mutable vs immutable(the next updated value points to the another memory location)
x=5
y=x
print(y)
x=9
print(x)
print(y)
