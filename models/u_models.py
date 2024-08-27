from pydantic import BaseModel,RootModel
from typing import List,Dict


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
	email:str

class confirmRegisterUmodel(BaseModel):
	email:str
	username:str
	password:str
	mobilenumber:str
	Class: str
	educationboard: str
	token:str




class ForgotPasswordUmodel(BaseModel):
	username:str
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



class questionAssessUmodel(BaseModel):
	questionid:str
	studentanswer:str


class AssessUmodel(BaseModel):
	d:List[Dict[str,str]]

class ProfileUmodel(BaseModel):
	email:str | None
	username:str | None
	mobilenumber:str | None
	Class: str | None
	educationboard: str | None
	bio: str | None