import tkinter as tk
from PIL import Image, ImageTk
import firebasethings as fire
root=tk.Tk(screenName="עושים טוב",baseName="עושים טוב",className="Tk",useTk=True)
root.title("עושים טוב")
root.configure(bg="#85B6C0")
root.geometry("350x600")
photo = Image.open("logo.png")
resized_image = photo.resize((350, 300), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(resized_image)

def creat_homepage():
    homepage_label = tk.Label(root, text="HomePage", font=("Helvetica", 10), bg="#85B6C0")
    homepage_label.place(x=140, y=100)
    request_button = tk.Button(root, text="request")
    request_button.place(x=145, y=300)

    swipe_button = tk.Button(root, text="swipe")
    swipe_button.place(x=145, y=400)

    profile_button = tk.Button(root, text="profile")
    profile_button.place(x=145, y=500)


def click(entry):
    user_text = entry.get()
    return user_text


def signup_screen(login_frame):
    login_frame.destroy()
    signup_frame = tk.Frame(root, bg="#85B6C0")
    signup_frame.pack(fill="both", expand=True)
    title_label_signup = tk.Label(signup_frame, text="open a profile:", font=("Courier", 18), bg="#85B6C0")
    title_label_signup.place(x=50, y=20)
    title_label_signup.place(x=50, y=20)
    put_logo(signup_frame)

    new_username_label = tk.Label(signup_frame, text="enter a username:", bg="#85B6C0",font=("Ariel", 10))
    new_username_label.place(x=30, y=250)
    mail_label= tk.Label(signup_frame, text="enter your email:", bg="#85B6C0",font=("Ariel", 10))
    mail_label.place(x=30, y=200)

    fill_mail=tk.Entry(signup_frame)
    fill_user_name= tk.Entry(signup_frame)

    fill_mail.place(x=150, y=200)
    fill_user_name.place(x=150, y=250)

    open_account_button=tk.Button(signup_frame ,text="open account",font=("Ariel", 10),command=lambda: if_user_exist(click(fill_user_name),click(fill_mail),signup_frame))


    open_account_button.place(x=50,y=280)
    have_an_account=tk.Button(signup_frame, text="already have an account? login", font=("Ariel", 10), command=lambda : back_to_login(
        signup_frame))
    have_an_account.place(x=160,y=280)

def back_to_login(frame):
    frame.destroy()
    login_screen()


def login_screen():
    login_frame = tk.Frame(root, bg="#85B6C0")
    login_frame.pack(fill="both", expand=True)
    title_label = tk.Label(login_frame, text="Login to profile:", font=("Courier", 18), bg="#85B6C0")
    title_label.place(x=50, y=20)
    put_logo(login_frame)
    username_label = tk.Label(login_frame, text="Username:", font=("Ariel", 10), bg="#85B6C0")
    username_label.place(x=50, y=200)

    entry1 = tk.Entry(login_frame)
    entry1.place(x=130, y=200)


    login_button = tk.Button(login_frame, text="Login",command=lambda : if_login(click(entry1),login_frame))
    login_button.place(x=110, y=230)
    creat_user = tk.Button(login_frame, text="signup", command=lambda: signup_screen(login_frame))
    creat_user.place(x=160, y=230)



def put_logo(frame):
    logo_label = tk.Label(frame, image=logo, bg="#85B6C0")
    logo_label.place(x=0, y=300)



def if_login(username_input,frame):
    print(username_input)
    if fire.sign_in(username_input):
        frame.destroy()
        creat_homepage()
    else:
        error_label= tk.Label(frame,text="wrong or not existed usrename!",font=("Ariel", 10, "bold"),bg="#85B6C0")
        error_label.place(x=50,y=260)

def if_user_exist(username_input,mail,frame):
    if fire.sign_up(username_input,mail):
        success_label= tk.Label(frame,text="sign up successfully go back to login!")
        success_label.place(x=50,y=260)
    else:
        error_label = tk.Label(frame, text="already registered!", font=("Ariel", 10, "bold"), bg="#85B6C0")
        error_label.place(x=50, y=260)




login_screen()
root.mainloop()



