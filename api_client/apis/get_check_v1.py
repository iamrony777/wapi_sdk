from ..client import Client
from ..models.validation import IdValidation

class GetCheckV1Api:
    def __init__(self,id,client:Client):
        self.__data = IdValidation(id=id)
        self.__client = client

    def fireApi(self):
        respond = self.__client.get_sync_auth_httpx_client().request(
            method="get",
            url="/api/v1/check",
            params={
                "id":self.__data.id
            }
        )
        return respond
    async def fireAsyncApi(self):
        respond = await self.__client.get_async_httpx_client().request(
            method="get",
            url="/api/v1/check",
            params={
            "id":self.__data.id
            }
        )
        # print(respond.status_code)
        return respond