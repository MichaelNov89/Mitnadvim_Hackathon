import pyrebase
FIREBASE_CONFIG = {
  'apiKey': "AIzaSyDoFHjHEUu2cHbiUMmH-lreQVX0-5y0ZHE",
  'authDomain': "osimtov-7447f.firebaseapp.com",
  'databaseURL': "https://osimtov-7447f-default-rtdb.firebaseio.com/",
  'projectId': "osimtov-7447f",
  'storageBucket': "osimtov-7447f.firebasestorage.app",
  'messagingSenderId': "307969315100",
  'appId': "1:307969315100:web:5af5389cec26687df4aad9",
  'measurementId': "G-20X1XPS5FK"
}


firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
# db = firebase.database()
auth = firebase.auth()
# storage = firebase.storage()
email = input("Enter your email: ")
password = input("Enter your password: ")
try:
    auth.sign_in_with_email_and_password(email, password)
    print("Logged in successfully")
except:
    print("Wrong email or password")











