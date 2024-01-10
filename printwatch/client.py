import datetime
import aiohttp
from uuid import uuid4

class PrintWatchClient():
    '''
    The object that handles API communications with the PrintWatch cloud server
    '''
    def __init__(
            self,
            settings : dict
        ):
        self.route = 'https://octoprint.printpal.io'
        self.settings = settings
        self.ticket_id = ''

    def create_ticket(self) -> None:
        self.ticket_id = uuid4().hex

    def clear_ticket(self) -> None:
        self.ticket_id = ''

    def _create_payload(
            self,
            encoded_image : str = None,
            scores : list = [],
            print_stats : dict = {},
            notify : bool = False,
            heartbeat : bool = False,
            notification_level : str = 'warning',
            settings : dict = {},
            state : int = 0,
            force : bool = True
        ) -> dict:
        '''
        Creates the JSON payload for requests
        being sent to the server.
        '''
        if notify:
            payload = {
                "api_key" : self.settings.get("api_key"),
                "printer_id" : self.settings.get("printer_id"),
                "email_addr" : self.settings.get("email_addr"),
                "printTime" : print_stats.get("print_duration", 550),
                "printTimeLeft" : print_stats.get("print_duration", 550) * ((1/print_stats.get("progress", 1.0)) - 1),
                "progress" : print_stats.get("progress", 0.0),
                "job_name" : print_stats.get("filename", "none"),
                "notification" : notification_level,
                "time" : datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            }
        elif heartbeat:
            payload = {
                'api_key': self.settings.get("api_key"),
                'printer_id' : self.settings.get("printer_id"),
                'state' : state,
                'version' : "1.3.01",
                'ticket_id' : self.ticket_id,
                'force' : force,
            }
            if len(settings) > 0:
                payload["settings"] = {}
                for key, ele in settings.items():
                    payload["settings"][key] = ele
        else:
            if self.ticket_id == '':
                self.create_ticket()

            payload = {
                'api_key' : self.settings.get("api_key"),
                'printer_id' : self.settings.get("printer_id"),
                'ticket_id' : self.ticket_id,
                'version' : '1.3.01',
                'state' : 0,
                'conf' : int(self.settings.get("thresholds", {}).get("display", 0.6) * 100),
                'buffer_length' : self.settings.get("buffer_length"),
                'buffer_percent' : self.settings.get("buffer_percent"),
                'thresholds' : [self.settings.get("thresholds", {}).get("notification", 0.3), self.settings.get("thresholds", {}).get("action", 0.6)],
                'scores' : scores,
                'sma_spaghetti' : self.settings.get("sma", 0.),
                'email_addr' : self.settings.get("email_addr"),
                'enable_feedback_images' : self.settings.get("enable_feedback_images")
            }
            for key, ele in print_stats.items():
                payload[key] = ele

            payload['image_array'] = encoded_image

        return payload


    async def _send_async(
                self,
                endpoint : str,
                payload : dict
            ) -> dict:

            async with aiohttp.ClientSession() as session:
                async with session.post(
                                '{}/{}'.format(self.route, endpoint),
                                json = payload,
                                headers={'User-Agent': 'Mozilla/5.0'},
                                timeout=aiohttp.ClientTimeout(total=30.0)
                            ) as response:
                            r = await response.json()

            self.response = r
            return r
