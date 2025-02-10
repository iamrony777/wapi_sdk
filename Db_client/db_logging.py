# from .db_util import DBConnUtil
from .db_props import DBPropertyUtil
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# conn = DBConnUtil.makeConnection()

DBConnUrl = DBPropertyUtil.getConnUrl()

engine = create_engine(DBConnUrl, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()

class APILogs(Base):
    __tablename__ = 'api_logs'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String,nullable=False)
    user_id = Column(String,nullable=False)
    from_ = Column(Integer)
    to = Column(Integer)
    response_code = Column(Integer,nullable=False)
    
class APIMessages(Base):
    __tablename__ = 'api_messages'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    api_id = Column(Integer, ForeignKey('api_logs.ID'))
    sender_id = Column(String,nullable=False)
    to = Column(String,nullable=False)
    text = Column(String)
    image = Column(String)
    video = Column(String)
    audio = Column(String)
    gifPlayback = Column(Integer)
    
Base.metadata.create_all(bind=engine)

class DBLogging():
    def addLog(method:str,user_id:str,response_code:int,from_=0,to=0):
        # stmt = conn.cursor()
        # stmt.execute(f'insert into api_logs(method,user_id,`from`,`to`,response_code) value (\'{method}\',\'{id}\',\'{from_}\',\'{to}\',{response_code});')
        # conn.commit()
        # stmt.execute(f'select ID from api_logs order by ID DESC limit 1; ')
        # row = stmt.fetchall()
        # id = row[0]
        # return id[0]
        new_log = APILogs(method=method,user_id=user_id,from_=from_,to=to,response_code=response_code)
        session.add(new_log)
        session.commit()
        session.refresh(new_log)
        return new_log.ID
    
    def addMessage(api_id,sender_id,to,text="",image="",video="",audio="",gifPlayback=None):
        # stmt = conn.cursor()
        # stmt.execute(f'insert into api_messages(api_id,sender_id,`to`,text,image,video,audio,gifPlayback) values ({api_id},\'{sender_id}\',\'{to}\',\'{text}\',\'{image}\',\'{video}\',\'{audio}\',{gifPlayback});')
        # conn.commit()
        # return 'Message Logged successfully'   
        new_message = APIMessages(api_id=api_id,sender_id=sender_id,to=to,text=text,image=image,video=video,audio=audio,gifPlayback=gifPlayback)
        session.add(new_message)
        session.commit()
        return 'Message Logged successfully'

#Example Ussage
id= DBLogging.addLog(method='test',user_id='917385043889',response_code=200)
print(id)