import pymongo


def addQuizAdmin(details):
    try:
        client = pymongo.MongoClient("mongodb://quizDB:quizDB@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["quizAdmins"]
        record = {"name":details[0],"username":details[1],"password":details[2],"email":details[3]}
        col.insert_one(record)
        return True
    except Exception as err:
        print(err)
        return False
def verifyUsername(username):
    try:
        client = pymongo.MongoClient("mongodb://quizDB:quizDB@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["quizAdmins"]
        query = {"username":username}
        res = col.find(query)   
        for x in res:
            return [True,x["password"]]
        else:
            return [False,None]
    except Exception as err:
        print(err)
        return [False,None]
if __name__=="__main__":
    admins = db.quizAdmins
    print(list(admins.find()))

