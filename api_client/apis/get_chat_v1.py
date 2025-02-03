from ..client import Client
from ..models.validation import IdValidation,FromNumberValidation

class GetChatV1Api:
    def __init__(self,id,from_,client:Client):
        self.__id = IdValidation(id=id)
        self.__client = client
        self.__from = FromNumberValidation(from_=from_)

    def fireApi(self):
        respond = self.__client.get_sync_auth_httpx_client().request(
            method="get",
            url="/api/v1/chat",
            params={
                "id":self.__id.id,
                "from":self.__from.from_
            }
        )
        return respond
    async def fireAsyncApi(self):
        respond = await self.__client.get_async_httpx_client().request(
            method="get",
            url="/api/v1/chat",
            params={
            "id":self.__id.id,
            "from":self.__from.from_
            }
        )
        # print(respond.status_code)
        return respond