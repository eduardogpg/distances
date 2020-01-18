import csv

# To Slow
from numpy import array
from pandas import DataFrame

from math import sin, cos, sqrt, atan2, radians

def open_tsv_file(path, delimiter='\t'):
    try:
        file = open(path)
        return list(csv.DictReader(file, delimiter=delimiter))
    except:
        print(f'No es posible encontrar el archivo: {path}')

def calculate_distance(lat1, long1, lat2, long2):
    lat1, long1 = radians(lat1), radians(long1)
    lat2, long2 = radians(lat2), radians(long2)
    
    dlon = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return 6373.0 * c

if __name__ == '__main__':
    users = open_tsv_file('./users_no_orders.tsv')
    restaurants = open_tsv_file('./top_restaurants.tsv')
    

    matriz = []
    headers = [restaurant['STORE_ID'] for restaurant in restaurants]
    headers.insert(0, '')

    matriz.append(headers)
    
    for user in users:
        user_id = user['APPLICATION_USER_ID']
        
        row = [user_id]
        for restaurant in restaurants:
            
            distance = calculate_distance(
                float(user['LAT']), float(user['LNG']),
                float(restaurant['REST_LAT']), float(restaurant['REST_LNG'])
            )

            row.append(distance)
        matriz.append(row)
    
    # To Slow
    data = array(matriz)
    print(DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))