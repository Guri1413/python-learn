# coomparison
x=2;
print(x==2);
y=3;
print(y==2);
print(x<y);

#boolean operators
name="meow";
age=2;
if name=="meow" and age==2:
	print("your name is meow and u r 2 yrs old");

if name=="meow" and age==3:
	print("ur name is meow but u r not 3 yrs old");

#in operator
name="meow";
if name in["meo","john"]:
	print("your name is either meow or john");

else:
	print("your name is not in list");