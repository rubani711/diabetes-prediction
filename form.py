import tkinter as tk

fields = ('Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age')


def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

root = tk.Tk()
ents = makeform(root, fields)
'''b1 = tk.Button(root, text='Pregnancies',
       command=(lambda e=ents: final_balance(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b2 = tk.Button(root, text='Glucose',
       command=(lambda e=ents: monthly_payment(e)))
b2.pack(side=tk.LEFT, padx=5, pady=5)'''
b3 = tk.Button(root, text='Quit', command=root.quit)
b3.pack(side=tk.LEFT, padx=5, pady=5)
root.mainloop()