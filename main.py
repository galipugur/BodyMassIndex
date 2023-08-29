import tkinter

backcolor = "light gray"

#window
window = tkinter.Tk()
window.config(bg=backcolor, pady=10)
window.title("Body Mass Index (BMI)")
window.minsize(width=300, height=175)

#labels
class Label_Head():
    def __init__(self, text):
        self.text = text
        my_label = tkinter.Label(text=text)
        my_label.config(pady=10, padx=10, bg=backcolor)
        my_label.pack()

#weight label
weight_label = Label_Head("Enter Your Weight (kg)")

#entry1
weight_entry = tkinter.Entry(width=20)
weight_entry.pack()

#height label
height_label = Label_Head("Enter Your Height (m)")

#entry2
height_entry = tkinter.Entry(width=20)
height_entry.pack()

'''
#you can do 'label' without creating a class like below.
#label1
weight_label = tkinter.Label(text="Enter Your Weight (kg)")
weight_label.config(pady=10, padx=10, bg=backcolor)
weight_label.pack()

#label2
height_label = tkinter.Label(text="Enter Your Height (m)")
height_label.config(padx=10, bg=backcolor)
height_label.pack()
'''

#button
def calculate():
    if len(weight_entry.get()) == 0 or len(height_entry.get()) == 0:
        result_label.config(text="Please Enter Both Weight and Height")
    else:
        try:
            user_weight = float(weight_entry.get())
            user_height = float(height_entry.get()) / 100
            result = float(round(user_weight / (user_height * user_height), 2))

            if result < 18.5:
                result_label.config(text=f"Your BMI is {result}. You are UNDERWEİGHT", bg="light green", fg="black")
            elif result >= 18.5 and result <= 24.9:
                result_label.config(text=f"Your BMI is {result}. You are NORMAL WEİGHT", bg="green", fg="white")
            elif result >= 25.0 and result <= 29.9:
                result_label.config(text=f"Your BMI is {result}. You are OVERWEİGHT", bg="orange", fg="white")
            elif result >= 30.0 and result <= 34.9:
                result_label.config(text=f"Your BMI is {result}. You are OBESITY CLASS 1", bg="red", fg="black")
            elif result >= 35.0 and result <= 39.9:
                result_label.config(text=f"Your BMI is {result}. You are OBESITY CLASS 2", bg="red", fg="black")
            else:
                result_label.config(text=f"Your BMI is {result}. You are OBESITY CLASS 3", bg="dark red", fg="white")
        except:
            result_label.config(text="Please Enter A Valid Number")

calculate_button = tkinter.Button(text="CALCULATE", command=calculate)
calculate_button.config(bg="black", fg="white", font=("calibri", 11, "bold"))
calculate_button.pack(pady=10)

#result label
result_label = tkinter.Label(text="")
result_label.pack()
result_label.config(bg=backcolor, padx=10, pady=10)

window.mainloop()
