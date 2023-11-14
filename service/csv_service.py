import csv
import io

def create_index_csv(product, index):
    with open('index.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        if csvfile.tell() == 0:
            csv_writer.writerow(['type','profitability_index'])

        csv_writer.writerow([product.type]+ [index])

def create_deal_csv(product1, product2, csv_data=None):
    if csv_data == None:
        csv_data = io.StringIO()
    csv_writer = csv.writer(csv_data)

    if csv_data.tell() == 0:
        csv_writer.writerow(['DEAL'] +
                            ['FIRST PRODUCT'] +
                            [column.name.upper() for column in type(product1).__table__.columns] +
                            ['SECOND PRODUCT'] +
                            [column.name.upper() for column in type(product2).__table__.columns] +
                            ['DEAL PRICE'])
        
    deal_price = round((product1.price + product2.price)*0.9,2)

    csv_writer.writerow([f'{product1.type} + {product2.type}'] +
                        [''] +
                        [getattr(product1, column.name) for column in type(product1).__table__.columns] +
                        [''] +
                        [getattr(product2, column.name) for column in type(product2).__table__.columns] +
                        [deal_price])
    
    return csv_data
