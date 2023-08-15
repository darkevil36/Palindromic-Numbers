n = int(input("Enter The Digits:"))
list_a = []
for i in range(1, n+1):
	num = int(input("Number:"))
	list_a.append(num)
x = list_a
y = list(reversed(list_a))

if x == y:
	print("It Is Palindrome ")
else :
	print("It Is Not Palindrome")
print("Your Number:")
print(x)
print("Reversed Number")
print(y)