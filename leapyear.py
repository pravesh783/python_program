year=int(input("enter a year :"))
if (year % 4==0 and year % 100!=0) :
	print("{}year is leap year ".format(year))
else:
	print("{} year is not leap year ".format(year))