# Read only
def read_only():
    '''a method that only reads the file'''
    try:
        file1 = open('data.txt', 'r')
        text = file1.read()
        print(text)
        file1.close()
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    '''a method that writes to a file'''
    file2 = open('more_data.txt', 'w') # if file exist it will be overwritten or created if it doesn't
    file2.write('oranges')
    file2.close()


# with open('data.txt') as f:
#     txt = f.read()
#     print(txt)

def read_food_sales():
    all_dates = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        print(data)
        for food_sale in data:

            split_food_sale = food_sale.split(',')
            
            order_date = split_food_sale[0]
            print(order_date)

            all_dates.append(order_date)


if __name__ == '__main__':
    # write_only() 
    # read_only()
    read_food_sales()
