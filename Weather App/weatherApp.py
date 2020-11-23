import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image
from math import floor

url = "https://weather.com/weather/today/l/976b6655d9aca9c81a71e34d15d14584404ca60b55fe7cb52f1bcd1439f1a6a1"

master = Tk()
master.title("Weather App")
master.config(bg="white")

img = Image.open("weather1.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--1Ayv3").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--3KcTQ").text

    weatherPrediction = soup.find('div',class_="CurrentConditions--phraseValue--2xXSr").text
    temperature1 = str(floor((int(temperature[:2]) - 32) * 5 / 9))
    # Adding to lebel
    locationLabel.config(text=(location[:10]+location[20:-8]))
    temperatureLabel.config(text=temperature1+temperature[2])
    weatherPredictionLabel.config(text=weatherPrediction)

# Creating Lebel
locationLabel = Label(master, font = ("Calibri bold", 20),fg="steelblue",bg='white')
locationLabel.grid(row=0, sticky ="N",padx=40)
temperatureLabel = Label(master, font = ("Calibri bold", 80),fg='orange',bg='white')
temperatureLabel.grid(row=1, sticky ="W",padx=60)
Label(master, image=img, bg='white').grid(row=1,sticky='E')
weatherPredictionLabel = Label(master, font=("Calibri bold",18),fg='sandybrown',bg='white')
weatherPredictionLabel.grid(row=2,sticky='W', padx=60)
getWeather()
master.mainloop()