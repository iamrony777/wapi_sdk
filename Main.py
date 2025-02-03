from api_client.client import Client
from api_client.apis.get_chat_v1 import GetChatV1Api
from api_client.apis.get_setup_v1 import GetSetupV1Api
from api_client.apis.get_check_v1 import GetCheckV1Api
from api_client.apis.get_status_v1 import GetStatusV1Api
from api_client.apis.delete_remove_v1 import DeleteRemoveV1Api
from api_client.apis.post_send_v1 import PostSendV1Api
from api_client.models.send_body import SendBody
from api_client.apis.ping import Ping
from Db_client.db_logging import DBLogging
import asyncio
import threading

async def main():
    # client = Client(base_url="https://wapi.ffstudios.io/")
    # # response = await client.get_async_httpx_client().request(
    # #     method="get",
    # #     url="/api/v1/setup",
    # #     params={
    # #         "id":"917385043889"
    # #     }
    # # )
    # # print(response.content)
    # # print("After the await")
    # setupApi = GetSetupV1Api(id="917385043889",client=client)
    # response = await setupApi.fireAsyncApi()
    # # response = setupApi.fireApi()
    # print("SEtup"+str(response.status_code))
    
    # chatApi = GetChatV1Api(id="917385043889",from_="917620146844",client=client)
    # response1 = await chatApi.fireAsyncApi()
   
    # print("chat"+str(response1.content))
    
    # checkApi = GetCheckV1Api(id="917385043889",client=client)
    # response2 = await checkApi.fireAsyncApi()
    # print("check "+ str(response2.status_code))
    
    # statusApi = GetStatusV1Api(id="917385043889",client=client)
    # response3 = await statusApi.fireAsyncApi()
    # print("status "+ str(response3.status_code))
    
    # removeApi = DeleteRemoveV1Api(id="9173845043889",client=client)
    # response4 = await removeApi.fireAsyncApi()
    # print("remove "+str(response4.status_code))
    
    # sendBodeTest= SendBody(id="917385043889",to="917385043889")
    # sendApi = PostSendV1Api(sendBody=sendBodeTest,client=client)
    # response5 = await sendApi.fireAsyncApi()
    # print("sendResponse" +str(response5.status_code))
    
    whatsAppApiImplementation = WhatsappApi(owner_number="917385043889",user_agent="91")
    
    send_response= await whatsAppApiImplementation.send(send_body=SendBody(id='917385043889',to='917385043889',text='Hi Bro'))
    print(send_response)
    
    # chat_response = await whatsAppApiImplementation.get_chats(number='917385043889',number_from='917305582123')
    # print(chat_response)
    
    # check_response= await whatsAppApiImplementation.check_number(number='917385043889')
    # print(check_response)
    
    # setup_response= await whatsAppApiImplementation.setup_owner()
    # print(setup_response)
    
    # status_response= await whatsAppApiImplementation.get_status(number='917385043889')
    # print(check_response)   
    
    # ping_server = await whatsAppApiImplementation.ping_server()
    # print(ping_server) 
    
    
class WhatsappApi:
    def __init__(self,owner_number:str,user_agent:str):
        self.__owner = owner_number
        self.__user_agent = user_agent
        self.__client = Client(base_url="https://wapi.ffstudios.io/",authentication_key="")
        
        
    async def send(self,send_body:SendBody):
        sendApi = PostSendV1Api(client=self.__client, sendBody=send_body)
        send_response = await sendApi.fireAsyncApi()
        api_id = DBLogging.addLog(method='send',id=send_body.id,to=send_body.to,response_code=send_response.status_code)
        DBLogging.addMessage(api_id=api_id,sender_id=send_body.id,to=send_body.to,text=send_body.text,image=send_body.image,video=send_body.image,gifPlayback=send_body.gifPlayback)
        return send_response.status_code
    
    async def get_chats(self,number,number_from):
        chatApi = GetChatV1Api(id=number,from_=number_from,client=self.__client)
        chat_response = await chatApi.fireAsyncApi()
        DBLogging.addLog(method='chats',id=number,from_ = number_from,response_code=chat_response.status_code)
        return chat_response.status_code
    
    async def check_number(self, number):
        checkApi = GetCheckV1Api(id=number,client=self.__client)
        check_response = await checkApi.fireAsyncApi()
        DBLogging.addLog(method='check',id=number,response_code=check_response.status_code)
        return check_response.status_code
    
    async def setup_owner(self):
        setupApi = GetSetupV1Api(id=self.__owner,client=self.__client)
        setup_response = await setupApi.fireAsyncApi()
        DBLogging.addLog(method='setup',id=self.__owner,response_code=setup_response.status_code)
        return setup_response.status_code
    
    async def get_status (self,number):
        statusApi = GetStatusV1Api(id=number,client=self.__client)
        status_response = await statusApi.fireAsyncApi()
        DBLogging.addLog(method='status',id=number,response_code=status_response.status_code)
        return status_response.status_code
    
    async def ping_server(self):
        pingApi = Ping(client=self.__client)
        ping_response = await pingApi.fireAsyncApi()
        DBLogging.addLog(method='ping',id=self.__owner,response_code=ping_response.status_code)
        return ping_response.status_code
        

asyncio.run(main())