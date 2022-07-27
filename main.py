from collections import deque
import heapq
import sys
import copy
from time import clock_getres
from turtle import left, right

INF = int(1e9)
input = sys.stdin.readline

up_side = [['w','w','w'],['w','w','w'],['w','w','w']]
down_side = [['y','y','y'],['y','y','y'],['y','y','y']]
left_side = [['g','g','g'],['g','g','g'],['g','g','g']]
right_side = [['b','b','b'],['b','b','b'],['b','b','b']]
back_side = [['o','o','o'],['o','o','o'],['o','o','o']]
front_side = [['r','r','r'],['r','r','r'],['r','r','r']]

def rotate(cube,is_clockwise):
	tmp = copy.deepcopy(cube)

	if is_clockwise:
		for i in range(3):
			for j in range(3):
				cube[j][2-i] = tmp[i][j]
	else:
		for i in range(3):
			for j in range(3):
				cube[j][i] = tmp[i][2-j]


def U():
	tmp_left = copy.deepcopy(left_side[0])
	tmp_front = copy.deepcopy(front_side[0])
	tmp_right = copy.deepcopy(right_side[0])
	tmp_back = copy.deepcopy(back_side[0])
	rotate(up_side,1)

	left_side[0] = tmp_front
	front_side[0] = tmp_right
	right_side[0] = tmp_back
	back_side[0] = tmp_left
		

def D():
	tmp_left = copy.deepcopy(left_side[2])
	tmp_front = copy.deepcopy(front_side[2])
	tmp_right = copy.deepcopy(right_side[2])
	tmp_back = copy.deepcopy(back_side[2])
	rotate(down_side,1)

	left_side[2] = tmp_back
	front_side[2] = tmp_left
	right_side[2] = tmp_front
	back_side[2] = tmp_right

def F():
	tmp_left = copy.deepcopy(left_side)
	tmp_right = copy.deepcopy(right_side)
	tmp_up = copy.deepcopy(up_side)
	tmp_down = copy.deepcopy(down_side)
	rotate(front_side,1)

	rotate(tmp_left,1)
	up_side[2] = tmp_left[2]

	rotate(right_side,0)
	right_side[2] = tmp_up[2]
	rotate(right_side,1)

	rotate(tmp_right,1)
	down_side[0] = tmp_right[0]

	rotate(left_side,0)
	left_side[0] = tmp_down[0]
	rotate(left_side,1)

def B():
	tmp_left = copy.deepcopy(left_side)
	tmp_right = copy.deepcopy(right_side)
	tmp_up = copy.deepcopy(up_side)
	tmp_down = copy.deepcopy(down_side)


	rotate(tmp_left,1)
	up_side[0] = tmp_left[0]

	rotate(right_side,0)
	right_side[0] = tmp_up[0]
	rotate(right_side,1)

	rotate(tmp_right,1)
	down_side[2] = tmp_right[2]

	rotate(left_side,0)
	left_side[2] = tmp_down[2]
	rotate(left_side,1)



def L():
	tmp_front = copy.deepcopy(front_side)
	tmp_back = copy.deepcopy(back_side)
	tmp_up = copy.deepcopy(up_side)
	tmp_down = copy.deepcopy(down_side)
	rotate(left_side,1)

	rotate(up_side,1)
	rotate(tmp_back,0)
	up_side[0] = tmp_back[0]
	rotate(up_side,0)

	rotate(front_side,1)
	rotate(tmp_up,1)
	front_side[0] = tmp_up[0]
	rotate(front_side,0)

	rotate(down_side,1)
	rotate(tmp_front,1)
	down_side[0] = tmp_front[0]
	rotate(down_side,0)

	rotate(back_side,0)
	rotate(tmp_down,1)
	back_side[0] = tmp_down[0]
	rotate(back_side,1)


def R():
	tmp_front = copy.deepcopy(front_side)
	tmp_back = copy.deepcopy(back_side)
	tmp_up = copy.deepcopy(up_side)
	tmp_down = copy.deepcopy(down_side)
	rotate(right_side,1)

	rotate(up_side,1)
	rotate(tmp_front,1)
	up_side[2] = tmp_front[2]
	rotate(up_side,0)

	rotate(front_side,1)
	rotate(tmp_down,1)
	front_side[2] = tmp_down[2]
	rotate(front_side,0)

	rotate(down_side,0)
	rotate(tmp_back,1)
	down_side[0] = tmp_back[0]
	rotate(down_side,1)

	rotate(back_side,0)
	rotate(tmp_up,1)
	back_side[2] = tmp_up[2]
	rotate(back_side,1)


def simulation(rotates):

	for dir in rotates:
		if dir == 'U+':
			U() #1 is clockwise
		elif dir == 'U-':
			for i in range(3):
				U() #0 is reverse  clockwise
		elif dir == 'D+':
			D()
		elif dir == 'D-':
			for i in range(3):
				D()
		elif dir == 'F+':
			F()
		elif dir == 'F-':
			for i in range(3):
				F()
		elif dir == 'B+':
			rotate(back_side,1)
			for i in range(3):
				B()
		elif dir == 'B-':
			rotate(back_side,0)
			B()
		elif dir == 'R+':
			R()
		elif dir == 'R-':
			for i in range(3):
				R()
		elif dir == 'L+':
			L()
		elif dir == 'L-':
			for i in range(3):
				L()

def return_default():
	for i in range(3):
		for j in range(3):
			up_side[i][j] = 'w'
			down_side[i][j] = 'y'
			left_side[i][j] =  'g'
			right_side[i][j] = 'b'
			back_side[i][j] = 'o'
			front_side[i][j] = 'r'


def main():
	n = int(input())

	for i in range(n):
		k = int(input())
		rotates = input().split()
		simulation(rotates)

		for i in range(3):
			print(''.join(up_side[i]))

		return_default()


main()






