def car_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

car_info(year=2018, brand='nissan')