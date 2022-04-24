import PySimpleGui as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text("Nome"),sg.Input()],
            [sg.Text("Idade"),sg.Input()],
            [sg.button("Eviar")]
        ]
        # Janela
        janela = sg.Windows("Dados do Usuário").layout(layout)
        # Dados Tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()