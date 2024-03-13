import tkinter as tk
from tkinter import messagebox

class authentication():
    def __init__(self,root):
        self.root=root
        
        self.root.title("User Authentication Management System")
        
        self.frame1=tk.Frame(self.root, width=30, height=30)
        self.frame1.pack(side=tk.LEFT)
        
        self.frame2= tk.Frame(self.root, width=50, height=30)
        self.frame2.pack(side=tk.RIGHT)
        
        self.name=tk.Label(self.frame1, text="User Name:")
        self.name.pack(side=tk.TOP,padx=10, pady=5)
        self.nameIn=tk.Entry(self.frame1)
        self.nameIn.pack(side=tk.TOP, pady=7,padx=10)
        
        self.code=tk.Label(self.frame1, text="Password:")
        self.code.pack(side=tk.TOP, pady=10, padx=10)
        self.codeIn=tk.Entry(self.frame1)
        self.codeIn.pack(side=tk.TOP, pady=12, padx=10)
        
        self.button=tk.Button(self.frame1, text="Sign In", command=self.signIn)
        self.button.pack(side=tk.TOP, padx=10, pady=15)
        
        self.list=tk.Listbox(self.frame2, bg="sky blue",font=("Arial",14), width=60, height=30)
        self.list.pack(side=tk.RIGHT)
        
        self.users=[
            {"Name":"david", "Code":"david123"},
            {"Name":"john", "Code":"john123"},
            {"Name":"peter", "Code":"peter123"}
        ] 
        self.tries=3  
    def signIn(self):
        userName=self.nameIn.get()
        userCode=self.codeIn.get()
        found=False
        
        for i in self.users:
            if userName==i["Name"] and userCode==i["Code"]:
                found=True
                wlcm=f"Welcome Mr.{userName}"
                self.list.insert(tk.END, wlcm)
                self.clear()
                break
                
            
        if not found:
            self.tries -=1
            if self.tries > 0:
                chance=f"Try again! You will be blocked after {self.tries} tries"
                self.list.insert(tk.END, chance)
                self.clear() 
            else:
                tk.messagebox.showerror("Block", "You Are Blocked!")
                self.root.destroy()
                
    def clear(self):
        self.nameIn.delete(0,tk.END)
        self.codeIn.delete(0,tk.END)            
        
        
        
root=tk.Tk()
ob=authentication(root)
root.mainloop()