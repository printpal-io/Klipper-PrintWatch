# Klipper-PrintWatch
PrintWatch Plugin that runs on any [Klipper](https://github.com/Klipper3d/klipper) based 3D Printer. This backend monitors the webcam stream on any Klipper printer for spaghetti type defects. It can work with any camera that is accessible via an IP address/HTTP endpoint. This Plugin requires [Moonraker](https://github.com/Arksine/moonraker) for making API requests to the Klipper firmware.

If you are an OEM using Klipper for their printers, please [contact us](https://printpal.io/contact/) for a more custom integration, support, and licensing options.

## Installation
This Backend component can be installed on any Linux device that is running Klipper. Ensure that the latest version of pip is installed on your device with the following commands:
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
git clone https://github.com/printpal-io/Klipper-PrintWatch
```
3. Change directories
```
cd Klipper-PrintWatch
```
4. Install libraries
```
pip3 install -r requirements.txt
```
5. Modify the settings file
```
sudo nano settings.json
```
Then change the `api_key` and `camera_ip` fields to match your configuration.

You can obtain your API key from your account's [settings tab](https://app.printpal.io), or [upgrade](https://printpal.io/standard-checkout/) if you haven't upgraded your account yet. 

The `camera_ip` field should be the URL address for retrieveing the _static image_ of your webcam. If using crowsnest (built-in streamer for Klipper), this URL is configured in your `crowsnest.conf` file. The address is typically `http://127.0.0.1/webcam/?action=snapshot`. Verify this by entering the URL into your browser and ensuring the static image of the webcam is returned.

6. Reload the systemctl daemo
```
sudo systemctl daemon-reload
```
7. Enable the systemctl process for PrintWatch
```
sudo systemctl enable /home/pi/Klipper-PrintWatch/printwatch.service
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

## Usage
In order to use the plugin, begin a print job and navigate to the [Web Application](https://app.printpal.io).

A few seconds after starting the print, your printer should be displayed on the `Printers` page. From here, modify the settings for your printer and click 'save', this will propogate the changes back down to your printer.

If this is your first time using the plugin, follow our [setup guide](https://printpal.io/documentation/tuning-your-setup/) for configuring your camera's settings, location, and the lighting.

## Development
Develop a custom integration with the AI backend by using the [REST API documentation](https://github.com/printpal-io/PrintWatchAI_Backend/wiki/REST-API) found on this repository.
