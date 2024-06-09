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
class registerUmodel(BaseModel):
	username:str
	password:str
	email:str

class QuestionUmodel(BaseModel):
	Class:str
	subject:str
	topic:str
	subtopic:str
	question:str
	option1:str
	option2:str
	option3:str
	option4:str
	correctanswer:str|None
	level:str
	explaination:str
	image:str
	questionset:str
