import PySimpleGUI as sg
layout=[
        [sg.Input(key="input1"),
         sg.Spin(["Km to Maile","Kg to Pound","Sec to Min"],key="units"),
         sg.Button("Convert",key="convert")
         ],

        [sg.Text("Output",key="-output-")]
        ]

window=sg.Window("Converter",layout)

while True:
        event,values=window.read()

        if event == sg.WIN_CLOSED:
                break
        if event=="convert":
           input_val=values["input1"]
           print(input_val)
           if input_val.isnumeric():
                unit=values["units"]
                if unit=="Km to Maile":
                    output=round(float(input_val)*0.6214,2)
                    output_str=f"{input_val} Km are {output} Miles."


                if unit=="Kg to Pound":
                    output=round(float(input_val)*2.20462,2)
                    output_str=f"{input_val} Kg are {output} Pounds."
                

                if unit=="Sec to Min":
                    output=round(float(input_val)/60,2)
                    output_str=f"{input_val} Secounds are {output} Minutes."
                window["-output-"].update(output_str)


window.close()
