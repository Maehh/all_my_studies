import tkinter

# Criar janela principal

def tomr_nc():
    text_cu['text'] = "POC POC POC POC"

window = tkinter.Tk()
window.title('Janelinha Janelinha')
window.geometry('400x400')


orientation_text = tkinter.Label(window, text='Clique para tomar no CU!')
orientation_text.grid(column=0, row=0, padx=50,pady=50)


button = tkinter.Button(window, text='CU!', command=tomr_nc)
button.grid(column=0, row=1, padx=10, pady=10)

text_cu = tkinter.Label(window, text='')
text_cu.grid(column=0, row=2, padx=10, pady=10)


window.mainloop()   # Sempre última linha de código - Mantém janela
