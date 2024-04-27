
import PySimpleGUI as psg
import random

#func
def game():

    global a,b
    a = random.randint(0,10)
    print(a)
    b = int(a)



#main
    layout = [
        [psg.Text("Number Guessing Game"),psg.Button("About")],
        [psg.Button("1",size=(10,2)),psg.Button("2",size=(10,2)),psg.Button("3",size=(10,2)),psg.Button("4",size=(10,2))],
        [psg.Button("5",size=(10,2)),psg.Button("6",size=(10,2)),psg.Button("7",size=(10,2)),psg.Button("8",size=(10,2))],
        [psg.Button("9",size=(10,2)),psg.Button("10",size=(10,2)),psg.Button("11",size=(10,2)),psg.Button("12",size=(10,2))],
        [psg.Button("13",size=(10,2)),psg.Button("14",size=(10,2)),psg.Button("15",size=(10,2)),psg.Button("16",size=(10,2))],
        [psg.Button("17",size=(10,2)),psg.Button("18",size=(10,2)),psg.Button("19",size=(10,2)),psg.Button("20",size=(10,2))],
        [psg.Button("Retry",key='-ry-')],
        [psg.Text(key='-res-')]]

    window = psg.Window('Game', layout, size=(400,400))




    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == 'Exit':
            break
        print(event,values)
        if event == "About":
            text = "This is the Number Guessing Game \nThis Was Devoloped By RAGHUL V\n\nPython Version  : 3.10 \nGame Version   : 1.0"
            psg.popup_scrolled(text, title="About the Game !",size=(30,10))
        if event == "-ry-":
            print("returning")
            window.close()
            return game()
        if event != str(b):
            window['-res-'].update(" Wrong answer ")
            window[event].update(button_color="red")
            print("noo")
        if event == str(b) :
            window['-res-'].update(" Correct answer ")
            window[str(b)].update(button_color="green")
            print("yess")
            pk = psg.popup_yes_no("Correct Answer !\nDo you want to Restart the Game ?",title=" Game")
            if pk == "Yes":
                print("clicked yes")
                window.close()
                return game()


 
    window.close()

game()
