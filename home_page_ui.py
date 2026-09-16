import tkinter as tk
from PIL import Image, ImageTk

#======INITIATE SCREEN=======
root=tk.Tk(screenName="עושים טוב",baseName="עושים טוב",className="Tk",useTk=True)
root.title("עושים טוב")
root.configure(bg="#85B6C0")
root.geometry("350x600")

#======GET EVENT INFO========


#======HOME PAGE=============
photo = Image.open("small_logo.png")
resized_image = photo.resize((150, 100), Image.Resampling.LANCZOS)
logo=tk_image = ImageTk.PhotoImage(resized_image)
LOGO_LABEL=tk.Label(root, image=logo,bg="#85B6C0")
LOGO_LABEL.place(x=90,y=0)

name_label = tk.Label(root, text="Name of the event:", font=("Ariel", 10),bg="#85B6C0")
name_label.place(x=50,y=100)

desc_label = tk.Label(root, text="Event description:", font=("Ariel", 10),bg="#85B6C0")
desc_label.place(x=55,y=120)

date_label = tk.Label(root, text="Date and time:", font=("Ariel", 10),bg="#85B6C0")
date_label.place(x=73,y=140)

city_label = tk.Label(root, text="City:", font=("Ariel", 10),bg="#85B6C0")
city_label.place(x=130,y=160)

num_of_par_label = tk.Label(root, text="Number of participants:", font=("Ariel", 10),bg="#85B6C0")
num_of_par_label.place(x=25,y=180)

accept_button=tk.Button(root, text="Accept")
accept_button.place(x=180,y=210)

deny_button=tk.Button(root, text="Deny")
deny_button.place(x=120,y=210)

root.mainloop()