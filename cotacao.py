import customtkinter
import requests
from tkinter import messagebox

window = customtkinter.CTk()

class Function():
    def getinformations(self):
        try:
            self.api_key = "075acf74dd8849811972c4ef"
            self.url_BRL_DOL = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD"
            self.url_BRL_EUR = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/EUR"
            self.url_BRL_GBP = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/GBP"
            self.request_DOL = requests.get(self.url_BRL_DOL)
            self.request_EUR = requests.get(self.url_BRL_EUR)
            self.request_GBP = requests.get(self.url_BRL_GBP)
            self.label_dolar_result.configure(text=(self.request_DOL.json()['conversion_rates']['BRL']))
            self.label_euro_result.configure(text=(self.request_EUR.json()['conversion_rates']['BRL']))
            self.label_libra_result.configure(text=(self.request_GBP.json()['conversion_rates']['BRL']))
        except:
            messagebox.showerror("Erro", "Erro ao se conectar com a API pode ser que a API está fora do ar ou a chave está invalida verifique https://app.exchangerate-api.com")

    def calculator(self):
        self.value = self.BRL_entry.get()
        if (self.value.isdigit()):
            try:
                self.top_level = customtkinter.CTkToplevel(self.window)
                self.top_level.lift()
                self.top_level.title("Calculadora")
                self.top_level.geometry("300x300")
                self.top_level.resizable(False,False)
                self.value_DOL = self.request_DOL.json()['conversion_rates']['BRL'] * float(self.value)
                self.value_EUR = self.request_EUR.json()['conversion_rates']['BRL'] * float(self.value)
                self.value_GBP = self.request_GBP.json()['conversion_rates']['BRL'] * float(self.value)

                self.label_mostrar_BRL = customtkinter.CTkLabel(self.top_level, text= f"R$: {float(self.value):.3f}".replace(".",","), font=("arial", 28, "bold"),text_color="#000000")
                self.label_mostrar_BRL.place(relx=0.05, rely=0.1)

                self.label_mostrar_DOL = customtkinter.CTkLabel(self.top_level, text= f"R$: {self.value_DOL:.3f}".replace(".",","), font=("arial", 28, "bold"),text_color="#006400")
                self.label_mostrar_DOL.place(relx=0.3,rely=0.35)

                self.label_mostrar_EUR = customtkinter.CTkLabel(self.top_level, text= f"R$: {self.value_EUR:.3f}".replace(".",","), font=("arial", 28, "bold"),text_color="#006400")
                self.label_mostrar_EUR.place(relx=0.3,rely=0.55)

                self.label_mostrar_GBP = customtkinter.CTkLabel(self.top_level, text= f"R$: {self.value_GBP:.3f}".replace(".",","), font=("arial", 28, "bold"),text_color="#006400")
                self.label_mostrar_GBP.place(relx=0.3,rely=0.75)

            except:
                self.top_level.destroy()
                messagebox.showerror("Error", "Parece que você está tentando calcular sem atualizar os campos:\nClique no botão de atualizar e tente novamente")
 
        else:
            messagebox.showinfo("Informação", "A entrada não pode conter:\nValores Vazio\nValores negativos\nOu valores de texto")

class Aplication(Function):
    def __init__(self):
        self.window = window
        self.setting_App()
        self.frame_window()
        self.widget_window()
        self.window.mainloop()

    def setting_App(self):
        self.window.title("Cotação De Moeda")
        self.window.iconbitmap("CustomTkinterProject\CotacaoMoeda\image\Moeda.ico")
        self.window.configure(fg_color="#708090")
        self.window.geometry("500x400")
        self.window.resizable(False,False)

    def frame_window(self):
        self.frame = customtkinter.CTkFrame(self.window)
        self.frame.configure(fg_color="#B0C4DE", border_width= 4)
        self.frame.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.95)

    def widget_window(self):
        self.label_title = customtkinter.CTkLabel(self.frame, text="Cotação de moedas", fg_color="transparent", font=("verdana", 20, "bold"))
        self.label_title.place(relx=0.3, rely=0.1)

        self.label_reais = customtkinter.CTkLabel(self.frame, text="Real Brasileiro(BRL)", fg_color="transparent", font=("verdana", 14, "bold"), text_color="green")
        self.label_reais.place(relx=0.25, rely=0.25)

        self.BRL_entry = customtkinter.CTkEntry(self.frame)
        self.BRL_entry.place(relx=0.60, rely=0.25, relwidth=0.2)

        self.label_dolar = customtkinter.CTkLabel(self.frame, text="Dolar:", fg_color="transparent", font=("verdana", 14, "bold"))
        self.label_dolar.place(relx=0.25, rely=0.35)

        self.label_euro = customtkinter.CTkLabel(self.frame, text="Euro:", fg_color="transparent", font=("verdana", 14, "bold"))
        self.label_euro.place(relx=0.25, rely=0.45)

        self.label_libra = customtkinter.CTkLabel(self.frame, text="Libra:", fg_color="transparent", font=("verdana", 14, "bold"))
        self.label_libra.place(relx=0.25, rely=0.55)

        self.label_dolar_result = customtkinter.CTkLabel(self.frame, text="Dolar", text_color="green", font=("arial", 15, "bold"))
        self.label_dolar_result.place(relx=0.40, rely=0.35)

        self.label_euro_result = customtkinter.CTkLabel(self.frame, text="Euro", text_color="green", font=("arial", 15, "bold"))
        self.label_euro_result.place(relx=0.40, rely=0.45)

        self.label_libra_result = customtkinter.CTkLabel(self.frame, text="Libras", text_color="green", font=("arial", 15, "bold"))
        self.label_libra_result.place(relx=0.40, rely=0.55)

        self.button_calc = customtkinter.CTkButton(self.frame, text="Atualizar", command= self.getinformations, font=("arial", 16, "bold"))
        self.button_calc.place(relx=0.15, rely=0.80, relwidth=0.3)

        self.button_calc = customtkinter.CTkButton(self.frame, text="Calcular", command= self.calculator, font=("arial", 16, "bold"))
        self.button_calc.place(relx=0.55, rely=0.80, relwidth=0.3)



Aplication()