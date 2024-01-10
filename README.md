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
Then modify the `api_key` and `camera_ip` fields to match your configuration.

You can obtain your API key from your account's [settings tab](https://app.printpal.io), or [upgrade](https://printpal.io/standard-checkout/) if you haven't upgraded your account yet. 

The `camera_ip` field should be the URL address for retrieveing the _static image_ of your webcam. If using crowsnest (built-in streamer for Klipper), this URL is configured in your `crowsnest.conf` file. The address is typically `http://127.0.0.1/webcam/?action=snapshot`. Verify this by entering the URL into your browser and ensuring the static image of the webcam is returned.

If you want to edit the `api_key` or `camera_ip` after having started the `printwatch.service`, you must run the command `systemctl restart printwatch` for the changes to take effect.

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

## Enabling the AI component on Mainsail UI

You must overwrite the Mainsail directory with the folder in this repository in order to enable the AI panel (this will change in the future).

1. Change directories to root:
```
$ cd ~
```
2. Overwrite the current mainsail folder:
```
$ cp -r /Klipper-PrintWatch/mainsail mainsail/
```
3. Verify that the AI component is on the WebUI by visiting `http://<DEVICE IP>` and navigating to the Dashboard:

![image](https://github.com/printpal-io/Klipper-PrintWatch/assets/95444610/7a273fce-f842-464c-8a20-ace9150d5c11)



# How to use the PrintWatch AI plugin on Mainsail UI

## Navigate to the dashboard

Visit the Mainsail UI page at `http://<RPi IP address>`
Navigate to the dashboard and observe the `AI` component added to the dashbaord items:

![image](https://github.com/printpal-io/MATTERSHAPER_BUILD/assets/95444610/bd2251f2-5283-4cee-990a-be9e22b4f27d)

**What each item means:**

`Status` : this is the status of the AI monitor, it can be: `Monitoring`, `Idle`, or `Disabled`.
  - `Monitoring` : this means that the AI is actively running and analyzing the webcam images
  - `Idle` : this means the AI is turned on but not actively observing anything.
  - `Disabled` : this means the AI is turned off

`Sensitivity` : this is the current sensitivity of the AI set by the user.  It can be three values:
  - `Fast (3 minutes)` : it takes ~3 minutes of consistent positive detections for an action to occur
  - `Medium (6 minutes)` : it takes ~6 minutes of consistent positive detections for an action to occur
  - `Long (12 minutes)` : it takes ~12 minutes of consistent positive detections for an action to occur

`Notification` : if notifications are enabled by the user

`Pausing` : if pausing the print is enabled by the user

`Defect Level` : the current moving average of the defect level detected by the AI
  - this value is `0-100`
  - it is a moving average value of the last `16/32/64` detections
    - if `Sensitivity` = `Fast (3 minutes` the last 16 detections are used for the average
    - if `Sensitivity` = `Medium (6 minutes` the last 32 detections are used for the average
    - if `Sensitivity` = `Fast (12 minutes` the last 64 detections are used for the average
  - Equation for the moving average is:
    
![image](https://github.com/printpal-io/MATTERSHAPER_BUILD/assets/95444610/71c81249-24a7-4a2a-9ce8-55b52d0b47e7)

## Navigate to the settings
Visit the settings page from the top navigation bar of the Mainsail UI and navigate to the `AI` sidebar option:

![image](https://github.com/printpal-io/MATTERSHAPER_BUILD/assets/95444610/7900e481-477e-48a9-a4a9-d232eb88548e)

The user can change the settings on this page and then must click `SAVE`.

If this is your first time using the plugin, follow our [configuration guide](https://docs.printpal.io/hardware-configuration/HARDWARE_CONFIGURATION_GUIDE/) for configuring your camera's settings, location, and the lighting.

## Development
Develop a custom integration with the AI backend by using the [REST API documentation](https://github.com/printpal-io/PrintWatchAI_Backend/wiki/REST-API) found on this repository.
