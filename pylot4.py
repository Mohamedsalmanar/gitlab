import matplotlib.pyplot as plt
import csv


years = []
sales = []

#Reading CSV file:
with open("sales.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for each_row in reader:
        years.append(int(each_row[0]))
        sales.append(int(each_row[1]))

print(years)
print(sales)
    
plt.figure(figsize=(7,5))
plt.plot(years, sales,color='r',label="Yearly Sales ")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales for last 5 years ")
plt.grid(True)
plt.show()
