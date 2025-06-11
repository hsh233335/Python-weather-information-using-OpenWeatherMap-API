# Python-weather-information-using-OpenWeatherMap-API
# Description
Shows the current weather information using OpenWeatherMap API and tkinter messagebox.
# What it does:
- Sends you a tkinter messagebox about the current weather.
- Shows an error when something goes wrong.
- Has 2 temperature types to choose from: **Celsius and Fahrenheit**.
- Warning: ***Celsius goes with metric input and Fahrenheit goes with imperial input***.
- ***Optional: Has an AI to chat. (using Ollama and requires windows 10 or later)***
# How do I run this code?
## Step 1:
Download the Python file.
## Step 2 (Optional (to use Ollama AI mentioned above):
Go to https://ollama.com/.
## Step 3 (Optional (to use Ollama AI mentioned above):
Download the installation file depending on your operating system, and follow instructions on-screen.
## Step 4 (Optional (to use Ollama AI mentioned above):
Run this in your terminal:
```
pip install ollama
```
and this:
```
ollama pull llama3
```
After that uncomment line 22-37.
## Step 5 (Required from now on):
Go to https://home.openweathermap.org/users/sign_up, and **create an account**. **If you already have an account**, go to https://home.openweathermap.org/api_keys, and copy the API Key.
## Step 6:
Replace the API Key at the **YOUR API KEY** text in code line 55.
## Step 7:
Run 
```
python weather.py
```
or without terminal view run:
```
pythonw weather.py
```
## Step 8:
Enjoy!

# Example (Exactly how the program will prompt you)
![Capture100](https://github.com/user-attachments/assets/ae458d55-9f67-41be-aa94-1e4f83d0ca69) <br> <br>
![Screenshot 2025-06-11 145102](https://github.com/user-attachments/assets/09262f2a-aa13-4ea8-9276-d44c78dbf728) <br> <br>
![Screenshot 2025-06-11 145122](https://github.com/user-attachments/assets/e233ecc8-ecd1-45a7-9f6a-627af7f7b984) <br> <br>
![Screenshot 2025-06-11 145147](https://github.com/user-attachments/assets/a1bc4d8f-90e7-4780-8367-53279017418f) <br> <br>
After you click ok: <br> <br>
![Screenshot 2025-06-11 145528](https://github.com/user-attachments/assets/6f8e97ce-a3a6-42e3-90d8-e6c410641d92) <br> <br>
Then after clicking exit (the cross): <br> <br>
![Capture101](https://github.com/user-attachments/assets/5bf42325-be9d-4ec6-ac47-0bda0aa82390) <br> <br>
If you click **"Yes" the program will close**. **If no, it will return to the previous page**.
