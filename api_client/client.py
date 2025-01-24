import httpx

class Client:
    
    def __init__(
            self,
            base_url,
            authentication_key=None,
            ):
        self.__base_url = base_url
        self.__client = None
        if(authentication_key):
            self.__authentication_key = authentication_key
            self.__is_authenticated = True

    def get_sync_httpx_client(
            self
            ) -> httpx.Client:
        if self.__client is None:
            self.__client = httpx.Client(
                base_url = self.__base_url,

            )
        return self.__client
    
    def get_async_httpx_client(
            self
    )->httpx.Client:
        if self.__client is None:
            self.__client = httpx.AsyncClient(
                base_url=self.__base_url
            )
        return self.__client
    
   
    def get_sync_auth_httpx_client(
            self
            ) -> httpx.Client:
        if self.__client is None:
            self.__client = httpx.Client(
                base_url = self.__base_url,
                headers={
                    "x-whatsapi-key":self.__authentication_key
                }
            )
        return self.__client
    
    def get_async_auth_httpx_client(
            self
    )->httpx.Client:
        if self.__client is None:
            self.__client = httpx.AsyncClient(
                base_url=self.__base_url,
                headers={
                    "x-whatsapi-key":self.__authentication_key
                }
            )
        return self.__client 
    
    
    async def __aenter__(self) -> "Client":
        await self.get_async_httpx_client.__aenter__()
        return self

    async def __aexit__(self) :
        print("Closing client")
        await self.get_async_httpx_client.__aexit__()