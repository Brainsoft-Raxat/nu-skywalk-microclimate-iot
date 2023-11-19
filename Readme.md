# ESP32 Skywalk microclimate monitoring system

Project Description
The Skywalk microclimate monitoring system is an IoT application that allows NU students to know the temperature, humidity, luminosity and atmospheric pressure at the skywalk between the Main Atrium and student residential blocks. The goal of the project was to use the skills learned in the course labs in a practical setting, demonstrating the benefits of the Internet of Things to a wider audience (students passing through skywalk and scanning the QR and learning about the project).


## Requirements

- ESP32 microcontroller
- DHT11 sensor (for temperature and humidity)
- MAX44009 sensor (for light intensity)
- BME280 sensor (for atmospheric pressure, temperature, and humidity)
- Telegram Bot API token
- Wi-Fi credentials (SSID and password)

## Getting Started

### 1. Telegram Bot API Token

To use this script, you need to create a Telegram Bot and obtain the Bot API token. Follow these steps:

1. Open the Telegram app and search for the "BotFather" bot.
2. Start a chat with BotFather and use the `/newbot` command to create a new bot.
3. Follow the instructions provided by BotFather to set a name and username for your bot.
4. Once the bot is created, BotFather will provide you with a unique API token. Save this token; you'll need it later.

### 2. Configure Wi-Fi

In the script, replace the placeholder values for Wi-Fi credentials with your own SSID and password:

```python
ssid_list = ['your_ssid']
password_list = ['your_password']
```

### 3. Configure Telegram Bot Token and Channel ID
```python
TOKEN = 'your_bot_token'
CHAT_ID = 'your_channel_id'
```

### 4. Connect Sensors
Connect the DHT11, MAX44009, and BME280 sensors to the appropriate pins on your ESP32. Update the pin configurations in the script if necessary.

### 5. Upload and Run
Upload the script to your ESP32 using your preferred method (e.g., via USB or OTA). After uploading, the script will run on the ESP32, read sensor data, and send it to the specified Telegram channel.