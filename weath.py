import requests
import json

# ------------全局变量-----------#
url_head = "https://api.seniverse.com/v3/weather/daily.json?"
key = "SfKmY_NJN1xWcsAOi"

three_day_weath_dict={}
# ---------------------------------#


def get_all_weath_dic():
    print(three_day_weath_dict)
    return three_day_weath_dict

def get_weather(locat_name):
    # 默认北京
    if locat_name == "\n" or locat_name == "":
        locat_name = "北京"

    locat_name = locat_name.replace("\n", "")  # 去掉自带的换行

    url = url_head + "key=" + key + "&" + "location=" + locat_name + "&" + "language=zh-Hans&unit=c&start=0&days=5"
    resq = requests.get(url)

    if resq.status_code == 200:
        val_data = resq.text
        weather_data = json.loads(val_data)  # str转字典
        locat = weather_data['results'][0]['location']['name']
        last_update = weather_data['results'][0]['last_update']

        three_day_weath_dict['location'] = locat
        three_day_weath_dict['last_update'] = last_update

        weath_cn = 0
        daily = weather_data['results'][0]['daily']
        while weath_cn < len(daily):
            daily_d = daily[weath_cn]

            three_day_weath_dict['text_day_'+str(weath_cn)] = daily_d['text_day']

            three_day_weath_dict['code_day_' + str(weath_cn)] = daily_d['code_day']
            three_day_weath_dict['high_' + str(weath_cn)] = daily_d['high']

            three_day_weath_dict['low_' + str(weath_cn)] = daily_d['low']

            three_day_weath_dict['humidity_' + str(weath_cn)] = daily_d['humidity']

            three_day_weath_dict['wind_direction_' + str(weath_cn)] = daily_d['wind_direction']

            weath_cn += 1

    else:
        print(resq.status_code)
        return 0


    return 1
