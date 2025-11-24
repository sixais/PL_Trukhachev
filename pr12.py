import requests
import json
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Получение данных пользователя GitHub')
window.geometry('500x350')
def request():
    username = "dimagi"
    repo = ent.get()
    url = f'https://api.github.com/repos/{username}/{repo}'
    try:
        r = requests.get(url)
        if r.status_code == 200:
            messagebox.showinfo('Успех', 'Соединение установлено!')
            user_data = r.json()
            result = {'company': user_data.get('company'), 'created_at': user_data.get('created_at'), 'email': user_data.get('email'), 'id': user_data.get('id'), 'name': user_data.get('name'), 'url': user_data.get('url')}
            with open('vivod.json', 'w') as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            messagebox.showinfo('Готово', 'Данные успешно сохранены в файл vivod.json')
        else:
            messagebox.showerror('Ошибка')
    except requests.exceptions.RequestException as e:
        messagebox.showerror('Сетевая ошибка')
frame = Frame(window)
frame.pack(expand=True)
Label(frame, text='Введите имя репозитория:').pack(pady=10)
ent = Entry(frame, width=30)
ent.pack(pady=5)
Button(frame, text='Получить информацию', command=request).pack(pady=15)
window.mainloop()