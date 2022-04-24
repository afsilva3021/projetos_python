from PySimpleGUI import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text("Nome",size=(5,0)),sg.Input(size=(15,0),key="Nome")],
            [sg.Text("Idade",size=(5,0)),sg.Input(size=(15,0),key="Idade")],
            [sg.Text("Quais provedores de e-mail são aceitos?")],
            [sg.Checkbox("Gmail",key="Gmail"),sg.Checkbox("Outlook",key="Outlook"),sg.Checkbox("Yahoo",key="Yahoo")],
            [sg.Button("Eviar")]
        ]
        # Janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        # Dados Tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values["Nome"]
        idade = self.values["Idade"]
        aceita_gmail = self.values["Gmail"],
        aceita_outlook = self.values["Outlook"],
        aceita_yahoo = self.values["Gmail"],
        print(f"aceita Gmail: {aceita_gmail}")
        print(f"aceita Outlook: {aceita_outlook}")
        print(f"aceita Yahoo: {aceita_yahoo}")

tela = TelaPython()
tela.Iniciar()