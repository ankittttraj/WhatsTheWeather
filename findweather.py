from datetime import datetime
from tkinter import *
from tkinter import messagebox

# for timezone calculation
import pytz
import requests
# for co-ordinates
from geopy.geocoders import Nominatim
# for timezone
from timezonefinder import TimezoneFinder

root = Tk()
root.configure(bg='white')


# function of giving city details
def searchcity():
    try:
        city = search_entry.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        time_zone_obj = TimezoneFinder()
        result = time_zone_obj.timezone_at(lng=location.longitude, lat=location.latitude)
        curr_location = pytz.timezone(result)
        local_time = datetime.now(curr_location)
        curr_time = local_time.strftime("%I:%M %p")
        curr_date = f"{datetime.now(curr_location).day}/{datetime.now(curr_location).month}/{datetime.now(curr_location).year}"
        clock.config(text=curr_time)
        time_zone.config(text=result)
        print(f"City Name is: {city}")
        # api for weather
        api_base_url = "https://api.openweathermap.org/data/2.5/weather?"
        api_key = 'bad8fabfab678f738531b4705c5872fb'
        url = api_base_url + "appid=" + api_key + "&q=" + city
        json_data = requests.get(url).json()
        # condition = json_data['weather'][0]['main']
        details = json_data['weather'][0]['description']
        temp_cel = int(json_data['main']['temp'] - 273.15)
        temp_faren = 1.8 * temp_cel + 32
        temp_faren = round(temp_faren, 1)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise_time = datetime.utcfromtimestamp(json_data['sys']['sunrise'] + json_data['timezone'])
        sunset_time = datetime.utcfromtimestamp(json_data['sys']['sunset'] + json_data['timezone'])
        sunrise_time_.config(text=f"{sunrise_time}")
        sunset_time_.config(text=f"{sunset_time}")
        temp_label_.config(text=f"{temp_cel}°C | {temp_faren}°F")
        # feels_like.config(text=f"feels: {temp} °C")
        wind_.config(text=f"{wind} m/s")
        detail_.config(text=f"{details}")
        humidity_.config(text=f"{humidity} %")
        pressure_.config(text=f"{pressure} hPa")
        date_label.config(text=curr_date)
    except Exception as e:
        messagebox.showerror("What's The Weather", "Invalid Entry, Please enter a proper city name.")


root.title("What's the Weather?")
root.geometry("950x500")
root.maxsize(950, 500)
root.minsize(950, 500)

# search box
photo = PhotoImage(file="Images/searchbar.png")
search_label = Label(image=photo, bg="white")
search_label.place(x=20, y=20)

# entry form
search_entry = StringVar()
search_box = Entry(root, justify="center", width=17, font="clarendon 25 bold", bg="#404040", border=0, fg="white",
                   textvariable=search_entry, highlightthickness=0)
search_box.place(x=50, y=40)
search_box.focus()

# search image
searchicon = PhotoImage(file="Images/searchicon.png")
buttonsearch = Button(image=searchicon, borderwidth=0, cursor="hand2", bg="#404040", command=searchcity, highlightthickness=0)
buttonsearch.place(x=399.5, y=33)

# to enter button press
root.bind('<Return>', lambda event: searchcity())

# weather logo
w_logo = PhotoImage(file="Images/weather_img.png")
weather_logo = Label(image=w_logo, borderwidth=15, bg="white")
weather_logo.place(x=130, y=100)

# sunrise sunset

sunrise = PhotoImage(file="Images/sunrise_img.png")
i_sunrise = Label(image=sunrise, highlightthickness=0)
i_sunrise.place(x=550, y=220)

sunset = PhotoImage(file="Images/sunset_img.png")
i_sunset = Label(image=sunset, highlightthickness=0)
i_sunset.place(x=750, y=220)

# box
box = PhotoImage(file="Images/bottom_ui.png")
box_image = Label(image=box)
box_image.pack(side=BOTTOM)

# labels
name1 = Label(root, text="WIND", font=("Arial Black", 15, 'bold'), fg="white", bg="#500474")
name1.place(x=55, y=400)

name2 = Label(root, text="HUMIDITY", font=("Arial Black", 15, 'bold'), fg="white", bg="#500474")
name2.place(x=250, y=400)

name3 = Label(root, text="DETAILS", font=("Arial Black", 15, 'bold'), fg="white", bg="#500474")
name3.place(x=500, y=400)

name4 = Label(root, text="PRESSURE", font=("Arial Black", 15, 'bold'), fg="white", bg="#500474")
name4.place(x=750, y=400)

# adding dot dot
temp_label_ = Label(text="...", font="arial 47 bold", fg="#500474", bg="white")
temp_label_.place(x=495, y=145)

clock = Label(font="stencil 20 bold", bg="white")
clock.place(x=700, y=7)
date_label = Label(font="stencil 16 bold", bg="white")
date_label.place(x=720, y=55)

b = Label(text="Timezone : ", font="sansserifcollection 11 bold", bg="white")
b.place(x=70, y=90)
time_zone = Label(justify="center", font="sansserifcollection 13 bold", bg="white")
time_zone.place(x=165, y=90)

wind_ = Label(text="...", font="arial 18 bold", fg="white", bg="#500474")
wind_.place(x=40, y=430)

humidity_ = Label(text="...", font="arial 18 bold", fg="white", bg="#500474")
humidity_.place(x=270, y=430)

detail_ = Label(text="...", font="arial 18 bold", fg="white", bg="#500474")
detail_.place(x=480, y=430)

pressure_ = Label(text="...", font="arial 18 bold", fg="white", bg="#500474")
pressure_.place(x=750, y=430)

sunrise_time_ = Label(font="arial 12 bold", bg="white")
sunrise_time_.place(x=500, y=330)

sunset_time_ = Label(font="arial 12 bold", bg="white")
sunset_time_.place(x=700, y=330)

root.mainloop()
