from datetime import datetime

# global sales record
sales = []

def process_sale(
    product={"id": 0, "name": "Unknown", "price": 0, "stock": 0},
    quantity=0
):
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
