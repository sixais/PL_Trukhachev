from tkinter import *
from tkinter import ttk, messagebox, filedialog, Menu

window = Tk()
window.title('Трухачев Андрей Дмитриевич')
window.geometry('500x350')
style = ttk.Style()
style.configure('Custom.TNotebook', tabposition='nw')
style.configure('Custom.TNotebook.Tab', padding=[25, 12], width=100, anchor='center')
tab_control = ttk.Notebook(window, style='Custom.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')
tab_control.pack(expand=1, fill="both", padx=20, pady=20)

#1
frame_calc = Frame(tab1)
frame_calc.pack(expand=True)
Label(frame_calc, text="Калькулятор").pack(pady=10)
frame_inputs = Frame(frame_calc)
frame_inputs.pack(pady=10)
entry1 = Entry(frame_inputs, width=10)
entry1.pack(side=LEFT, padx=5)
operations = ['+', '-', '*', '/']
operation_var = StringVar(value='+')
operation_menu = ttk.Combobox(frame_inputs, textvariable=operation_var, values=operations, width=5, state='readonly')
operation_menu.pack(side=LEFT, padx=5)
entry2 = Entry(frame_inputs, width=10)
entry2.pack(side=LEFT, padx=5)
def calc():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        result_label.config(text=f"Результат: {result}")
    except:
        messagebox.showerror("Ошибка", "Введите корректные числа!")
Button(frame_calc, text="Вычислить", command=calc).pack(pady=10)
result_label = Label(frame_calc, text="Результат: ")
result_label.pack()

#2
frame_checkboxes = Frame(tab2)
frame_checkboxes.pack(expand=True)
Label(frame_checkboxes, text="Выберите вариант:").pack(pady=10)
choice_var = StringVar()
def check():
    # Снимаем выбор с других чекбоксов при выборе одного
    selected = choice_var.get()
    if selected == "1":
        checkbox2_var.set(False)
        checkbox3_var.set(False)
    elif selected == "2":
        checkbox1_var.set(False)
        checkbox3_var.set(False)
    elif selected == "3":
        checkbox1_var.set(False)
        checkbox2_var.set(False)
checkbox1_var = BooleanVar()
checkbox1 = Checkbutton(frame_checkboxes, text="Первый", variable=checkbox1_var, command=lambda: [choice_var.set("1"), check()])
checkbox1.pack()
checkbox2_var = BooleanVar()
checkbox2 = Checkbutton(frame_checkboxes, text="Второй", variable=checkbox2_var, command=lambda: [choice_var.set("2"), check()])
checkbox2.pack()
checkbox3_var = BooleanVar()
checkbox3 = Checkbutton(frame_checkboxes, text="Третий", variable=checkbox3_var, command=lambda: [choice_var.set("3"), check()])
checkbox3.pack()
def show_selection():
    if checkbox1_var.get():
        messagebox.showinfo("Выбор", "Вы выбрали первый вариант")
    elif checkbox2_var.get():
        messagebox.showinfo("Выбор", "Вы выбрали второй вариант")
    elif checkbox3_var.get():
        messagebox.showinfo("Выбор", "Вы выбрали третий вариант")
    else:
        messagebox.showwarning("Внимание", "Вы ничего не выбрали!")
Button(frame_checkboxes, text="Показать выбор", command=show_selection).pack(pady=10)

#3
frame_text = Frame(tab3)
frame_text.pack(expand=True, fill=BOTH)
menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
text_widget = Text(frame_text)
text_widget.pack(expand=True, fill=BOTH, padx=10, pady=10)
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_widget.delete(1.0, END)
            text_widget.insert(1.0, file.read())
file_menu.add_command(label="Открыть файл", command=open_file)

window.mainloop()