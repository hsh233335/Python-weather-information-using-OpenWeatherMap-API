# Python-weather-information-using-OpenWeatherMap-API
# Description
Shows the current weather information using OpenWeatherMap API and tkinter messagebox.
# What it does:
- Sends you a tkinter messagebox about the current weather.
- Shows an error when something goes wrong.
- Has 2 temperature types to choose from: **Celsius and Fahrenheit**.
- Warning: ***Celsius goes with metric input and Fahrenheit goes with imperial input***.
- ***Optional: Has an AI to chat. (using Ollama and requires windows 10 or later)***
# Requirements
Python 3 and above. Git. <br> **If you don't have git, press the green code button and the top and click "Download ZIP".
After that, extract the file and follow the steps below. (I would recommend moving the downloaded and extracted file to Desktop, get the python file out of the extracted folder.)**
# How do I run this code?
## Step 1:
Download the Python file.
## Step 2 (Optional (to use Ollama AI mentioned above):
Go to https://ollama.com/download
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
After that uncomment line 23-38.
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
Enjoy, run with
```
git clone https://github.com/hsh233335/Python-weather-information-using-OpenWeatherMap-API
```

# Example (Exactly how the program will prompt you)
![Capture100](https://github.com/user-attachments/assets/ae458d55-9f67-41be-aa94-1e4f83d0ca69) <br> <br>
![Screenshot 2025-06-11 145102](https://github.com/user-attachments/assets/09262f2a-aa13-4ea8-9276-d44c78dbf728) <br> <br>
![Screenshot 2025-06-11 145122](https://github.com/user-attachments/assets/e233ecc8-ecd1-45a7-9f6a-627af7f7b984) <br> <br>
![Capture105](https://github.com/user-attachments/assets/15009154-4024-4357-95cd-cbb748029f48) <br> <br>
After you click ok: (See updates below. These pictures below will come after the updates section.)<br> <br>
![Screenshot 2025-06-11 145528](https://github.com/user-attachments/assets/6f8e97ce-a3a6-42e3-90d8-e6c410641d92) <br> <br>
Then after clicking exit (the cross): <br> <br>
![Capture101](https://github.com/user-attachments/assets/5bf42325-be9d-4ec6-ac47-0bda0aa82390) <br> <br>
If you click **"Yes" the program will close**. **If no, it will return to the previous page**.

# Updates
- The sentence: "It is also saved as weatherlog.txt at the directory this Python file is in" is added to weather information tkinter messagebox to show that a weather log file is added. <br> <br>
  ![Capture107](https://github.com/user-attachments/assets/6935c247-8232-4329-920e-d7b01bd188bd) <br> <br>
- Added a log file feature that logs the weather information from the tkinter messagebox previously. <br> <br>
 ![Capture108](https://github.com/user-attachments/assets/b667ac6d-cc0a-4ca0-bc9d-321b9e959da7) <br> <br>
- Added a log file deleter that asks you if you want to delete the log file. (Will come after weather information messagebox) <br> <br>
  ![Capture103](https://github.com/user-attachments/assets/5a628341-5fb5-4b0c-b815-3cfd1f61722b) <br> <br>
  **If you press yes, this screen below will show. Or if you pressed no, it will return to the first page.** <br> <br>
  ![Capture104](https://github.com/user-attachments/assets/5dbe0b80-81b1-4707-b05b-9b5c5edbcc93) <br> <br>
  Then will return you. <br> <br>
  ![Screenshot 2025-06-11 145528](https://github.com/user-attachments/assets/6f8e97ce-a3a6-42e3-90d8-e6c410641d92)
