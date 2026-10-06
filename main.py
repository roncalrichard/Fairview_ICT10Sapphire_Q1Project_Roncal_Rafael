from pyscript import document, display

def build_inventory_sku_record(e):
    # Clear the div content 
    document.getElementById('sku_tag_display').innerHTML = ""
    
    # Create variables for category, product name, and stock quantity from input fields
    category = document.getElementById('inv_cat_select').value
    product_name = document.getElementById('inv_item_title_in').value.strip()
    stock_qty = int(document.getElementById('inv_qty_in').value)
    
    # Create the SKU variable using slicing and string concatenation
    sku_code = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
    
    # Display the SKU
    display("SKU: ", sku_code, target='sku_tag_display')