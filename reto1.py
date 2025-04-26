# Programa para calcular el costo total de una compra

# Llamo repetición Bucle gral
list=[]
Market = True
while Market:
   
    # Solicito nombre del producto
    print("The Brothers Market \n")
    product = input("Enter the product name \n")

    # Solicito precio unitario

    unit_price = float(input("Enter the unit price of the product \n"))
    while unit_price <= 0:
        print("The price must be greater than 0.")
        unit_price = float(input("Enter the unit price of the product \n"))
        
    # Solicito cantidad de productos
    quantity = int(input("Enter the quantity of products \n"))
    while quantity <= 0:
        print("The amount must be greater than 0.")
        quantity = int(input("Enter the quantity of products \n"))
    #Agrego respuesta a la lista
    list.append([quantity, product, unit_price])

    # Solicito porcentaje de descuento
    discount = float(input("Enter the discount percentage (0 a 100) \n"))
    while discount < 0 or discount > 100:
        print("The discount must be between 0 y 100.")
        discount = float(input("Enter the discount percentage(0 a 100) \n"))


    back = int(input("Do you want to add another product? Yes (1) NO (2) \n"))

    if back == 2:
        print("Finish")
        Market = False
    
    cost_without_discount = 0
    total_cost = 0
    for calc in list:
        cost_without_discount = cost_without_discount +(quantity * unit_price)
        reduct = (cost_without_discount * discount) / 100 
        total_cost = (cost_without_discount - reduct)

print("\n")     

print("total account without discount: ")
print("quantity, product, unitPrice")
for i in list:
    print(i[0],i[1],i[2])


print(f"total account= {cost_without_discount:.2f}\n")

print("*******************")
print("total account with discount: ")
print(f"{total_cost:.2f}")
         
            
    



    
