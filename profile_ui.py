import tkinter as tk
#======INITIATE SCREEN======
root=tk.Tk(screenName="עושים טוב",baseName="עושים טוב",className="Tk",useTk=True)
root.title("עושים טוב")
root.configure(bg="#FFD6E8")
root.geometry("350x600")

#======PROFILE SCREEN======
title_label = tk.Label(root, text="Profile Screen", font=("Courier", 18), bg="#FFD6E8")
title_label.pack()






root.mainloop()