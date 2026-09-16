import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Request import Request
from User import User

# 1. Initialize the SDK with your service account credentials
# Replace 'serviceAccountKey.json' with the actual path to your downloaded key
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# 2. Get the Firestore database client
db = firestore.client()

# 3. Test the connection by writing a document
def add_request_to_database(request):
    doc_ref = db.collection('requests').document(request.event_id)
    doc_ref.set({
        "req_name": request.req_name,
        "req_desc": request.req_desc,
        "event_id" : request.event_id,
        "creator_id" : request.creator_id,
        "date" : request.date,
        "time" : request.time,
        "city": request.city,
        "number_of_participants": request.number_of_participants,
        "status": request.status,
        "volunteer_list": request.volunteer_list,
        "is_full" : request.is_full

    })

def add_user_to_database(user):
    doc_ref = db.collection('users').document(user.uid)
    doc_ref.set({
        "uid": user.uid,
        "username": user.username,
        "volunteer_times": user.volunteer_times,
        "rating": user.rating

    })

def read_users_from_database(uid):
    user= db.collection('users').document(uid).get().to_dict()
    print(user)
    return user

def read_requests_from_database(req_id):
    req= db.collection('requests').document(req_id).get().to_dict()
    print(req)
    return req

def check_in_collection():
    doc= db.collection('users').stream()
    return[doc.id for doc in doc]


def get_all_reqs_for_user(uid,city):
    vol_for_user=[]
    doc = db.collection('requests').stream()
    for doc in doc:
        if doc.city == city:
            vol_for_user.append(doc.to_dict())

    print(vol_for_user)
    return vol_for_user





def sign_up():
    username= input("Enter your username: ")
    if check_in_collection().count(username)==0:
        new_user= User(username,username)
        add_user_to_database(new_user)
    else:
        print("Username already in use")

def create_request():
    req_name= input("Enter your request name: ")
    req_desc= input("Enter your request description: ")
    req_people= int(input("Enter your request peole: "))
    req_date=input("Enter your request date: ")
    req_city= input("Enter your request city: ")
    req_time= input("Enter your request time: ")
    new_req= Request(req_name,req_desc,req_people)


def sign_in():
    username= input("Enter your username: ")
    if check_in_collection().count(username)!=0:
        print("Successfully logged in")
    else:
        print("No user")

# Run the test
if __name__ == '__main__':
    req= Request("ufck off","man idk how the fukc do i do this i ma tIred i wnat to idk","1","1","2/3/2","18:00","TelAviv",5)
    user=User("Tal","user11")
    add_user_to_database(user)
    add_request_to_database(req)
    read_users_from_database(user.uid)
    read_requests_from_database(req.event_id)
    sign_up()
    sign_in()
