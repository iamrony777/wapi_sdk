from ..client import Client
from ..models.validation import IdValidation

class GetStatusV1Api:
    def __init__(self,id,client:Client):
        self.__id = IdValidation(id=id)
        self.__client = client

    def fireApi(self):
        respond = self.__client.get_sync_auth_httpx_client().request(
            method="get",
            url="/api/v1/status",
            params={
                "id":self.__id.id
            }
        )
        return respond
    async def fireAsyncApi(self):
        respond = await self.__client.get_async_httpx_client().request(
            method="get",
            url="/api/v1/status",
            params={
            "id":self.__id.id
            }
        )
        return respond