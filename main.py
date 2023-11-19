import PySimpleGUI as sg

import pymongo

import dotenv

import os

dotenv.load_dotenv()

myclient = pymongo.MongoClient("mongodb://"+os.environ['host']+"/")

mydb = myclient[os.environ['database']]

mycol = mydb[os.environ['collection']]

sg.theme("Black")

layout = [   

    [sg.Text("Nome")],
    [sg.Input(key="nome")],
    [sg.Text("Telefone")],
    [sg.Input(key="fone")],
    [sg.Button("Salvar")],
    [sg.Button("Pesquisar por Nome")],
    [sg.Button("Deletar por Nome")]

    ]

window = sg.Window("Tela de Gestão", layout=layout)

i = 0

while True:
    events, values = window.read()

    if events == "Salvar":

        if len(values["nome"]) > 0:
            if len(values["fone"]) > 0:
                mydict = { "nome": values['nome'], "fone": values['fone'] }

                x = mycol.insert_one(mydict)


    if events == "Pesquisar por Nome":
        
        mydoc = mycol.find({ "nome": values['nome']})
        
        lista_str = ''

        for x in mydoc:

            if i > 5:
                break

            i+=1
            
            lista_str += x['nome']+", "+x['fone']+"\n\n"

        i = 0
            

        sg.popup(lista_str)
        

    if events == "Deletar por Nome":
        myquery = { "nome": values['nome'] }

        mycol.delete_one(myquery)

    if events == sg.WIN_CLOSED:
        break
