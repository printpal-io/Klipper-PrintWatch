import PIL.Image as Image
from io import BytesIO
import urllib3
import aiohttp
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests

class MJPEG:
    def __init__(
            self,
            id : str = '',
            ip : str = ''
        ):
        self.id = id
        self.ip = ip
        self.frame = None
        self.cap = None
        self.byte_frame = None
        self.pil_image = None

    async def snap(self) -> bytes:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                            '{}'.format(
                                self.ip
                            ),
                            timeout=aiohttp.ClientTimeout(total=5.0)
                        ) as response:
                        if response.status == 200:
                            self.byte_frame = await response.read()
                            return self.byte_frame
        return False


    def snap_sync(self) -> bytes:
        try:
            r = requests.get(self.ip)
            if r.status_code == 200:
                self.byte_frame = r.content
                return r.content
            return b''
        except Exception as e:
            print(f'Exception with snap: {str(e)}')
            return b''
