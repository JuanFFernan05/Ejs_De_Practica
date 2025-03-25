import tkinter as tk
from tkinter import messagebox


# Variables
player = 'O'
game_over = False

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons [i][2]['text'] != '':      # Verificar por fila
            return True 
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':      # Verificar por columna
            return True
        if (buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '') or (buttons[0][2]['text'] == buttons [1][1]['text'] == buttons [2][0]['text'] != ''):
            return True  
    return False
    
def button_click(row, col):
    global player, game_over
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = player
        if(player == 'X'): 
            buttons[row][col]['bg'] = "#68A2D5"
        else:
            buttons[row][col]['bg'] = "#FC6B60"
        if check_winner():          # Comprobar si alguien gano
            messagebox.showinfo(title = "Ta Te Ti", message = f"Jugador {player} gana!")
            game_over = True 
        elif all(buttons[row][col]['text'] != '' for row in range(3) for col in range(3)):          # Comprobar si la partida terminó empatada
                messagebox.showinfo(title = "Fin de partida", message = "Es un empate!")
                game_over = True
        else:           # Seguimos - Cambio de jugador
            if player == 'X':
                player = 'O'    
            else:
                player = 'X'


def reset_game():
    global player, game_over
    player = 'X'
    game_over = False 
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
            buttons[row][col]['bg'] = "#838383"

root = tk.Tk()
root.title("Ta-Te-Ti")
root.geometry("500x500")
root.configure(bg = "#1F1F1F")

frame = tk.Frame(root, bg="#1F1F1F")
frame.place(relx = 0.5, rely = 0.5, anchor = 'center')

buttons = [[tk.Button(frame, text = '', font = "normal 20 bold", 
                    width = 5, height = 2, fg = "white", command = lambda row = row, col = col: button_click(row, col)) 
            for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row = row, column = col, padx = 10, pady = 10)

reset_button = tk.Button(root, text = "Reiniciar", font = "Normal 15 bold", command = reset_game, bg = "#838383", fg = "white")
reset_button.place(relx = 0.5, rely = 0.9, anchor = "center")


root.mainloop()

    