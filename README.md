# PrintWatchAI_Backend
Backend component for PrintWatchAI Plugin for Duet This backend monitors the webcam stream on any RepRapFirmware printer for spaghetti type defects. It can work with any camera that is accessible via an IP address/HTTP endpoint.

## Installation
This Backend component can be installed on any Linux device. Ensure that the latest version of pip is installed on your device with the following commands:
```
pip install --upgrade pip
```

In some cases you will need to specify pip3:
```
pip3 install --upgrade pip
```

In some cases, you will need to upgrade using python:
```
python -m pip install --upgrade pip
```

Please follow the steps below for your device:

### Raspberry Pi
1. SSH into the Raspberry Pi and navigate to the root directory of the user
```
cd /home/pi
```
2. Download this repository's release for Raspberry Pi
```
wget https://github.com/printpal-io/PrintWatchAI_Backend/archive/refs/tags/raspberrypi.zip
```
3. Unzip the file
```
unzip raspberrypi.zip && rm raspberrypi.zip
```
4. Change directories
```
cd PrintWatchAI_Backend-raspberrypi
```
5. Install libraries
```
pip3 install -r requirements.txt
```
6. Reload the systemctl daemo
```
sudo systemctl daemon-reload
```
7. Enable the systemctl process for PrintWatch
```
sudo systemctl enable /home/pi/PrintWatchAI_Backend-raspberrypi/printwatch.service
```
8. Start the systemctl process for PrintWatch
```
sudo systemctl start printwatch.service
```
9. Validate the printwatch process is running
```
sudo journalctl -u printwatch
```
Outputs:
```
Sep 08 23:35:24 pi systemd[1]: Started PrintWatch AI.
Sep 08 23:35:28 pi python3[2237]: INFO:     Started server process [2237]
Sep 08 23:35:28 pi python3[2237]: INFO:     Waiting for application startup.
Sep 08 23:35:28 pi python3[2237]: INFO:     Application startup complete.
Sep 08 23:35:28 pi python3[2237]: INFO:     Uvicorn running on http://0.0.0.0:8989 (Press CTRL+C to quit)
```

**Install the webcam streaming service:**

1. SSH into the Raspberry Pi and navigate to the root directory of the user
```
cd /home/pi
```
2. Pull uStreamer
```
git clone --depth=1 https://github.com/pikvm/ustreamer
```
3. Change directories
```
cd ustreamer
```
4. Install dependencies
```
sudo apt install libevent-dev libjpeg9-dev libbsd-dev libasound2-dev libspeex-dev libspeexdsp-dev libopus-dev
```
5. Install
```
sudo make install
```
6. Make uStreamer user
```
sudo useradd -r ustreamer
```
```
sudo usermod -a -G video ustreamer
```
7. Enable and start the systemctl process for uStreamer
```
sudo systemctl enable /home/pi/PrintWatchAI_Backend-raspberrypi/ustreamer.service
```
```
sudo systemctl start ustreamer.service
```

Once the uStreamer is installed and enabled, use the snapshot URL: `http://<raspberrypi-ip>:8080/snapshot` for the `Webcam URL` setting. Verify the URL by entering it into your browser and having a static image returned.
### Orange Pi
1. SSH into the Orange Pi and navigate to the root directory of the user
```
cd /home/orangepi
```
2. Download this repository's release for Orange Pi
```
wget https://github.com/printpal-io/PrintWatchAI_Backend/archive/refs/tags/orangepi.zip
```
3. Unzip the file
```
unzip orangepi.zip && rm orangepi.zip
```
4. Change directories
```
cd PrintWatchAI_Backend-orangepi
```
5. Install libraries
```
pip3 install -r requirements.txt
```
6. Reload the systemctl daemo
```
sudo systemctl daemon-reload
```
7. Enable the systemctl process for PrintWatch
```
sudo systemctl enable /home/orangepi/PrintWatchAI_Backend-orangepi/printwatch.service
```
8. Start the systemctl process for PrintWatch
```
sudo systemctl start printwatch.service
```
9. Validate the printwatch process is running
```
sudo journalctl -u printwatch
```
Outputs:
```
Sep 08 23:35:24 orangepi systemd[1]: Started PrintWatch AI.
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Started server process [2237]
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Waiting for application startup.
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Application startup complete.
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Uvicorn running on http://0.0.0.0:8989 (Press CTRL+C to quit)
```


### Linux
1. SSH into the Orange Pi and navigate to the root directory of the user
```
cd /home/{user}
```
2. Download this repository's release for Orange Pi
```
wget https://github.com/printpal-io/PrintWatchAI_Backend/archive/refs/tags/orangepi.zip
```
3. Unzip the file
```
unzip orangepi.zip && rm orangepi.zip
```
4. Change directories
```
cd PrintWatchAI_Backend-orangepi
```
5. Install libraries
```
pip3 install -r requirements.txt
```
6. Modify the `printwatch.service` file to match your configuration. Replace the `{user}` with your Linux devices corresponding name
```
[Unit]
Description=PrintWatch AI
After=multi-user.target

[Service]
WorkingDirectory=/home/{user}/PrintWatchAI_Backend-orangepi/
User={user}
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/{user}/PrintWatchAI_Backend-orangepi/main.py

[Install]
WantedBy=multi-user.target
```
7. Reload the systemctl daemo
```
sudo systemctl daemon-reload
```
8. Enable the systemctl process for PrintWatch
```
sudo systemctl enable /home/{user}/PrintWatchAI_Backend-orangepi/printwatch.service
```
9. Start the systemctl process for PrintWatch
```
sudo systemctl start printwatch.service
```
10. Validate the printwatch process is running
```
sudo journalctl -u printwatch
```
Outputs:
```
Sep 08 23:35:24 orangepi systemd[1]: Started PrintWatch AI.
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Started server process [2237]
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Waiting for application startup.
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Application startup complete.
Sep 08 23:35:28 orangepi python3[2237]: INFO:     Uvicorn running on http://0.0.0.0:8989 (Press CTRL+C to quit)
```


## Development
Develop a custom integration with the AI backend by using the [REST API documentation](https://github.com/printpal-io/PrintWatchAI_Backend/wiki/REST-API) found on this repository.
