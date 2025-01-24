class SendBody():
    def __init__(self,id,to,text,image,video,audio,gifPlayback):
        self.__id=id
        self.__to = to
        self.__text = text
        self.__image = image
        self.__video= video
        self.__audio = audio
        self.__gifPlayback = gifPlayback

    def getDataDick(self)->dict[str,any]:
        return {
            "id":self.__id,
            "to":self.__to,
            "text":self.__text,
            "image":self.__image,
            "video":self.__video,
            "audio":self.__audio,
            "gifPlayback":self.__gifPlayback
        }