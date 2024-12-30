current_year=int(input("enter the current year"))
final_year=int(input("enter the final year"))
print("the leap years are:\n")
for year in range(current_year,final_year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print(year)