import pymongo
import datetime
import bson
import rstr
import re
from creds import dbname,dbpass
def addQuizAdmin(details):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["quizAdmins"]
        record = {"name":details[0],"username":details[1],"password":details[2],"email":details[3],"isActive":False}
        col.insert_one(record)
        return True
    except Exception as err:
        print(err)
        return False
def login(username):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["quizAdmins"]
        query = {"username":username}
        res = col.find(query)
        for x in res:
            y = x
        if(y["isActive"]):
            return True
        new = {"$set":{"isActive":True}}
        col.update_one(query,new)   
        return False
    except Exception as err:
        print(err)
        return False
def logOut(username,status = False):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["quizAdmins"]
        query = {"username":username}
        new = {"$set":{"isActive":status}}
        col.update_one(query,new)   
        return True
    except Exception as err:
        print(err)
        return False
def verifyUsername(username):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
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
def checkEmailAvaibility(email):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["quizAdmins"]
        query = {"email":email}
        res = col.find(query)   
        for x in res:
            return False
        else:
            return True
    except Exception as err:
        print(err)
        return None
def checkSessionCode(a):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["sessions"]
        query = {"session_code":a}
        res = col.find(query)   
        for x in res:
            print(x)
            return False
        else:
            return True
    except Exception as err:
        print(err)
        return True
def publishQuiz(questions,nickname,duration,username,start=None,end=None):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["sessions"]
        a = rstr.xeger(r'[A-Z]\d[A-Z]\d-[A-Z]\d[A-Z]\d')
        while(checkSessionCode(a)==False):
            a = rstr.xeger(r'[A-Z]\d[A-Z]\d-[A-Z]\d[A-Z]\d')
        session_code = a
        session_nickname = nickname
        try:
            duration = int(duration)
        except:
            duration = 10
        status = False
        invites = {}
        session_owner = username
        ques = {}
        total = 0
        for x in questions.values():
            qid = str(bson.ObjectId())
            d = {}
            d["question"]=x["question"]
            d["score"]=x["score"]
            try:
                d["score"]=int(d["score"])
            except:
                d["score"]=1
            total+=d["score"]
            options = {}
            ansindx = x["answer"][0]
            for k,val in x["options"].items():
                optid = str(bson.ObjectId())
                options[optid]=val
                if(k==ansindx):
                    try:
                        d["answer"].append(optid)
                    except:
                        d["answer"]=[optid]
            d["options"]=options
            d["isMul"]=False
            ques[qid]=d
        record = {"session_code":session_code,"session_owner":session_owner,"session_nickname":session_nickname,"session_start":start,"session_end":end,"duration":duration,"questions":ques,"status":status,"participants":{},"isRestricted":False,"invites":{},"total_score":total}
        col.insert_one(record)
        return [True,session_code]
    except Exception as err:
        print(err)
        return [False,None]
def verifySessionCode(code):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["sessions"]
        query = {"session_code":code}
        res = col.find(query)   
        for x in res:
            return [True,x]
        else:
            return [False,None]
    except Exception as err:
        print(err)
        return [None,None]
def addParticipant(session_code,participantName,completionStatus=False,score=-1):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["sessions"]
        query = {"session_code":session_code}
        res = col.find(query)
        for y in res:
            x = y["participants"]
        pcode = str(bson.ObjectId())
        x[pcode]={"participantName":participantName,"completionStatus":completionStatus,"score":score}
        new = {"$set":{"participants":x}}
        col.update_one(query,new)   
        return pcode
    except Exception as err:
        print(err)
        return None
def updateParticipant(session_code,pcode,completionStatus=False,score=-1):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        col = db["sessions"]
        query = {"session_code":session_code}
        res = col.find(query)
        for y in res:
            x = y["participants"]
        x[pcode]["completionStatus"]=completionStatus
        x[pcode]["score"]=score
        new = {"$set":{"participants":x}}
        col.update_one(query,new)   
        return True
    except Exception as err:
        print(err)
        return False
def getAllSessions(username,active=False):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        sessions = db["sessions"]
        curtime = datetime.datetime.now()
        query = {"session_owner":username}
        res = sessions.find(query)
        ret = {}
        for x in res:
            if(active):
                start = x["session_start"]
                end = x["session_end"]
                if(start==None or end==None):
                    pass
                elif(curtime>=end or curtime<start):
                    continue
            ret[x["session_code"]]={"session_nickname":x["session_nickname"],"duration":x["duration"],"session_start":x["session_start"],"session_end":x["session_end"],"questions":x["questions"],"participants":x["participants"],"total_score":x["total_score"]}
        return ret
    except Exception as err:
        print(err)
        return None
def getSessionInfo(session_code):
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        sessions = db["sessions"]
        query = {"session_code":session_code}
        res = sessions.find(query)
        ret = {}
        for x in res:
            return {"session_nickname":x["session_nickname"],"duration":x["duration"],"session_start":x["session_start"],"session_end":x["session_end"],"questions":x["questions"],"participants":x["participants"],"total_score":x["total_score"]}
    except Exception as err:
        print(err)
        return None
if __name__=="__main__":
    try:
        client = pymongo.MongoClient(f"mongodb://{dbname}:{dbpass}@cluster0-shard-00-00.jk81v.mongodb.net:27017,cluster0-shard-00-01.jk81v.mongodb.net:27017,cluster0-shard-00-02.jk81v.mongodb.net:27017/?ssl=true&replicaSet=atlas-rms0md-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('quiz')
        sessions = db["sessions"]
        curtime = datetime.datetime.now()
        query = {"session_owner":"test@123"}
        res = sessions.find(query)
    except pymongo.errors.ConnectionFailure:
        print("No internet")
            
    