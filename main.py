from tkinter import *

import requests
from PIL import ImageTk,Image
import request
url = 'https://api.openweathermap.org/data/2.5/weather'
apiKey = '9e12d43bb1bccd972ea5ee64cf7272f7'
iconUrl = 'http://openweathermap.org/img/wn/{}@2x.png'


def getWeather(city):
    params = {'q':city,'appid':apiKey,'lang':'tr'}
    data = requests.get(url,params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp']-273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city,country,temp,icon,condition)


def main():
    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream= True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon



screnn = Tk()
screnn.geometry("300x450")
screnn.title("Hava Durumu")

cityEntry = Entry(screnn,justify="center")
cityEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntry.focus()

searchButton = Button(screnn,text="Arama",font=('Arial',15),command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel = Label(screnn)
iconLabel.pack()

locationLabel = Label(screnn,font=("Arial",40))
locationLabel.pack()

tempLabel= Label(screnn,font=("Arial",50,"bold"))
tempLabel.pack()

conditionLabel = Label(screnn,font=("Arial",20))
conditionLabel.pack()

screnn.mainloop()

