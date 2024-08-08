from langchain.schema import Document
from fastapi import FastAPI,Request,Response,Depends,HTTPException
from fastapi.responses import JSONResponse
from controllers.u_controllers import UploadUGVector,getUtweet,getUanswer,getUtranslate,UploadUGImageUUrl,getUimageuurl,AssessUContent,InsertQuestionU,loginU,registerU,forgotPasswordU,updatePasswordU,beforeRegisterU
from models.u_models import uTweet,uAnswer,ucorrect,QuestionUmodel,loginUmodel,registerUmodel,ForgotPasswordUmodel,confirmRegisterUmodel
import jwt

app = FastAPI()

def auth_middleware(request:Request):
	token = request.headers.get("session")
	if not token:
		raise HTTPException(status_code=401, detail="No Session Found")
	try:
		jwt.decode(jwt=token,key="SECRET_UG",algorithms=["HS256"])
	except Exception as e:
		print(e)
		raise HTTPException(status_code=401, detail="No Session Found")




@app.post("/login",response_class=JSONResponse)
def ulogin(ubody:loginUmodel,request:Request,response:Response):
	if type(ubody.username) != str or type(ubody.password) != str:
		return "Username and password Must be of type string"
	if loginU(ubody.username,ubody.password):
		try:
			token = jwt.encode(payload={"user":ubody.username},key="SECRET_UG",algorithm="HS256")
			response.set_cookie("session",token)
		except Exception as e:
			print(e)
			return JSONResponse(content={"Message":"Something Went Wrong"},status_code=400)
	else:
		return JSONResponse(content={"Message":"Incorrect Username Or Password"},status_code=400)

			

			
@app.post("/forgotpassword",response_class=JSONResponse)
def uForgotPassword(ubody:ForgotPasswordUmodel):
	print(type(ubody.email))
	if type(ubody.email) != str:
		return JSONResponse(content={"Message":"email must be a string"},status_code=400)
	status ,status_code= forgotPasswordU(ubody)
	JSONResponse(content={"Message":status},status_code=status_code)

@app.get("/updatepassword",response_class=JSONResponse)
def uResetPassword(password: str = "",token : str=""):
	if password and token:
		resu = updatePasswordU(password,token)
		JSONResponse(content={"Message":resu},status_code=200)
	if password and not token:
		JSONResponse(content={"Message":"Provide a token"},status_code=400)
	if not password and token:
		JSONResponse(content={"Message":"Provide A new Password"},status_code=400)
	JSONResponse(content={"Message":"Provide a username and a password"},status_code=400)




@app.post("/getotp")
def uRegister(ubody:registerUmodel):
	resu,status_code = beforeRegisterU(ubody)
	return JSONResponse(content={"Message":resu},status_code=status_code)





@app.post("/register")
def uconfirmRegister(ubody:confirmRegisterUmodel):
	resu = registerU(ubody)
	return {"STATUS":resu}














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
	print(u_answerGenerated)
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


