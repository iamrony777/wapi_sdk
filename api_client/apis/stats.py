from ..client import Client

class GetSetupV1Api:
    def __init__(self,client:Client):
        
        self.__client = client

    def fireApi(self):
        respond = self.__client.get_sync_httpx_client().request(
            method="get",
            url="/stats",
            
        )
        return respond
    
    async def fireAsyncApi(self):
        respond =await self.__client.get_async_httpx_client().request(
            method="get",
            url="/stats",
            
        )
        return respond