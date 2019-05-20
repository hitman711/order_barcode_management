import sys

import pandas as pd


def order_set():
    """
    Function to read order list file, filter out data,
    print top 5 customer order count and return dataset of order
    """
    # Read csv file
    order_list = pd.read_csv('orders.csv', sep=',')
    # Remove empty rows
    order_list.dropna(inplace=True)
    # Filter top 5 customer with max order
    top_5_customer = order_list.pivot_table(
        index=['customer_id'], aggfunc='size').sort_values(
        ascending=False).head(5).to_dict()
    # Print top 5 customer detail
    if top_5_customer:
        print('List of Top 5 customer with maximum orders')
    for x in top_5_customer:
        print('%s, %s' % (x, top_5_customer[x]))
    return order_list


def barcode_set():
    """
    Function to read barcode file, filter out non order barcode list,
    return dataset of orders with group of barcodes.
    """
    # Read csv file
    barcode_list = pd.read_csv('barcodes.csv', sep=',')
    # Count of unused barcode list
    print("Total no. of barcode left :- ",
          barcode_list[barcode_list.order_id.isnull()].count().barcode)
    # Remove unused barcode from list
    barcode_list = barcode_list[barcode_list.order_id.notnull()]
    # Convert order id from float to int
    barcode_list = barcode_list.astype(int)
    # Return list object which is collection of order_id and list of barcode
    return barcode_list.groupby('order_id').agg(lambda x: list(x))


def filter_operation():
    """
    Function to create customer orders csv file and
    print non barcode assign order list
    """
    # Collect barcode list
    barcode_list = barcode_set()
    # Collect order list
    order_list = order_set()
    # Merge both list
    new_list = pd.merge(order_list, barcode_list, on='order_id')
    # Reindex column for export file
    new_list = new_list.reindex(columns=['customer_id', 'order_id', 'barcode'])
    # Store data in export file
    new_list.to_csv('new_list.csv', index=None)
    # Filter orders which dont have barcode detail
    no_barcode = order_list[~order_list.order_id.isin(
        new_list.order_id)].to_dict('r')
    # Print no barcode order list
    if no_barcode:
        print("Following order no. don't have barcode")
    for x in no_barcode:
        print(x['order_id'], file=sys.stderr)


filter_operation()
