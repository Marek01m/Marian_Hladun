import requests
import json 
from tkinter import * 

WIDTH=800
HEIGHT=700

root=Tk()
root.title("Currency calculator")
root.iconbitmap('favicon.ico')

variable1 = StringVar(root) 
variable2 = StringVar(root) 

variable1.set("currency")
variable2.set("currency") 

def RealTimeCurrencyConversion(event=None): 
      
    from_currency = variable1.get() 
    to_currency = variable2.get() 
      
    api_key = "19OU05E2ZGNFEBZM"
     
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
  
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key 
     
    req_ob = requests.get(main_url) 
    
    result = req_ob.json() 
    
    Exchange_Rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate']) 
      
    amount = float(amount1_field.get()) 
  
    new_amount = round(amount * Exchange_Rate, 3) 
  
    amount2_field.insert(0, str(new_amount)) 

def clear_all():
    amount1_field.delete(0, 'end')  
    amount2_field.delete(0, 'end') 


if __name__ == "__main__":
            
    canvas=Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    background_image=PhotoImage(file="dollars.png")
    background_label=Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame=Frame(root,bg="#bff5cd")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    welcome_label=Label(frame, text="Welcome to currency calc!", bg="yellow",pady="10", padx="5")
    welcome_label.config(font=("Unispace", 20))
    welcome_label.pack()

    main_frame=Frame(frame,bg="white")
    main_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

    label1 = Label(main_frame, text = "Amount :",fg = 'black')#, bg = 'dark green')  
    label1.place(relx=0.05, rely=0.05, relheight=0.1)
    label1.config(font=("Unispace", 16))

    label2 = Label(main_frame, text = "From Currency :",fg = 'black')#, bg = 'dark green')    
    label2.place(relx=0.05, rely=0.2, relheight=0.1)
    label2.config(font=("Unispace", 16))

    label3 = Label(main_frame, text = "To Currency :",fg = 'black')#, bg = 'dark green')    
    label3.place(relx=0.05, rely=0.35, relheight=0.1)
    label3.config(font=("Unispace", 16))

    label4 = Label(main_frame, text = "Converted Amount :",fg = 'black')#, bg = 'dark green')  
    label4.place(relx=0.05, rely=0.5, relheight=0.1)
    label4.config(font=("Unispace", 16))
    
    amount1_field = Entry(main_frame, font=("Unispace", 16)) 
    amount1_field.place(relx=0.5, rely=0.05, relwidth=0.4, relheight=0.1)#, relheight=0.1) 
    
    amount2_field = Entry(main_frame, font=("Unispace", 16)) 
    amount2_field.place(relx=0.5, rely=0.5,relwidth=0.4, relheight=0.1) 

    currency_code=['USD','AUD','CNY','CZK','EUR','GBP','PLN','RUB','UAH','BTC']

    from_currency_option = OptionMenu(main_frame, variable1, *currency_code) 
    to_currency_option = OptionMenu(main_frame, variable2, *currency_code) 

    from_currency_option.config(font=("Unispace", 16),cursor='circle')
    to_currency_option.config(font=("Unispace", 16),cursor='circle')

    from_currency_option.place(relx=0.5, rely=0.2, relheight=0.1)
    to_currency_option.place(relx=0.5, rely=0.35, relheight=0.1)
    
    convert_button=Button(main_frame,text = "Convert",font=("Unispace", 16), bg = "red", fg = "black",cursor='exchange',command = RealTimeCurrencyConversion)
    convert_button.place(relx=0.7, rely=0.7, relheight=0.1)
        
    clear_button=Button(main_frame,text = "Clear",font=("Unispace", 16), bg = "red", fg = "black",cursor='target', command = clear_all)
    clear_button.place(relx=0.52, rely=0.7, relheight=0.1)
     
    root.bind('<Return>', RealTimeCurrencyConversion) 
    root.mainloop()

