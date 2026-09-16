import tkinter as tk
from PIL import Image, ImageTk
#======INITIATE SCREEN======
root=tk.Tk(screenName="עושים טוב",baseName="עושים טוב",className="Tk",useTk=True)
root.title("עושים טוב")
root.configure(bg="#FFD6E8")
root.geometry("350x600")
photo = Image.open("logo.png")
resized_image = photo.resize((350, 300), Image.Resampling.LANCZOS)
logo=tk_image = ImageTk.PhotoImage(resized_image)
LOGO_LABEL=tk.Label(root, image=logo,bg="#FFD6E8")
LOGO_LABEL.place(x=0,y=300)

#========FIRST SCREEN======
title_label=tk.Label(root, text="Login to profile:", font=("Courier", 18),bg="#FFD6E8")
title_label.place(x=50,y=20)

username_label=tk.Label(root, text="Username:", font=("Ariel", 10),bg="#FFD6E8")
username_label.place(x=50,y=200)

entry1 = tk.Entry(root)
entry1.place(x=130,y=200)

login_button=tk.Button(root, text="Login")
login_button.place(x=110,y=230)
dont_have_user=tk.Label(root, text="Don't Have A user?", font=("Ariel", 10),bg="#FFD6E8")
creat_user=tk.Button(root, text="signup")
creat_user.place(x=160,y=230)


root.mainloop()



