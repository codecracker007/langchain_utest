import pymongo

def insertIntoQuestionsU(cursorU,collectionU):
    idU = cursorU.sahasra_questions.question_bank.insert_one(dict(collectionU))
    return str(idU.inserted_id)

def CheckifEmailPresent(cursorU,collectionU):
    idu = cursorU.sahasra_users.users.Findone(dict(collectionU))
    if idu:
        return str(idu.email)
    return False

