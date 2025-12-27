def process_sales(product, quantity):
    if quantity <= product["stock"]:
        total = product["price"] * quantity
        product["stock"] -= quantity

        sales.append({
            "product": product["name"],
            "quantity": quantity,
            "amount": total,
            "date": datetime.now()
        })
        return total
    else:
        return None
