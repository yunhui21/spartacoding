from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.8fihl8l.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name':'영수'},{'$set':{'age':19}})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})