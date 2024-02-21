from tkinter import *

class TextEditor:
    def __init__(self, title, geometry):
        # Configuração inicial da janela
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.minsize(width=840, height=480)

        # Configuração do frame para conter os widgets de controle de fonte
        self.frame = Frame(self.window, height=18)
        self.frame.pack(fill='x')

        # Widgets para controle de fonte
        font_text = Label(self.frame, text=" Font: ")
        font_text.pack(side='left')

        self.spin_font = Spinbox(self.frame, values=("Arial", "Verdana", "Courier", "System", "Helvetica"))
        self.spin_font.pack(side="left")

        font_size = Label(self.frame, text=" Font size: ")
        font_size.pack(side="left")

        self.spin_size = Spinbox(self.frame, from_=0, to=50)
        self.spin_size.pack(side='left')

        button_update = Button(self.frame, text='UP', command=self.update_font)
        button_update.pack(side='left')

        # Configuração do editor de texto
        self.text_area = Text(self.window, font=f'{self.spin_font.get()} {self.spin_size.get()}', width=830, height=480)
        self.text_area.pack()

        # Configuração do menu principal
        self.main_menu = Menu(self.window)

        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.newfile)
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Exit", command=self.window.quit)

        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.window.configure(menu=self.main_menu)

        self.window.mainloop()

    # Função para criar um novo arquivo
    def newfile(self):
        self.text_area.delete(1.0, "end")

    # Função para salvar o conteúdo atual do editor de texto em um arquivo
    def save(self):
        container = self.text_area.get(1.0, "end")
        with open('notepad.txt', "wt+") as a:
            a.write(container)

    # Função para abrir e exibir o conteúdo de um arquivo existente
    def open_file(self):
        with open("notepad.txt", "r") as a:
            container = a.read()
            self.text_area.insert(1.0, container)

    # Função para atualizar a fonte e o tamanho da fonte do editor de texto
    def update_font(self):
        size = self.spin_size.get()
        font = self.spin_font.get()
        self.text_area.config(font=f'{font} {size}')

app = TextEditor("Notepad", "840x480")