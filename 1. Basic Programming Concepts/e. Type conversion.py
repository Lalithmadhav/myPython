# Create a list of tuples containing purchase data with these fields:
#   Product name (string)
#   Quantity (string)
#   Price per unit (string)
#   Purchase date (string in format "DD-MM-YYYY")
import datetime

def process_purchase_data(purchase_records: list[tuple[str, str, str, str]]) -> list[tuple[str, int, float, datetime.datetime]]:
    """
    Convert purchase record strings to appropriate data types.
    Example input: [("Apple", "5", "1.50", "15-12-2024"), ...]
    """
    if not purchase_records:
        return []
    processed_data = []

    try:
        for data in purchase_records:
            item = str(data[0])
            quantity = int(data[1])
            ppi = round(float(data[2]),2) # ppi means Price per item
            pdate = datetime.datetime.strptime(data[3], "%d-%m-%Y").date() # pdate means Purchase date
            myTuple = (item, quantity, ppi, pdate)
            processed_data.append(myTuple)

    except ValueError as e:
        print(f"Error processing data: {e}")
    return processed_data

def generate_sales_report(processed_data):  # Monthly sales report
    """
    Generate a formatted sales report.
    Should include:
    - Total sales value (formatted to 2 decimal places)
    - Average purchase value
    - Highest and lowest purchase amounts
    """
    total_sale = 0
    highest = 0
    lowest = float('inf')

    def total_sale_value():
        for data in processed_data:
            nonlocal total_sale
            total_sale += data[1]*data[2]

    def highest_and_lowest_purchase():
        nonlocal highest, lowest
        for data in processed_data:
            lineTotal = data[1]*data[2]
            if lineTotal>highest:
                highest = lineTotal

            if lineTotal<lowest:
                lowest = lineTotal
        return [highest, lowest]

    def avg_purchase():
        return round(total_sale/len(processed_data), 2)
    
    
    total_sale_value()
    highest_and_lowest_purchase()
    avg_purchase= avg_purchase()

    print("\n|" + "-"*78 + "|")
    print(f"\n|{"SHOP RECEIPT":^78}|")
    print("\n|" + "="*78 + "|")
    print(f"\n|{"Item":<15}|{"Quantity":^14}|{"Price":>15}|{"linePrice":15}|{"Date":^15}|")
    print("\n|" + "-"*78 + "|")

    # for data in processed_data:
    for item, quantity, price, date in processed_data: # printing item wise data
        print(f"\n|{item:<15}|{quantity:^14}|{price:>15}|{linePrice(quantity, price):>15}|{date.strftime("%d-%m-%Y"):>15}|")
    
    print("\n|" + "-"*78 + "|")
    print(f"\n|{"Total":>46}|{total_sale:>31}|")
    print(f"\n|{"Average":>46}|{avg_purchase:>31}|")
    print(f"\n|{"Highest":>46}|{highest:>31}|")
    print(f"\n|{"Lowest":>46}|{lowest:>31}|")
    most_sold_item = None
    highest_quantity = 0

    # Loop through each item in the processed_data to find the item with the highest quantity
    for item, quantity, price, date in processed_data:
        if quantity > highest_quantity:
            highest_quantity = quantity
            most_sold_item = item # Most saled item

    print(f"Most Sold Item: {most_sold_item}")


    # print(f"\n|{"Discount":>30}{discount(total):>10}|")
    # print(f"\n|{"Final Price":>30}{total - discount(total):>10}|")

    print("\n|" + "-"*80 + "|")

    return {
        "Total sales value": total_sale,
        "Average purchase value": avg_purchase,
        "Highest purchase amount": highest,
        "Lowest purchase amount": lowest,
        "Most Sold Item": most_sold_item
    }

def print_daily_summary(processed_data): # Daily sales report
    """
    Print a summary showing:
    - Date (formatted nicely)
    - Number of items sold (right-aligned)
    - Total revenue (with 2 decimal places)
    """
    today_date = input("Enter a date for its report (DD-MM-YYYY): ").strip()
    today_date = datetime.datetime.strptime(today_date, "%d-%m-%Y").date()
    global invoice
    
    total = 0
    print("|" + "-"*78 + "|")
    print(f"|{"SHOP RECEIPT":^78}|")
    print("|" + "="*78 + "|")
    print(f"|  Invoice No.: #{invoice:04d}{"Date:":>47}{today_date.strftime("%d-%m-%Y"):<11}|")
    print(f"|{"Item":<20}|{"Quantity":^18}|{"Price":>18}|{"linePrice":>19}|")
    for item, quantity, price, date in processed_data:
        if today_date == date:
            print(f"\n|{item:<20}|{quantity:^18}|{price:>18}|{linePrice(quantity,price):>19}|")
            total += linePrice(quantity,price)
            
    print("|" + "-" * 78 + "|")
    print(f"|{'Total Sales':<58}|{total:>19.2f}|")
    print("|" + "-" * 78 + "|")
    invoice += 1

# Test data
purchase_records = [
    ("Apple", "5", "1.50", "15-12-2024"),
    ("Banana", "3", "0.75", "15-12-2024"),
    ("Orange", "12", "2.25", "16-12-2024")
]

global invoice
invoice = 1

def linePrice(quantity, price):
        return quantity*price

process_purchase_data(purchase_records)
generate_sales_report(processed_data)
print_daily_summary(processed_data)

# Write functions to:
# a) Convert all the numeric data to appropriate types (quantities to int, prices to float)
# b) Calculate total value for each purchase
# c) Format the output in different ways:

# Prices should show exactly 2 decimal places
# Quantities should be right-aligned in 3 spaces
# Dates should be converted to a more readable format