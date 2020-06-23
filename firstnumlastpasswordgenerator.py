import tkinter as tk
import random
import names

#names.get_full_name()
#names.get_full_name(gender='male')
#names.get_first_name()
#names.get_first_name(gender='female')
#names.get_last_name()

def random_sentence():
    first_names = [names.get_first_name()]
    number = [random.randint(1,100)]
    last = [names.get_last_name()]
    full_sentence = '{}{}{}'.format(names.get_first_name(), random.choice(number), random.choice(last))
    return full_sentence

def update_label_and_entry():
    new_random_sentence = random_sentence()
    label.config(text=new_random_sentence)
    entry.delete(0, tk.END) # delete content from 0 to end
    entry.insert(0, new_random_sentence) # insert new_random_name at position 0

root = tk.Tk()
label = tk.Label(root)
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="New random sentence", command=update_label_and_entry)
button.pack()
root.mainloop()
