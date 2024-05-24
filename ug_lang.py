from langchain.schema import Document
from fastapi import FastAPI
from controllers.u_controllers import UploadUGVector,getUtweet,getUanswer,getUtranslate,UploadUGImageUUrl,getUimageuurl,AssessUContent
from models.u_models import uTweet,uAnswer,ucorrect
app = FastAPI()


'''@app.post("/login")
def ulogin(ubody:loginUmodel):
	if type(ubody.username) != 'string' or type(ubody.password) != 'string':
		return "Username and password Must be of type string"



	
@app.post("/register")
def uregister(ubody:registerUmodel):'''





@app.get("/uFetchuUimageurl")
def ufetch_uimageuurl(ucontext: str = ""):
	uuimageurl = getUimageuurl(ucontext)
	return uuimageurl


@app.get("/api/uUploadVector")
def split_lang():
		try:
			doc_ucontent = UploadUGVector("newu.txt")
			return {"success_code":1}
		except Exception as e:
			print(e)
			return {"success_code":0}


@app.get("/api/uUploadImageuUrl")
def split_uimageurl():
	doc_ucontent = UploadUGImageUUrl("uimageuurl.txt")
	return doc_ucontent


@app.post("/api/utweet")
def get_utweet(body: uTweet):
	try:
		message = body.tweet
		u_tweetGenerated = getUtweet(message)
		return {"uGEN":u_tweetGenerated}
	except Exception as e:
		print(e)
		return {"uGEN":"ERROR"}

@app.post("/api/uanswer")
def get_uanswer(body: uAnswer):
	question = body.question
	print(question)
	u_answerGenerated = AssessUContent(question)
	return {"UGEN":str(u_answerGenerated)}

@app.post("/api/utranslate")
def get_utranslate(body: ucorrect):
	try:
		ugrammar = body.ucgrammar
		u_translateGenerated = getUtranslate(ugrammar)
		return {"UGEN":u_translateGenerated}
	except Exception as e:
		print(e)
		return {"uGEN":"ERROR"}


