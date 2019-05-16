#!/usr/bin/env python3

import csv
from order import Order

global orders
orders = {}

def main():
    process_csv()

    for order_id in orders:
        orders.get(order_id).get_stuff()

    print()
    print('Orders fully loaded')

    order_id = "placeholder"

    while True:
        

        barcode = input('scan a barcode')
        
        # order
        if '-' not in barcode:
            order_id = "#" + barcode
            print('order id: ' + order_id)

            if order_id not in orders:
                print("Error! Unable to find Order")
                order_id = "placeholder"
            else:
                print('Order found!')
                print(orders.get(order_id).get_quantities())
            print()

        # meal
        else:
            sku = barcode
            

            if orders.get(order_id).order_contains_sku(sku):
                print('found meal with sku: ' + sku)
                orders.get(order_id).meal_scanned(sku)
                print('picked: ' + str(orders.get(order_id).get_picked()))
            else:
                print('Error! Unable to find meal with sku: ' +sku)
            



def process_csv():

    with open('input.csv') as csv_file:
    
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        prev_order_id = "placeholder"

        for row in csv_reader:
            line_count += 1

            if line_count == 1: # headers row
                continue

            order_id = row[0]

            # create Order object
            if not order_id == prev_order_id:
                prev_order_id = order_id
                create_order(order_id, row)

            # add meals to Order object
            add_meals_to_order(order_id, row)


        print('Processed ' + str(line_count) + ' lines.')

def create_order(order_id, row):
    # order_id, shipping_method, datetime, name
    orders[order_id] = Order(order_id, row[14], row[15], row[24])

def add_meals_to_order(order_id, row):
    # sku, meal, quantity
    orders.get(order_id).add_meals(row[20], row[17], row[16])

    # print(order_id +"   "+ row[20] +"   "+ row[17] +"   "+ row[16])


if __name__ == "__main__":
    # execute only if run as a script
    main()