import threading
import os
import subprocess as sp


def TermInstall():
	libs_t = ['tesseract-ocr', 'libtesseract-dev',
	'tesseract-ocr-por', 'libasound-dev', 'portaudio19-dev',
	'libportaudio2', 'libportaudiocpp0']

	sp.run("sudo apt -y update", shell=True, capture_output=True)
	sp.run("wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz", shell=True, capture_output=True)
	sp.run("tar -xvzf geckodriver-v0.32.0-linux64.tar.gz", shell=True, capture_output=True)
	sp.run("mv geckodriver /usr/bin", shell=True, capture_output=True)
	sp.run("rm -f -r -d -v geckodriver-v0.32.0-linux64.tar.gz", shell=True, capture_output=True)
	for lib1 in libs_t:
		a = sp.run(f'sudo apt -y install {lib1}', shell=True, capture_output=True)
		if a.returncode != 0:
			print(f'Nao foi possivel installar:  [{lib1}]')
			exit()
		else:
			print(f'A biblioteca {lib1} foi instalada com sucesso!')

	TermInstall.status = 'Fim'


def PipInstall():
	libs_pip = ['playwright', 'pywhatkit', 'pyautogui', 
	'SpeechRecognition', 'selenium', 'gtts', 'pyalsaaudio', 'pygame',
	'playsound', 'requests', 'wikipedia', 'emojis', 'opencv-python']

	for lib2 in libs_pip:
		b = sp.run(f'pip3 install {lib2}', shell=True, capture_output=True)
		if (b.returncode != 0):
			print('FATAL ERROR')
			print(f"Nao foi possivel installar a biblioteca {lib2}")
			exit()
		else:
			print(f"A biblioteca {lib2} foi instalada com sucesso!")

	PipInstall.status = 'Fim'


if os.uname().sysname == 'Linux':
	if os.getuid() != 0:
		print("Voce DEVE rodar esse programa como superusuario(root)!")
		exit()
	
	thread1 = threading.Thread(target=TermInstall)
	thread2 = threading.Thread(target=PipInstall)
	thread1.start()
	thread2.start()

	while True:
		try:
			if TermInstall.status == 'Fim':
				print('fim da thread TermInstall')
				break
		except:
			pass
	
	while True:
		try:
			if PipInstall.status == 'Fim':
				print('fim da thread PipInstall')
				break
		except:
			pass

	libs_pip2 = ['pyaudio', 'pytesseract']
	for lib in libs_pip2:
		#async_call = pool.apply_async(TermInstall)
		c = sp.run(f'pip install {lib}', shell=True, capture_output=True)
		if (c.returncode != 0):
			print(f"Nao foi possivel instalar {lib}")
			exit()
		else:
			print(f"A biblioteca {lib} foi instalada com sucesso")

	d = sp.run("playwright install", shell=True, capture_output=True)
	if (c.returncode != 0):
		print("Nao foi possivel rodar o comando {playwright install}")
		exit()
	else:
		print("Todas as instalacoes foram concluidas ;)")
		input("Pressione Enter para sair! ")
		sp.run("clear")


elif os.uname().sysname == 'Windows':
	print("coming soon")

