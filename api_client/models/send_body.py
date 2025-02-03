from pydantic import BaseModel, Field

class SendBody(BaseModel):
    
    id: str = Field(..., min_length=11, max_length=13, description="Sender ID")
    to: str = Field(..., min_length=11, max_length=13, description="Receiver ID")
    text: str = Field(None, description="Text message content (optional)")
    image: str = Field(None, description="Image URL (optional)")
    video: str = Field(None, description="Video URL (optional)")
    audio: str = Field(None, description="Audio URL (optional)")
    gifPlayback: bool = Field(default=False, description="Enable GIF autoplay (optional)")

    def get_data_dict(self) -> dict[str, any]:
        return self.model_dump()
