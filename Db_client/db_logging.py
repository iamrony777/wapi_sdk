from .db_util import DBConnUtil

conn = DBConnUtil.makeConnection()

class DBLogging():
    def addLog(method:str,id:str,response_code:int,from_=0,to=0,):
        stmt = conn.cursor()
        stmt.execute(f'insert into api_logs(method,user_id,`from`,`to`,response_code) value (\'{method}\',\'{id}\',\'{from_}\',\'{to}\',{response_code});')
        conn.commit()
        stmt.execute(f'select ID from api_logs order by ID DESC limit 1; ')
        row = stmt.fetchall()
        id = row[0]
        return id[0]
    
    def addMessage(api_id,sender_id,to,text="",image="",video="",audio="",gifPlayback=None):
        stmt = conn.cursor()
        stmt.execute(f'insert into api_messages(api_id,sender_id,`to`,text,image,video,audio,gifPlayback) values ({api_id},\'{sender_id}\',\'{to}\',\'{text}\',\'{image}\',\'{video}\',\'{audio}\',{gifPlayback});')
        conn.commit()
        return 'Message Logged successfully'   

# loggingh = DBLogging()
# id= loggingh.addLog(method='status',id='917385043889')
# print(id)