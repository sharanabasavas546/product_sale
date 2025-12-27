from datetime import datetime

# Global sales list
sales = []

def process_sale(product=None, quantity=0):

    if product is None:
        product = {
            "id": 0,
            "name": "Unknown",
            "price": 0,
            "stock": 0
        }

    print(f"[INFO] Processing sale for product: {product['name']}")
    print(f"[INFO] Requested quantity: {quantity}")
    print(f"[INFO] Available stock: {product['stock']}")

    if quantity <= product["stock"]:
        total = product["price"] * quantity
        product["stock"] -= quantity

        sales.append({
            "product": product["name"],
            "quantity": quantity,
            "amount": total,
            "date": datetime.now()
        })

        print(f"[SUCCESS] Sale completed")
        print(f"[SUCCESS] Total amount: {total}")
        print(f"[SUCCESS] Remaining stock: {product['stock']}")
        print("-" * 40)

        return total
    else:
        print("[ERROR] Insufficient stock")
        print("-" * 40)
        return None
