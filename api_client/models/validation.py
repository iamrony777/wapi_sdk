from pydantic import BaseModel, Field

class IdValidation(BaseModel):
    id:str = Field(...,min_length=11,max_length=13, description="User id is phone number including country code")
    
class FromNumberValidation(BaseModel):
    from_:str = Field(...,min_length=11,max_length=13, description="User id is phone number including country code")
    