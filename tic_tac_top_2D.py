from colorama import init
from colorama import Fore, Style, Back
init(autoreset=True)
# -*- coding: utf-8 -*-
board = list(range(1,10))

def draw_board(board):
	print(Fore.YELLOW + "-" * 13)
	for i in range(3):
		print(Fore.GREEN + "|", board[0+i*3], Fore.GREEN + "|", board[1+i*3], Fore.GREEN + "|", board[2+i*3], Fore.GREEN + "|")
		print(Fore.YELLOW + "-" * 13)

def take_input(player_token):
	valid = False
	while not valid:
		player_answer = input("Куда поставим " + player_token+"? ")
		try:
			player_answer = int(player_answer)
		except:
			print(Fore.RED + "Некорректный ввод. Вы уверены, что ввели число?")
			continue
		if player_answer >= 1 and player_answer <= 9:
			if (str(board[player_answer-1]) not in "XO"):
				board[player_answer-1] = player_token
				valid = True
			else:
				print(Fore.RED + "Эта клеточка уже занята")
		else:
			print(Fore.RED + "Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
	win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for each in win_coord:
		if board[each[0]] == board[each[1]] == board[each[2]]:
			return board[each[0]]
	return False

def main(board):
	counter = 0
	win = False
	while not win:
		draw_board(board)
		if counter % 2 == 0:
			take_input("X")
		else:
			take_input("O")
		counter += 1
		if counter > 4:
			tmp = check_win(board)
			if tmp:
				print(tmp, "Выиграл!")
				win = True
				break
			if counter == 9:
				print("Нечья!")
				break
	draw_board(board)

print(main(board))

input("Нажмите ENTER чтобы закончить игру... ")