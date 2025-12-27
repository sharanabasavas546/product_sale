import product_sales

def test_successful_sale():
    product = {"id": 10, "name": "Tablet", "price": 20000, "stock": 5}
    
    total = product_sales.process_sale(product, 2)
    
    assert total == 40000
    assert product["stock"] == 3


def test_insufficient_stock():
    product = {"id": 11, "name": "Camera", "price": 30000, "stock": 1}
    
    total = product_sales.process_sale(product, 5)
    
    assert total is None
    assert product["stock"] == 1


def test_sales_record_added():
    product = {"id": 12, "name": "Speaker", "price": 5000, "stock": 10}
    
    initial_sales_count = len(product_sales.sales)
    product_sales.process_sale(product, 1)
    
    assert len(product_sales.sales) == initial_sales_count + 1
