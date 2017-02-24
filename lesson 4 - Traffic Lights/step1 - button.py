from gpiozero import Button

button = Button(21)

count = 0
total = 3

while True:
	if count <= total:
		print(button.is_pressed)
		count = count + 1
	else:
		print('Application Exit')
		break