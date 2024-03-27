from langchain.schema import Document
from fastapi import FastAPI
from controllers.u_controllers import UploadUGVector,getUtweet,getUanswer,getUtranslate
from models.u_models import uTweet,uAnswer,ucorrect
app = FastAPI()


@app.get("/uUploadVector")
def split_lang():
		try:
			doc_ucontent = UploadUGVector("myfile.txt")
			return {"success_code":1}
		except Exception as e:
			print(e)
			return {"success_code":0}



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
	try:
		question = body.question
		u_answerGenerated = getUanswer(question)
		return {"UGEN":u_answerGenerated}
	except Exception as e:
		print(e)
		return {"uGEN":"ERROR"}


@app.post("/api/utranslate")
def get_utranslate(body: ucorrect):
	try:
		ugrammar = body.ucgrammar
		u_translateGenerated = getUtranslate(ugrammar)
		return {"UGEN":u_translateGenerated}
	except Exception as e:
		print(e)
		return {"uGEN":"ERROR"}


