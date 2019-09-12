import requests
import json 
import tkinter as tk

WIDTH=800
HEIGHT=700

root=tk.Tk()
root.title("Currency calculator")
root.iconbitmap('favicon.ico')

variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 

variable1.set("EUR")#KeyError 
variable2.set("UAH") 

class CurrencyConverter:

    rates={}

    def __init__(self,url):
        response=requests.get(url)
        data=response.json()
        self.rates=data["rates"]

    def convert(self,amount,from_currency,to_currency,output):

        try:             #10 eur to uah
            float(amount)
        except:
            amount.insert(0,str(10.0))
            amount=10.0

        # initial_amount=amount
        if from_currency != "USD":
            amount=amount/self.rates[from_currency] 
        if to_currency == "USD":
            output.insert(0, str(round(amount,3))) 
        else: 
            output.insert(0,str(round(amount * self.rates[to_currency],3)))           


converter = CurrencyConverter("https://api.exchangerate-api.com/v4/latest/USD")

# print(converter.convert(1.0, "EUR", "USD"))
# print(converter.convert(1.0, "GBP", "USD"))
# print(converter.convert(1.0, "CAD", "GBP"))
# print(converter.convert(1.0, "CAD", "EUR"))

#converter.convert(15.0, "EUR", "UAH",amount2_field) 

#,command = converter.convert(amount1_field.get(), variable1.get(), variable2.get(),amount2_field)

def clear_all():
    amount1_field.delete(0, 'end')  
    amount2_field.delete(0, 'end') 

if __name__ == "__main__":
            
    canvas=tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    background_image=tk.PhotoImage(file="dollars.png")
    background_label=tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame=tk.Frame(root,bg="#bff5cd")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    welcome_label=tk.Label(frame, text="Welcome to currency calc!", bg="yellow",pady="10", padx="5")
    welcome_label.config(font=("Unispace", 20))
    welcome_label.pack()

    main_frame=tk.Frame(frame,bg="white")
    main_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

    label1 = tk.Label(main_frame, text = "Amount :",fg = 'black')#, bg = 'dark green')  
    label1.place(relx=0.05, rely=0.05, relheight=0.1)
    label1.config(font=("Unispace", 16))

    label2 = tk.Label(main_frame, text = "From Currency :",fg = 'black')#, bg = 'dark green')    
    label2.place(relx=0.05, rely=0.2, relheight=0.1)
    label2.config(font=("Unispace", 16))

    label3 = tk.Label(main_frame, text = "To Currency :",fg = 'black')#, bg = 'dark green')    
    label3.place(relx=0.05, rely=0.35, relheight=0.1)
    label3.config(font=("Unispace", 16))

    label4 = tk.Label(main_frame, text = "Converted Amount :",fg = 'black')#, bg = 'dark green')  
    label4.place(relx=0.05, rely=0.5, relheight=0.1)
    label4.config(font=("Unispace", 16))
    
    amount1_field = tk.Entry(main_frame, font=("Unispace", 16)) 
    amount1_field.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.1)#, relheight=0.1) 
    
    
    amount2_field = tk.Entry(main_frame, font=("Unispace", 16)) 
    amount2_field.place(relx=0.5, rely=0.5,relwidth=0.4, relheight=0.1) 

    currency_code=['USD','AUD','CAD','CNY','CZK','EUR','GBP','JPY','PLN','RUB','UAH']

    from_currency_option = tk.OptionMenu(main_frame, variable1, *currency_code) 
    to_currency_option = tk.OptionMenu(main_frame, variable2, *currency_code) 

    from_currency_option.config(font=("Unispace", 16),cursor='circle')
    to_currency_option.config(font=("Unispace", 16),cursor='circle')

    from_currency_option.place(relx=0.5, rely=0.2, relheight=0.1)
    to_currency_option.place(relx=0.5, rely=0.35, relheight=0.1)
    
    convert_button=tk.Button(main_frame,text = "Convert",font=("Unispace", 16), bg = "red", fg = "black",cursor='exchange', command=converter.convert(amount1_field, "EUR", "UAH",amount2_field) )#, command=converter.convert(amount1_field.get(), "EUR", "UAH",amount2_field) )#,command = converter.convert(amount1_field.get(), variable1.get(), variable2.get(),amount2_field))#,command = converter.convert(amount1_field.get(), variable1.get(), variable2.get(),amount2_field))#KeyError
    convert_button.place(relx=0.7, rely=0.7, relheight=0.1)
        
    clear_button=tk.Button(main_frame,text = "Clear",font=("Unispace", 16), bg = "red", fg = "black",cursor='target', command = clear_all)
    clear_button.place(relx=0.52, rely=0.7, relheight=0.1)
     
    
    root.mainloop()


















# def real_time_currency_conversion():
#     url ="https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5" #Connect to the URL as if you are opening it in browser 
 
#     response = requests.get(url)
#     data=response.json()
#     # data = response.text 
#     # parsed = json.loads(data)

#     amount=float(amount1_field.get())

#     if variable1.get()=='UAH':
#         if variable2.get()=='UAH':
#             amount2_field.insert(0, str(amount))
#         elif variable2.get()=='USD':
#             amount2_field.insert(0, str(round(amount/float(parsed[0]['sale']),3)))
#         elif variable2.get()=='EUR':
#             amount2_field.insert(0, str(round(amount/float(parsed[1]['sale']),3)))
#         elif variable2.get()=='RUB':
#             amount2_field.insert(0, str(round(amount/float(parsed[2]['sale']),3)))
#     elif variable1.get()=='USD':
#         if variable2.get()=='USD':
#             amount2_field.insert(0, str(amount))
#         elif variable2.get()=='UAH':       
#             amount2_field.insert(0, str(round(amount*float(parsed[0]['buy']),3)))
#         elif variable2.get()=='EUR':
#             pass
                

#     # new_amount = round(amount * Exchange_Rate, 3) 
  
    
#     # amount2_field.insert(0, str(new_amount)) 
#_____________________________________________________

# class CurrencyConverter:
#     def __init__(self, url):
#         response = requests.get(url)
#         data = response.json()
#         # data = response.text 
#         # parsed = json.loads(data) 
#         self.data=data

#     def convert(self, amount, from_currency, to_currency,ident_1,ident_2):
       



#         my_amount = amount
#         if from_currency != "UAH":#міняєм валюту на гривні по курсу
#             my_amount=my_amount* float(self.data[ident_1]['buy'])
#         #elif from_currency == "UAH":

#         if to_currency == "UAH":
#             amount2_field.insert(0, str(my_amount))

#         else:
#             amount2_field.insert(0, str(my_amount/float(self.data[ident_2]['sale'])))

#amount2_field.insert(0, str())


# converter = CurrencyConverter("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
#converter.convert(amount1_field,variable1.get(),variable2.get())           


 

      
    
# def currency_convert():
#     url ="https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
#     response = requests.get(url)
#     data = response.json()













    # #my_amount=amount1_field
    # # ident_1=1
    # # ident_2=2
    # # if variable1.get()=="USD":
    # #     ident_1=0
    # # elif variable1.get()=="EUR":
    # #     ident_1=1
    # # elif variable1.get()=="RUB":
    # #     ident_1=2
    # # elif variable1.get()=="BTC":
    # #     ident_1=3

    # # if variable2.get()=="USD":
    # #     ident_2=0
    # # elif variable2.get()=="EUR":
    # #     ident_2=1
    # # elif variable2.get()=="RUB":
    # #     ident_2=2
    # # elif variable2.get()=="BTC":
    # #     ident_2=3
    # new_amount=None
    # exch_var=-1
    # exch_var1=-1
    # amount1=amount1_field.get()
    # if  variable1.get() != "UAH":#міняєм валюту на гривні по курсу
    #     if variable1.get()=="USD":
    #         exch_var=float(data[0]['buy'])
    #     elif variable1.get()=="EUR":
    #         exch_var=float(data[1]['buy'])
    #     elif variable1.get()=="RUB":
    #         exch_var=float(data[2]['buy'])
    #     elif variable1.get()=="BTC":
    #         exch_var=float(data[3]['buy'])
    #     new_amount=amount1 * exch_var
    #     #elif from_currency == "UAH":

    # if variable2.get() == "UAH":
    #     return amount2_field.insert(0, str(new_amount))

    # else:
    #     if variable2.get()=="USD":
    #         exch_var1=float(data[0]['sale'])
    #     elif variable2.get()=="EUR":
    #         exch_var1=float(data[1]['sale'])
    #     elif variable2.get()=="RUB":
    #         exch_var1=float(data[2]['sale'])
    #     elif variable2.get()=="BTC":
    #         exch_var1=float(data[3]['sale'])
    #     return amount2_field.insert(0, str(new_amount/exch_var1))
#_______________________________________________________________________________