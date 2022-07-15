import pymongo
import datetime

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
    client = pymongo.MongoClient("mongodb://quizDB:quizDB@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('quiz')
    sessions = db["sessions"]
    myquery = { "session_owner": "test@123"}
    newvalues = { "$set": { "session_start": datetime.datetime(year=2022, month=7, day=15,hour=23,minute=30) ,"session_end":datetime.datetime(year=2022, month=7, day=16,hour=10,minute=30) }}

    sessions.update_one(myquery, newvalues)
    for x in sessions.find(myquery):
        print(x)
