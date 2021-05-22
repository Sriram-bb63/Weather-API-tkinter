# Importing modules
from tkinter import Tk, Label
import json
import requests

# Creating window
root = Tk()
root.title("Weather")
# root.geometry("165x70")

# Display func
def disp(APIcity, APIaqi, APIstatus, color):
    root.configure(bg=color)
    # Labels
    city = Label(root, text=APIcity, bg=color, font=("Arial Bold", 10))
    city.grid(row=0, column=0)

    aqi = Label(root, text="AQI:"+str(APIaqi), bg=color, font=("Arial Bold", 10))
    aqi.grid(row=1, column=0, columnspan=3)

    status = Label(root, text=APIstatus, bg=color)
    status.grid(row=2, column=0, columnspan=3)


try:
    # getting API from AirNow
    APIfile = requests.get(
        'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY={apikey}'.format(
        zipcode='20002', apikey='B9B759FC-6C22-496B-BEE2-2025217AE65C')
        )
    print(">>>>>>>>>>", APIfile)
    print(">>>>>>>>>>", type(APIfile))
    print(">>>>>>>>>>", type(APIfile.content))

    # Get data from JSON
    data = json.loads(APIfile.content)
    print(">>>>>>>>>>",data)
    print(">>>>>>>>>>", type(data))
    APIcity = data[1]["ReportingArea"]
    APIaqi = data[1]["AQI"]
    APIstatus = data[1]["Category"]["Name"]

    # setting bg color
    if APIstatus == "Good":
        color = "green"
    elif APIstatus == "Moderate":
        color = "yellow"
    elif APIstatus == "Unhealthy for Sensitive Groups":
        color = "orange"
    elif APIstatus == "Unhealthy":
        color = "red"
    elif APIstatus == "Very Unhealthy":
        color = "purple"
    else:
        color = "maroon"

    # display data
    disp(APIcity, APIaqi, APIstatus, color)

except:
    root.configure(bg="red")
    error = Label(root, text="Error", bg="red")
    error.grid(row=0, column=1, columnspan=3)

# mainlooping window
root.mainloop()
