def product_info(object_name="Uncnown name", color="none", price=0):
    print("Name product = ", object_name, sep = "\t")
    print("Color = ", color, sep = "\t")
    print("Price = ", price, sep = "\t")

product_info("Pen","Red",23)

product_info(price = 10, object_name = "Box")