import PySimpleGUI as sg
import simplecrypt

file:str
dir_file = ""
widget= [[sg.TabGroup([[sg.Tab("Encriptar", layout=[[sg.Button("File"), sg.InputText(default_text=dir_file, size=20, key=("-OUTPUT FILE ENCRY-"), background_color="#DEDEDE"), sg.Text("Constraseña: "), sg.InputText(key=("-OUTPUT PASS ENCRY-"), size=20, password_char="*")],
                                                    [sg.Button(button_text="Encriptar")]]), 
                        sg.Tab("Desencriptar", layout=[[sg.Button("File "), sg.InputText(default_text=dir_file, size=20, key=("-OUTPUT FILE DESCRY-"), background_color="#DEDEDE"), sg.Text("Constraseña: "), sg.InputText(key=("-OUTPUT PASS DESCRY-"), size=20, password_char="*")], 
                                                       [sg.Button(button_text="Desencriptar"), ]])]]) ],        
         [sg.Button(button_text="Limpiar consola")],
         [sg.Multiline(auto_refresh=True, size=(60, 10), disabled=True, reroute_cprint=True, key=("-MULTILINE-"), background_color="black")],
]

window = sg.Window(title="PyToCrypto", layout=widget)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == "File":
        try:
            file = sg.popup_get_file(message="File",file_types=(("ALL FILE", "*.*"),))
            dir_file = file
            window["-OUTPUT FILE ENCRY-"].update(dir_file)
        except:
            window["-MULTILINE-"].update(sg.cprint("No se agrego ningun archivo ", font=("Console", 10), text_color="white"))

    elif events == "Encriptar":
        password = values["-OUTPUT PASS ENCRY-"]
        
        try:
                with open(file=file, mode="rb") as f:
                    r = f.read()
                window["-MULTILINE-"].update(sg.cprint("Encriptando " + dir_file + "", font=("Console", 10), text_color="white"))
                a = simplecrypt.encrypt(password=password, data=r)

                with open(file=file + ".enc", mode="wb") as f:
                    f.write(a)
                window["-MULTILINE-"].update(sg.cprint("Se encriptado  " + f.name + "", font=("Console", 10), text_color="white"))
        
        except Exception as e:
            window["-MULTILINE-"].update(sg.cprint("Error de encriptado {}".format(e), font=("Console", 10), text_color="red"))
    
    elif events == "Limpiar consola":
         window["-MULTILINE-"].update(sg.cprint(erase_all=True))
    
    #Proceso para descentriptar archivos. 
    elif events == "File ":
        file = sg.popup_get_file(message="File",file_types=((".enc", ".enc"),)) 
        dir_file = file
        window["-OUTPUT FILE DESCRY-"].update(dir_file)
    
    elif events == "Desencriptar":
        try:
            password = values["-OUTPUT PASS DESCRY-"]
            
            with open(file=file, mode="rb") as f_c:
                d = f_c.read()

            window["-MULTILINE-"].update(sg.cprint("desencriptando... " + dir_file , font=("Console", 10), text_color="white"))        
            with open(file=file[:-4] , mode="wb") as f_:
                b = simplecrypt.decrypt(password=password, data=d)
                f_.write(b)    

            window["-MULTILINE-"].update(sg.cprint("Se desencripto " + f_.name, font=("Console", 10), text_color="white"))
        
        except Exception as e:
            window["-MULTILINE-"].update(sg.cprint("Error de desencriptado {}".format(e), font=("Console", 10), text_color="red"))

window.close() 