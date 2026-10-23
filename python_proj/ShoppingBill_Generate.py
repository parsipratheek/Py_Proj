products = []
total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(item)
    total = total + price * quantity

print("\n SHOPPING BILL ")
print("Product\t\tPrice\tQuantity\tAmount")

for item in products:
    amount = item["price"] * item["quantity"]
    print(item["name"], "\t", item["price"], "\t",
          item["quantity"], "\t", amount)

print("Final Amount: Rs.", round(total, 2))
