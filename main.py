#!/usr/bin/env python3

import csv

def main():
    process_csv()

def process_csv():

    with open('input.csv') as csv_file:
    
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:

            if line_count == 0:
                print(row)
                line_count += 1
            else:
                print(row)
                line_count += 1
                
        print(f'Processed {line_count} lines.')










if __name__ == "__main__":
    # execute only if run as a script
    main()