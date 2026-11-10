import pandas as pd
#ja pandas vēl nav instaletas:      pip install pandas
#ir  nepieciešams instalēt openpyx: pip install openpyxl
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('10 - 12 klašu stundu izmaņas')
root.resizable(False, False)
root.geometry('600x300')

root.rowconfigure(2, weight=1)

sheet_url = "https://docs.google.com/spreadsheets/d/1t6UqdU_WXneufHDFHpPJfwkdLP-4ynt2/edit?gid=724315152#gid=724315152"

base_url = sheet_url.split("/edit")[0]
xlsx_url = f"{base_url}/export?format=xlsx"

klasesBurtaNobīde = 1
klasesNumuraNobīde = 0
klasesBurts = "A"
klasesNumurs = 10


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Rīt():
    global sheet_index
    sheet_index += 2
    AtjaunotLogu()

def Vakar():
    global sheet_index
    sheet_index -= 2
    AtjaunotLogu()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         Šie ir kā last-ditch effort censties izkārpīties no fakta ka stundu imzaiņas tiek mainītas neregulāri, dažreiz pirmie 2 sheets ir 5-9 klases, vai 6-9, un tikai tad sāk iet pamīšus 6-9 un 10-12, un google sheets saglabā pagājušo dienu stundu izmaiņu sheets, lai gan skolnieks to skatīt nevar D:<

def A():
    global klasesBurtaNobīde, klasesBurts
    print("A klase!")
    klasesBurtaNobīde = 1
    klasesBurts = "A"
    AtjaunotLogu()

def B():
    global klasesBurtaNobīde, klasesBurts
    print("B klase!")
    klasesBurtaNobīde = 2
    klasesBurts = "B"
    AtjaunotLogu()

def C():
    global klasesBurtaNobīde, klasesBurts
    print("C klase!")
    klasesBurtaNobīde = 3
    klasesBurts = "C"
    AtjaunotLogu()

def D():
    global klasesBurtaNobīde, klasesBurts
    print("D klase!")
    klasesBurtaNobīde = 4
    klasesBurts = "D"
    AtjaunotLogu()


def Desmit():
    global klasesNumuraNobīde, klasesNumurs
    print("10 klase!")
    klasesNumuraNobīde = 0
    klasesNumurs = "10"
    AtjaunotLogu()

def Vienpadsmit():
    global klasesNumuraNobīde, klasesNumurs
    print("11 klase!")
    klasesNumuraNobīde = 4
    klasesNumurs = "11"
    AtjaunotLogu()

def Divpadsmit():
    global klasesNumuraNobīde, klasesNumurs
    print("12 klase!")
    klasesNumuraNobīde = 8
    klasesNumurs = "12"
    AtjaunotLogu()

def AtjaunotLogu():
    print("Logs atjaunots")
    #sheet_index = 2
    global sheet_index
    global sheet_name
    df = pd.read_excel(xlsx_url, sheet_name=sheet_index)

    first_column = df.iloc[:, klasesBurtaNobīde + klasesNumuraNobīde]

    Pname_label.config(
        text=first_column.to_string(index=False))

    Klases_label.config(
        text=f"{klasesNumurs}{klasesBurts}")
    

    excel = pd.ExcelFile(xlsx_url)

# Visu lapu nosaukumi
    #print(excel.sheet_names)

    sheet_name = excel.sheet_names[sheet_index]

    #print(sheet_name)
    Datums_label.config(
        #text=f"{sheet_name}"
        text = f"{df.iloc[-1,:]}"
        )


buttonA = tk.Button(root, text="A klase", command=A)
buttonB = tk.Button(root, text="B klase", command=B)
buttonC = tk.Button(root, text="C klase", command=C)
buttonD = tk.Button(root, text="D klase", command=D)

buttonA.grid(row=0, column=0)
buttonB.grid(row=0, column=1)
buttonC.grid(row=0, column=2)
buttonD.grid(row=0, column=3)


button10 = tk.Button(root, text="10 klase", command=Desmit)
button11 = tk.Button(root, text="11 klase", command=Vienpadsmit)
button12 = tk.Button(root, text="12 klase", command=Divpadsmit)

button10.grid(row=1, column=0)
button11.grid(row=1, column=1)
button12.grid(row=1, column=2)


buttonRīt = tk.Button(root, text="Iepriekšējā diena", command=Rīt)
buttonVakar = tk.Button(root, text="Nākamā diena", command=Vakar)
buttonRīt.grid(row=4, column=1)
buttonVakar.grid(row=4, column=2)

sheet_index = 1 
df = pd.read_excel(xlsx_url, sheet_name=sheet_index)
kolonnasVar = klasesBurtaNobīde + klasesNumuraNobīde
first_column = df.iloc[:, klasesBurtaNobīde + klasesNumuraNobīde] 


Pname_label = tk.Label(root, text = "Lūdzu nospied savu attiecīgo burtu vai klasi", font=('calibre',10, 'bold'), anchor='w', justify="left")
Klases_label = tk.Label(root, text = "", font=('calibre',10, 'bold'), anchor='w', justify="left")
Datums_label = tk.Label(root, text = "", font=('calibre',10, 'bold'), anchor='w', justify="left")


Pname_label.place(x=170, y=55)
Klases_label.place(x=90, y=150)
Datums_label.place(x=528, y=283)

root.mainloop()