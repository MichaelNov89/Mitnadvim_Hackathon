import tkinter as tk
#======INITIATE SCREEN======
root=tk.Tk(screenName="עושים טוב",baseName="עושים טוב",className="Tk",useTk=1)
root.title("עושים טוב")
root.geometry("350x600")

#========FIRST SCREEN======
tk.Label(root, text="Login to profile:", font=("Courier", 18)).grid(row=0, column=1)
tk.Label(root, text="Username:", font=("Ariel", 10)).grid(row=30, column=0)
tk.Label(root, text="Password:", font=("Ariel", 10)).grid(row=31, column=0)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=20, column=1)
entry2.grid(row=21, column=1)
tk.Button(root, text="Login").grid(row=6, column=1, columnspan=2)


root.mainloop()



