from api_client.client import Client
from api_client.apis.get_chat_v1 import GetChatV1Api
from api_client.apis.get_setup_v1 import GetSetupV1Api
from api_client.apis.get_check_v1 import GetCheckV1Api
from api_client.apis.get_status_v1 import GetStatusV1Api
from api_client.apis.delete_remove_v1 import DeleteRemoveV1Api
from api_client.apis.post_send_v1 import PostSendV1Api
import asyncio
import threading

async def main():
    client = Client(base_url="https://wapi.ffstudios.io/")
    # response = await client.get_async_httpx_client().request(
    #     method="get",
    #     url="/api/v1/setup",
    #     params={
    #         "id":"917385043889"
    #     }
    # )
    # print(response.content)
    # print("After the await")
    setupApi = GetSetupV1Api(id="917385043889",client=client)
    response = await setupApi.fireAsyncApi()
    # response = setupApi.fireApi()
    print("SEtup"+str(response.status_code))
    
    chatApi = GetChatV1Api(id="917385043889",from_="917620146844",client=client)
    response1 = await chatApi.fireAsyncApi()
   
    print("chat"+str(response1.content))
    
    checkApi = GetCheckV1Api(id="917385043889",client=client)
    response2 = await checkApi.fireAsyncApi()
    print("check "+ str(response2.status_code))
    
    statusApi = GetStatusV1Api(id="917385043889",client=client)
    response3 = await statusApi.fireAsyncApi()
    print("status "+ str(response3.status_code))
    
    removeApi = DeleteRemoveV1Api(id="9173845043889",client=client)
    response4 = await removeApi.fireAsyncApi()
    print("remove "+str(response4.status_code))
    
    
    
    

asyncio.run(main())