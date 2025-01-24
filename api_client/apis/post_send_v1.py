from ..client import Client

class PostSendV1Api:
    def __init__(self,sendBody,client:Client):
        self.__sendBody = sendBody
        self.__client = client

    def fireApi(self):
        respond = self.__client.get_sync_auth_httpx_client().request(
            method="post",
            url="/api/v1/remove",
            params=self.__sendBody
        )
        return respond
    async def fireAsyncApi(self):
        respond = await self.__client.get_async_httpx_client().request(
            method="post",
            url="/api/v1/remove",
            params=self.__sendBody
        )
        return respond