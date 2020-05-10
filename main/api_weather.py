import requests

def make_request_name(city_name):
    # returns the json file for current weather using city name
    api_url = 'http://openweathermap.org/data/2.5/weather?q=' + city_name + \
              '&appid=439d4b804bc8187953eb36d2a8c26a02'
    r = requests.get(api_url).json()
    return r

def make_request_hourly_city_id(city_id):
    api_url = 'http://openweathermap.org/data/2.5/forecast/hourly?id=' + str(city_id) +\
              '&appid=439d4b804bc8187953eb36d2a8c26a02'
    r = requests.get(api_url).json()
    r_list_24_hours = r['list'][:8]
    return r_list_24_hours

def make_request_query_set(query_set):
    hometown = ''
    list_city_details = []
    for i in query_set:
        api_url = 'http://openweathermap.org/data/2.5/weather?q=' + i.cities + \
                    '&appid=439d4b804bc8187953eb36d2a8c26a02'
        r = requests.get(api_url).json()
        if i.hometown == True:
            hometown = {'id' : i.id, 'set' : r}
            print('-------',hometown,'-------')
        else:
            list_city_details.append({'id' : i.id, 'set' : r})
    return hometown, list_city_details

if __name__ == '__main__':
    pass

