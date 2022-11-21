import json
import requests

Max_payout = {
    "1 to 10 line games": 5000,
    "15 to 20 line games": 4000,
    "25 to 35 line games": 3000,
    "40 line games": 3000,
    "50 line games": 4000,
    "100 line games": 3000}

response = requests.get("https://api-test.spinomenal.com/reporting/getbrandstakes?partnerId=SPIN-test")
data1 = response.json()  # convert json data to python object-dict
documentation = data1.get('Data')  # or data['Data']    # we get list

for each_gambler in range(len(documentation)):
    each_game = documentation[each_gambler]  # dict

    value = list(each_game.values())

    CURRENCY = value[0]
    StakesConfig = value[1]  # list of dictionaries

    for each_round in range(len(StakesConfig)):
        rounds = StakesConfig[each_round]  # dict

        value_games = list(rounds.values())  # print(value_games)

        num_of_lines = value_games[0].split()
        del num_of_lines[-2:]

        num_of_stakes = value_games[1].split(',')
        res = list(map(float, num_of_stakes))  # convert list of strings to list of integers

        MAX_BET = round(max(res))
        MIN_BET = round(min(res))
        LINES = int(num_of_lines[-1])
        MAX_PAYOUT_PER_LINE = Max_payout[value_games[0]] if value_games[0] in Max_payout else 1
        MAX_EXP = MAX_BET * MAX_PAYOUT_PER_LINE * LINES

        json_dict = {
            'max_exposure': str(MAX_EXP),
            'max_bet': str(MAX_BET),
            'min_bet': str(MIN_BET),
            'currency': CURRENCY,
            'lines': str(LINES)
        }

        api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE3NDEyNzUxOCwidWlkIjoyNzgzNjk1NCwiaWFkIjoiMjAyMi0wOC0wNlQwODozNDo0OS42MjdaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTM5OTE1LCJyZ24iOiJ1c2UxIn0.buBnMyjxxPvPL3Is6OnvifvGqAyYfpxbctrg9Fgjj1c"
        apiUrl = "https://api.monday.com/v2"
        headers = {"Authorization": api_key}

        query = 'mutation ($myItemName: String!, $columnVals: JSON!) ' \
                '{ create_item (board_id:3515139152, item_name:$myItemName, column_values:$columnVals) { id } }'

        var = {'myItemName': 'Spin-test lines',
               'columnVals': json.dumps(json_dict)
               }

        data = {'query': query, 'variables': var}
        r = requests.post(url=apiUrl, json=data, headers=headers)
        print(r.json())



