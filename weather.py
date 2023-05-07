from tkinter import *
import requests
import json
from tkinter import messagebox
#from xpinyin import Pinyin

#------------全局变量-----------#

root = Tk()#GUI

#文本
location_text = Text(root,width=25,height=2,font=("楷体",12))
location_text.grid(row=0,column=1)

#url = 'https://api.seniverse.com/v3/weather/daily.json?key=SfKmY_NJN1xWcsAOi&location=beijing&language=zh-Hans&unit=c&start=0&days=5'

url_head = "https://api.seniverse.com/v3/weather/daily.json?"
key = "SfKmY_NJN1xWcsAOi"

#---------------------------------#

def get_weather(locat_name):
    #默认北京
    if locat_name == "\n":
        locat_name="北京"

    locat_name=locat_name.replace("\n","")#去掉自带的换行

    url = url_head + "key=" + key + "&" + "location="+locat_name + "&" + "language=zh-Hans&unit=c&start=0&days=5"
    #print(url)
    resq = requests.get(url)


    if resq.status_code==200:
        val_data = resq.text
        #print(val_data)
    
        #va = val_data
        #print(type(val_data))
        weather_data = json.loads(val_data) #str转字典
        #print(weather_data)#字典类型
     
        locat = weather_data['results'][0]['location']['name']
        timezone = weather_data['results'][0]['location']['timezone']
        timezone_offset = weather_data['results'][0]['location']['timezone_offset']

        
        print("==========================")    
        print("")

        print("地区：",locat)
        print("时区：",timezone)    
        print("时区偏移：",timezone_offset)
        print("")

        weath_cn=0
        daily = weather_data['results'][0]['daily']
        while weath_cn <len(daily):

            daily_d = daily[weath_cn]
            print("")
            print("--------") 
            print("时间：",daily_d['date'])
            print("天气：",daily_d['text_day'])    
    
            print("今日最高温度(℃):",daily_d['high'])
            print("今日最低温度(℃):",daily_d['low'])
            print("湿度(%):",daily_d['humidity'])
            print("风向:",daily_d['wind_direction'])
            
            print("风速(km/h):",daily_d['wind_speed'])
            print("风向角度(0~360):",daily_d['wind_direction_degree'])
            print("风力等级:",daily_d['wind_scale'])
            print("降水量(mm):",daily_d['rainfall'])

            weath_cn+=1
               
        print("")

        print("最后更新于:",weather_data['results'][0]['last_update'])
        print("")
        print("==========================")


    else :
        print(resq.status_code) 
def start_request():
    text = location_text.get("1.0","end")
    print(text)
    #获取天气
    
    get_weather(text)

def info_request():
    messagebox.showinfo(title="提示",message="在文本框输入查询地区，之后会出来未来3天天气状况哦~\r\n仅限市级城市呀😊      作者：拾贰  版本：v1.0  日期：23-03-17")

def init_gui():
    root.geometry("380x100+750+400")
    root.title("—天气获取工具😀—  Author:拾贰")
    start_button = Button(root,text="获 取",anchor='w',font=("楷体",15),command=start_request)
    start_button.grid(row=0,column=0)
    
    info_button = Button(root,text="关  于",anchor='w',font=("楷体",15),command=info_request)
    info_button.grid(row=1,column=0)
    #label = Label(root,text="\r\n")
    #label.grid(row=0,column=0)
    #location_text.pack()
    
def main():
    init_gui()

    root.mainloop()

main()