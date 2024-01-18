import tkinter as tk
root= tk.Tk()
root.title("MANAGEMENT SYSTEM")


appLabel=tk.Label(root,text="Students's Management system",fg="Blue",width=35)
appLabel.config(font=("sylfaen",30))
appLabel.grid(row=0,columnspan=2,padx=(10,10),pady=(30,0))

nameLabel=tk.Label(root,text="Enter your name:",width=40,anchor='w',font=("sylfaen",12)).grid(row=1,column=0,padx=(10,0),pady=(30,0))

collegeLabel=tk.Label(root,text="Enter your college:",width=40,anchor='w',font=("sylfaen",12)).grid(row=2,column=0,padx=(10,0),pady=(30,0))

phoneLabel=tk.Label(root,text="Enter your phone no:",width=40,anchor='w',font=("sylfaen",12)).grid(row=3,column=0,padx=(10,0),pady=(30,0))

addressLabel=tk.Label(root,text="Enter your address:",width=40,anchor='w',font=("sylfaen",12)).grid(row=4,column=0,padx=(10,0),pady=(30,0))

nameEntry= tk.Entry(root,width=30)
nameEntry.grid(row=1,column=1,padx=(0,10),pady=(30,20))

collegeEntry= tk.Entry(root,width=30)
collegeEntry.grid(row=2,column=1,padx=(0,10),pady=(30,20))

phoneEntry= tk.Entry(root,width=30)
phoneEntry.grid(row=3,column=1,padx=(0,10),pady=(30,20))

addressEntry= tk.Entry(root,width=30)
addressEntry.grid(row=4,column=1,padx=(0,10),pady=(30,20))

button= tk.Button(root,text="Take Input")
button.grid(row=5,column=0,pady= 20)

displayButton=tk.Button(root,text="Display Results")
displayButton.grid(row=5,column=1)




















































root.mainloop()