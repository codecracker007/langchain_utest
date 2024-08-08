import pymongo

def insertIntoQuestionsU(cursorU,collectionU):
    idU = cursorU.sahasra_questions.question_bank.insert_one(dict(collectionU))
    return str(idU.inserted_id)

def CheckifEmailPresent(cursorU,collectionU):
    print(collectionU)
    idu = cursorU.sahasra_users.users.find_one({"email":collectionU})
    if idu:
        print(idu)
        return str(idu["email"])
    return False

