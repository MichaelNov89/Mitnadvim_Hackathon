
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
        "event_id": request.event_id,
        "creator_id": request.creator_id,
        "date": request.date,
        "time": request.time,
        "city": request.city,
        "number_of_participants": request.number_of_participants,
        "status": request.status,
        "volunteer_list": request.volunteer_list,
        "is_full": request.is_full

    })


def add_user_to_database(user):
    doc_ref = db.collection('users').document(user.uid)
    doc_ref.set({
        "uid": user.uid,
        "username": user.username,
        "mail": user.mail,
        "volunteer_times": user.volunteer_times,
        "vol_list": user.vol_list,
        "created_req_list": user.created_req_list,
        "rating": user.rating

    })


def read_users_from_database(uid):
    user = db.collection('users').document(uid).get().to_dict()
    print(user)
    return user


def read_requests_from_database(req_id):
    req = db.collection('requests').document(req_id).get().to_dict()
    print(req)
    return req


def check_in_collection():
    doc = db.collection('users').stream()
    return [doc.id for doc in doc]


def get_all_reqs_for_user(uid, city):
    vol_for_user = []
    doc = db.collection('requests').stream()
    for doc in doc:
        if doc.city == city:
            vol_for_user.append(doc.to_dict())

    print(vol_for_user)
    return vol_for_user


def get_user(uid):
    doc = db.collection('users').document(uid).get().to_dict()
    return doc


def get_req(req_id):
    doc = db.collection('requests').document(req_id).get().to_dict()
    return doc

def sign_up(username,email):
    global curr_login
    if check_in_collection().count(username) == 0:
        new_user = User(username, username, email)
        add_user_to_database(new_user)
        curr_login=new_user.uid

    else:
        print("Username already in use")


# create a req using from the curr loggin
def create_request():
    user_id = curr_login
    curr_user = get_user(curr_login)
    print(curr_user)
    event_id = user_id + str(len(curr_user["created_req_list"])+1)
    req_name = input("Enter your request name: ")
    req_desc = input("Enter your request description: ")
    req_people = int(input("Enter your request people: "))
    req_date = input("Enter your request date: ")
    req_city = input("Enter your request city: ")
    req_time = input("Enter your request time: ")
    new_req = Request(req_name, req_desc,event_id,user_id, req_time, req_date, req_city,req_people)
    add_request_to_database(new_req)


def sign_in(username):
    global curr_login
    if check_in_collection().count(username) != 0:
        print("Successfully logged in")
        curr_login = username

    else:
        print("No user")


def accept_or_decline_reqs(accepted,req_id):
    if accepted:
        updated_user=get_user(curr_login)
        updated_user['vol_list'].append(req_id)
        db.collection('users').document(curr_login).set(updated_user)
        updated_req=get_req(req_id)
        updated_req["volunteer_list"].append(curr_login)
        db.collection('requests').document(req_id).set(updated_req)





# Run the test
if __name__ == '__main__':
    global curr_login
    curr_login=""
    print(curr_login)
    req = Request("fuck off", "man idk how the fukc do i do this i ma tIred i wnat to idk", "1", "1", "2/3/2", "18:00",
                  "TelAviv", 5)
    user = User("Tal", "Tal","mail@gmail.com")
    print(get_user("Tal"))
    add_user_to_database(user)
    add_request_to_database(req)
    read_users_from_database(user.uid)
    read_requests_from_database(req.event_id)
    sign_in(input("Enter your username to sign in: "))
    print(curr_login)
    accept_or_decline_reqs(True,"Tal0")
    create_request()
