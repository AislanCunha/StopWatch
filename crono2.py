#Este cronômetro está baseado no vídeo "https://www.youtube.com/watch?v=-UQCLfrqO8g&t=329s"
from tkinter import *
import tkinter

#cores utilizadas#
color1 = "#0a0a0a" #preta
color2 = "#fafcff" #branca
color3 = "#eb463b" #vermelho

#configurando a janela do cronômetro
window = Tk()
window.title('stopwatch')
window.geometry('300x180')
window.configure(bg=color1)
window.resizable(width=FALSE, height=FALSE)

#funções para a execução do cronômetro
    #definido das primeiras variáveis globais
global watch
global turn
global meter
global limiter

limiter = 59
watch = '00:00:00'
turn = False
meter = -5

def begin():
    global watch
    global meter
    global limiter

    if turn:#antes do cronômetro começar
        if meter <=-1:
            outset = 'Start in ' + str(meter)
            label_watch['text'] = outset
            label_watch['font'] = 'Arial 10'
    
    #rodando o cronômetro
        else:
            label_watch['font'] = 'Times 50 bold'

            temporary = str(watch)
            h,m,s = map(int, temporary.split(':'))
            h = int(h)
            m = int(m)
            s = int(meter)

            if (s>=limiter):
                meter = 0
                m+=1

            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)

        #atualizando os valores dentro da função
            temporary = str(h[-2:]) + ':' + str(m[-2:]) + ':'  + str(s[-2:])
            label_watch['text'] = temporary
            watch = temporary


        label_watch.after(1000, begin)
        meter +=1

#função para o botão start o cronômetro
def start():
    global turn
    turn = True
    begin()

#função para o botão pause no cronômetro
def pause():
    global turn
    turn = False

#função para o botão reset no cronômetro
def reset():
    global meter
    global watch
    
    #reiniciando o tempo e o contador do cronômetro
    meter = 0
    watch = '00:00:00'
    label_watch['text'] = watch   


#criando labels do cronômetro
label_app = Label(window, text='progressive stopwatch', fon=('Arial 10'), bg=color1, fg=color2)
label_app.place(x=20, y=5)

label_watch = Label(window, text=watch, fon=('Times 50 bold'), bg=color1, fg=color3)
label_watch.place(x=20, y=30)

#criando os botões (start, pause, reset)
start_button = Button(window, command=start, text='Start', width=10, height=2, bg=color1, fg=color2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
start_button.place(x=20, y=130)

pause_button = Button(window, command=pause, text='Pause', width=10, height=2, bg=color1, fg=color2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
pause_button.place(x=105, y=130)

reset_button = Button(window, command=reset, text='Reset', width=10, height=2, bg=color1, fg=color2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
reset_button.place(x=190, y=130)

window.mainloop()

#para abrir o projeto devemos abrir novo terminal com 'python' e o nome do 'crono.py'