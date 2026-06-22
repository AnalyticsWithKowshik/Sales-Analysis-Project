import pandas as pd
import matplotlib.pyplot as plt
#Load dataset
df=pd.read_excel("Product-Sales-Region.xlsx")
#Create Sales Column
df["sales"]=df["Quantity"]*df["UnitPrice"]
#Calculate Total Revenue
print("Total Revenue:")
print(df["sales"].sum())
#Top 5 Products by Revenue
print("\n Top 5 Products by Revenue:")
print(df.groupby("Product")
["sales"].sum().sort_values(ascending=False).head())
#Top 5 Regions by Revenue
print("\n Top 5 Regions by Revenue:")
print(df.groupby("Region")
["sales"].sum().sort_values(ascending=False).head())
#Top 5 Stores by Revenue
print("\n Top 5 Stores by Revenue:")
print(df.groupby("StoreLocation")["sales"].sum().sort_values(ascending=False).head())
#Best Selling Product
print("\n Best Selling product")
best_product=(df.groupby("Product")["sales"].sum().sort_values(ascending=False).idxmax()) 
print(best_product)
#Best Selling Store
print("\n Best Selling Store:")
print(df.groupby("StoreLocation")["sales"].sum().sort_values(ascending=False).idxmax())
#Montly Revenue Analysis
df["month"]=df["OrderDate"].dt.month_name()
print("\nMonthly Revenue Trend:")
monthly_revenue=(df.groupby("month")["sales"].sum())
print(monthly_revenue)
#Best Selling Month
print("\n Best Selling Month:")
print(monthly_revenue.idxmax())
#Worst Selling Month
print("\n Worst Selling Month:")
print(monthly_revenue.idxmin())
#Average Order Value
print("\n Average Order Value:")
aov=df["sales"].sum()/df["OrderID"].nunique()
print(round(aov,2))
#Monthly Sales Graph
df["MonthNum"]=df["OrderDate"].dt.month
df["Month"]=df["OrderDate"].dt.month_name()
monthly_revenue=df.groupby(["MonthNum","Month"])["sales"].sum().reset_index()
plt.bar(monthly_revenue["Month"],monthly_revenue["sales"])
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("monthly_revenue.png")
plt.show()
#Total Unique Order
print("Total Orders:",df["OrderID"].nunique())
#Total Unique Customer
print("Total Customers:",df["CustomerName"].nunique())
#Average Shipping Cost
print("Average Shipping Cost:",round(df["ShippingCost"].mean(),2))
#Top 5 products Revenue Bar Graph
top_products=df.groupby("Product")["sales"].sum().sort_values(ascending=False).head()
plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.savefig("top_products.png")
plt.show()