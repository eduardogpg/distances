from typing import Dict
from typing import List
from typing import Union

from numpy import array
from pandas import DataFrame

from modules.calculate.distance import Distance
from modules.tsv.opentsv import openTsv
# from typing import Union


def main(args: List[str]) -> int:
    tsv = openTsv()
    dist = Distance()
    path_user = 'tsv_files/users_no_orders.tsv'
    path_restaurants = 'tsv_files/top_restaurants.tsv'
    users: List[Dict[str, str]] = tsv.open_tsv_file(path_user)
    restaurants: List[Dict[str, str]] = tsv.open_tsv_file(path_restaurants)

    matriz: list = []
    headers: list = [
        restaurant['STORE_ID'] for restaurant in restaurants
    ]
    headers.insert(0, '')

    matriz.append(headers)

    for user in users:
        user_id: str = user['APPLICATION_USER_ID']

        row: List[Union[str, float]] = [user_id]
        for restaurant in restaurants:

            distance: float = dist.calculate_distance(
                float(user['LAT']), float(user['LNG']),
                float(restaurant['REST_LAT']), float(restaurant['REST_LNG'])
            )

            row.append(distance)
        matriz.append(row)

    # To Slow
    data = array(matriz)
    dtf = DataFrame(
        data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:]
    )
    print(dtf)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
