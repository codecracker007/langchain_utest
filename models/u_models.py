from pydantic import BaseModel



class uTweet(BaseModel):
	tweet:str

class uAnswer(BaseModel):
	question:str

class ucorrect(BaseModel):
	ucgrammar:dict

class loginUmodel(BaseModel):
	username:str
	password:str
	