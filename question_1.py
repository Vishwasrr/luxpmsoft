def send_odds():
    json_data = {"array": [i for i in range(41) if i % 2 == 1]}
    print('printing for verificatioin', json_data)
    return json_data


# print(send_odds())
