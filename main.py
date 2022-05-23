import PySimpleGUI as sg

layout=[[sg.Button('but')],
        [sg.Input(key='text')],
        [sg.Text(key='out')],
        [sg.Button(key='del')]
        ]
window = sg.Window('', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'but':
        window['out'].print(values['text'])
        window['text'].update('')
    if event == 'del':
        #print(window['out'].__dict__)
        #[len(window['out'].DisplayText.split('\n'))-1]
        #o=window['out'].DisplayText.split('\n')
        k=window['out'].DisplayText.split('\n')[:-1]
        p=window['out'].update("\n".join(str(x) for x in k))
        print(k)
window.close()