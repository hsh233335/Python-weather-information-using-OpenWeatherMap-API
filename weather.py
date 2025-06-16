import requests
import os
from ollama import chat
from ollama import ChatResponse
from tkinter import simpledialog
from tkinter import messagebox

# Loop for the program.
while True:
    # Get user's input.
    location = simpledialog.askstring("Location Information:", "Type exit or enter a city or talk to ai? just type ai:")
    if location is None:
        question0 = messagebox.askyesno("Question:", "Are you sure?")
        if question0 is True:
            break
        else:
            continue
    elif location.lower() == "exit":
        print("Exiting...")
        break
    
    # Ask Ai about anything mode. (Only uncomment when you want to ask ai.)
    # elif location.lower() == "ai":
    #     question = simpledialog.askstring("Question:", "What do you like to ask ai?")
    #     if question is None:
    #         question1 = messagebox.askyesno("Question:", "Are you sure?")
    #         if question1 is True:
    #             break
    #         else:
    #             continue
    #     answer: ChatResponse = chat(model= "llama3", messages= [
    #         {
    #             'role': 'user',
    #             'content': question,
    #         },
    #     ])
    #     messagebox.showinfo("Ai's response:", answer.message.content)
    #     continue

    measurement = simpledialog.askstring("Measurement:", "Enter a measurement unit (metric/imperial):")
    if measurement is None:
        question2 = messagebox.askyesno("Question:", "Are you sure?")
        if question2 is True:
            break
        else:
            continue
    unit = simpledialog.askstring("Unit:", "Enter a unit (celsius/fahrenheit):")
    if unit is None:
        question3 = messagebox.askyesno("Question:", "Are you sure?")
        if question3 is True:
            break
        else:
            continue

    # Get weather data from Openweathermap api.
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=YOURAPIKEY&units={measurement}")
    data = response.json()

    if response.status_code == 404:
        messagebox.showerror("Error", "City not found!")
    elif response.status_code == 502:
        messagebox.showerror("Error!", "Bad Gateway \n Try again later.")
    elif response.status_code != 200:
        messagebox.showerror("Error!", "Try again later.")

    # Exception clause to handle user's input for the city name not found.
    try:
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        place = data['name']
        country = data['sys']['country']
        weather = data['weather'][0]['description']
        humid = data['main']['humidity']
        wind = data['wind']['speed']
        convertwind = int(wind)
        temp = data['main']['temp']
        temperaturefeelslike = data['main']['feels_like']
        converttemp = int(temperaturefeelslike)

        valid_combo = (unit == "celsius" and measurement == "metric") or (unit == "fahrenheit" and measurement == "imperial")
        if not valid_combo:
            messagebox.showerror("Error!", "Unit and measurement do not match!\nUse celsius with metric and fahrenheit with imperial.")
            continue

        # Show the current weather information from Openweathermap api.
        messagebox.showinfo("Weather information:", 
            f"Location: {place} \n"
            f"The location of your city is {place}, and the country is {country}.\n"
            f"The longitude of your city is {longitude}. \n"
            f"The latitude of your city is {latitude}. \n"
            f"The weather of your city is {weather}. \n"
            f"Your wind in your city is {convertwind} m/s. \n"
            f"The humidity of your city is {humid}%.\n"
            f"Your temperature is {temp}°{'C' if unit == 'celsius' else 'F'}.\n"
            f"Your temperature (feels like) is {converttemp}°{'C' if unit == 'celsius' else 'F'}.\n \n"
            "It is also saved as weatherlog.txt at the directory this Python file is in"
        )

        # Creates a weatherlog.txt file after showing the current weather information.
        with open('weatherlog.txt', 'a', encoding= "utf-8") as weather_log:
            weather_log.writelines(["Weather information: \n"
            f"Location: {place} \n"
            f"The location of your city is {place}, and the country is {country}.\n"
            f"The longitude of your city is {longitude}. \n"
            f"The latitude of your city is {latitude}. \n"
            f"The weather of your city is {weather}. \n"
            f"Your wind in your city is {convertwind} m/s. \n"
            f"The humidity of your city is {humid}%.\n"
            f"Your temperature is {temp}°{'C' if unit == 'celsius' else 'F'}.\n"
            f"Your temperature (feels like) is {converttemp}°{'C' if unit == 'celsius' else 'F'}. \n \n"])

        # Asks you if you want to delete the log file.
        question4 = messagebox.askyesno("Question:", "Do you want to delete the log file?")
        if question4 is True:
            try:
                os.remove("weatherlog.txt")
                messagebox.showinfo("Information:", "Your weatherlog.txt file is successfully deleted.")
            except (FileNotFoundError, PermissionError):
                messagebox.showerror("Error!", "The weather log file couldn't be deleted. \n Please check if your weatherlog.txt file is in the same directory and try again later.")
                continue
        else:
            continue

    except (KeyError, NameError):
        messagebox.showerror("Error!", "City not found and information cannot be displayed! \n Or you didn't uncomment lines 23-38 for Ollama AI. \n If you don't have Ollama AI please look at how to install it in the github repository. \n If not, please don't use AI.")
    except ValueError:
        messagebox.showerror("Error!", "Inputs you entered previously must be a string. \n Or did you use a wrong type of Ollama AI?")
    except ModuleNotFoundError:
        messagebox.showerror("Error!", "Didn't you run pip install ollama?")
    except ConnectionError:
        messagebox.showerror("Error!", "Ollama isn't installed from https://www.ollama.com/download")
