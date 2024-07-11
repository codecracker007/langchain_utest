from langchain.schema import Document
from fastapi import FastAPI,Request,Response,Depends
from fastapi.responses import JSONResponse
from controllers.u_controllers import UploadUGVector,getUtweet,getUanswer,getUtranslate,UploadUGImageUUrl,getUimageuurl,AssessUContent,InsertQuestionU,loginU,registerU,forgotPasswordU,updatePasswordU
from models.u_models import uTweet,uAnswer,ucorrect,QuestionUmodel,loginUmodel,registerUmodel,ForgotPasswordUmodel
import jwt

app = FastAPI()

def auth_middleware(request:Request):
	token = request.headers.get("session")
	if not token:
		raise HTTPException(status_code=401, detail="No Session Found")
	try:
		jwt.decode(token,"SECRET_UG",algorithms=["HS256"])
	except Exception as e:
		print(e)
		raise HTTPException(status_code=401, detail="No Session Found")




@app.post("/login")
def ulogin(ubody:loginUmodel,request:Request,response:Response):
	if type(ubody.username) != 'string' or type(ubody.password) != 'string':
		return "Username and password Must be of type string"
	if loginU(ubody.username,ubody.password):
		try:
			token = jwt.encode({"user":ubody.username},"SECRET_UG",algorithms=["HS256"])
			response.set_cookie("session",token)
		except Exception as e:
			print(e)
			JSONResponse(content={"ERROR":"Something Went Wrong While Logging In"},status_code=500)

			

			
@app.post("/forgotpasswordU")
def uForgotPassword(ubody:ForgotPasswordUmodel):
	if type(ubody.email) != 'string':
		return "email must be a string"
	status = forgotPasswordU(ubody)
	JSONResponse(context={"STATUS":status},status_code=200)

@app.get("/reset_passwordU")
def uResetPassword(password: str = "",token : str=""):
	if password and token:
		resu = updatePasswordU(password,token)
		JSONResponse(content={"STATUS":resu},status_code=200)
	if password and not token:
		JSONResponse(content={"STATUS":"Provide a token"})
	if not password and token:
		JSONResponse(content={"STATUS":"Provide A new Password"})
	JSONResponse(content={"STATUS":"Provide a username and a password"})




	
@app.post("/register")
def uregister(ubody:registerUmodel):
	try:
		if registerU(ubody):
			JSONResponse(content={"SUCCESS":"User Created"},status_code=200)
		JSONResponse(content={"ERROR":"Username or Email Already Exists"},status_code=400)
	except Exception as e:
		print(e)
		JSONResponse(content={"ERROR":"Something Went Wrong while registering"},status_code=500)















@app.get("/uFetchuUimageurl")
def ufetch_uimageuurl(ucontext: str = ""):
	uuimageurl = getUimageuurl(ucontext)
	return uuimageurl


@app.post("/api/question")
def insQuestion(body:QuestionUmodel):
	try:
		idU = InsertQuestionU(body)
		return {"STATUS":"SUCCESS","insertedID":idU}
	except Exception as e:
		print(e)
		return{"STATUS":"ERROR"}

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
def get_uanswer(body: uAnswer,request:Request):
	question = body.question
	print(question)
	u_answerGenerated = AssessUContent(question,"TESTUG")
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


