import pymongo

def insertIntoQuestionsU(cursorU,collectionU):
    idU = cursorU.sahasra_questions.question_bank.insert_one(dict(collectionU))
    return str(idU.inserted_id)