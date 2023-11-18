import utelegram
import network
import time
import dht
import machine
import max44009
from machine import SoftI2C, Pin
import bme280

try:

    i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
    # ESP32 - Pin assignment

    lux = max44009.MAX44009(i2c)
    lux.continuous = 1
    lux.manual = 0
    lux.current_division_ratio = 0
    lux.integration_time = 3
    lux._read_config()
    
    i2c_bme = SoftI2C(scl=Pin(19), sda=Pin(18), freq=10000)
    bme = bme280.BME280(i2c=i2c_bme)

    print('Starting...')

    max_retry_count = 7

    def do_connect(ssid_list, password_list):
        sta_if = network.WLAN(network.STA_IF)
        count = 0
        
        connected = False

        if not sta_if.isconnected():
            for i, ssid in enumerate(ssid_list):
                print(f'Connecting to network {ssid}')
                sta_if.active(True)
                sta_if.connect(ssid, password_list[i])

                while count < 7:
                    count += 1

                    if sta_if.isconnected():
                        count = 0
                        break
                    print('.', end='')
                    time.sleep(1)

                if count == 7:
                    print(f'Failed to connect to network {ssid}, retrying in 5 seconds...')
                    count = 0
                    sta_if.disconnect()
                    time.sleep(1)  # Add a delay before retrying
                else:
                    connected = True
                    break  # Exit the loop if connected successfully

        if not connected:
            count = 0
            print('Failed to connect to any network, sleeping...')
            machine.deepsleep(5000)
        print('Network config:', sta_if.ifconfig())
        
    ssid_list = ['ssid1', 'ssid2']
    password_list = ['pass1','pass2']

    do_connect(ssid_list, password_list)

    TOKEN='<BOT-TOKEN>'
    CHAT_ID='<channel-id>'

    emoji_temp = chr(0x0001F321)
    emoji_hum = chr(0x0001F4A7)
    degree_celcius = chr(0x2103)
    emoji_lightbulb = chr(0x0001F4A1)
    emoji_pressure = chr(0x0001F3CB)

    def get_temp_hum(max_retries=3):
        for _ in range(max_retries):
            try:
                sensor.measure()
            except OSError as e:
                print(f'Failed to read sensor. {e}')
                time.sleep(1)
                continue  # Continue to the next iteration
            temp = sensor.temperature()
            hum = sensor.humidity()
            return temp, hum
        print("Maximum retries reached. Unable to read sensor.")
        machine.deepsleep(5000)

    bot = utelegram.ubot(TOKEN)
    print('getting sensor readings...')
    try:
        sensor = dht.DHT11(machine.Pin(14))
        temp, hum = get_temp_hum()
        lux_val = lux.lux
        pres = bme.pressure
    except:
        print("Failed to get readings")
        machine.deepsleep(5000)

    msg = f'{emoji_temp} Temperature:   {temp}{degree_celcius}\n{emoji_hum} Humidity:          {hum}%\n{emoji_lightbulb} Lux:                    {lux_val}\n{emoji_pressure} Atm. Pressure:  {pres}\n'
    print(msg)
    ok = bot.send(CHAT_ID, msg)
    if ok:        
        print('sent message, sleeping...')
        machine.deepsleep(3600000)
    else:
        print('caught error, sleeping...')
        machine.deepsleep(5000)

except Exception as e:
    print(e)
    time.sleep(2)
    machine.deepsleep(5000)


