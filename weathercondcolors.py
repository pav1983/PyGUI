import requests
from tkinter import *
import io
from PIL import ImageTk, Image
import urlopen

root=Tk()

root.title("Weather Widget")
root.resizable(0,0)
root.wm_attributes('-topmost',1)
root.geometry("375x150")

#main area display
info = StringVar()

weather = Message(root, textvariable = info, width = 200)   
info.set("What's your weather?")            
weather.grid(row=1, column=1)


#function that gets weather
def getWeather():
    #Replace YOURAPIKEYHERE with the API key you obtain by signing up at https://openweathermap.org/
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid={your api goes here}&units=imperial&zip='
    country_code = ',us'
    zip_code = e.get()
    
    url = api_address + zip_code + country_code
    json_data = requests.get(url).json()
    
    if 'message' in json_data:
        info.set('Invalid zip code.')
    
    else:
        city = json_data['name']
        #description = json_data['weather'][0]['description']
        #icon = json_data['weather'][0]['icon']
        temperature = str(json_data['main']['temp']) + u'\u00b0' + " F"
        #weather['fg'] = 'red'
        weather['font'] = 'Courier 18 normal'
        #weather['bg'] = 'pink'
    
        info.set(city + "\n" + temperature)
        
        if json_data['main']['temp'] >= 110 and json_data['main']['temp'] <= 119.9:
            weather['bg'] = 'burgundy'
        elif json_data['main']['temp'] >= 100 and json_data['main']['temp'] <= 109.9:
            weather['bg'] = 'brown'
        elif json_data['main']['temp'] >= 90 and json_data['main']['temp'] <= 99.9:
            weather['bg'] = 'red'
        elif json_data['main']['temp'] >= 80 and json_data['main']['temp'] <= 89.9:
            weather['bg'] = '#eb7434'
        elif json_data['main']['temp'] >= 70 and json_data['main']['temp'] <= 79.9:
            weather['bg'] = '#ebc934'
        elif json_data['main']['temp'] >= 60 and json_data['main']['temp'] <= 69.9:
            weather['bg'] = 'yellow'
        elif json_data['main']['temp'] >= 50 and json_data['main']['temp'] <= 59.9:
            weather['bg'] = 'gray'
        elif json_data['main']['temp'] >= 40 and json_data['main']['temp'] <= 49.9:
            weather['bg'] = '#03f4fc'
        elif json_data['main']['temp'] >= 30 and json_data['main']['temp'] <= 39.9:
            weather['bg'] = '#0394fc'
        elif json_data['main']['temp'] >= 20 and json_data['main']['temp'] <= 29.9:
            weather['bg'] = '#034afc'
        elif json_data['main']['temp'] >= 10 and json_data['main']['temp'] <= 19.9:
            weather['bg'] = '#6703fc'
        elif json_data['main']['temp'] >= 0 and json_data['main']['temp'] <= 9.9:
            weather['bg'] = '#c7ace8'
        elif json_data['main']['temp'] >= -10 and json_data['main']['temp'] <= -19.9:
            weather['bg'] = '#ece4f7'


label=Label(root,text='Enter your zip code:  ')
label.grid(row=3, column=1, sticky='E')

e=Entry(root)
e.grid(row=3, column=2)

sub = Button(root,text='Get Weather', command = getWeather)
sub.grid(row=4, column=2)

root.mainloop()
