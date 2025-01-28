from ..client import Client

class Ping:
    def __init__(self,client:Client):
        
        self.__client = client

    def fireApi(self):
        respond = self.__client.get_sync_httpx_client().request(
            method="get",
            url="/ping",
            
        )
        return respond
    
    async def fireAsyncApi(self):
        respond = await self.__client.get_async_httpx_client().request(
            method="get",
            url="/ping",
            
        )
        return respond