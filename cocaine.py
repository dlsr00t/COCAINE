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
			print(f'\033[1;31mNao foi possivel installar o pacote:  [{lib1}]\033[m')
			exit()
		else:
			print(f'\033[32mO pacote {lib1} foi instalado com sucesso!\033[m')

	TermInstall.status = 'Fim'


def PipInstall():
	libs_pip = ['playwright', 'pywhatkit', 'pyautogui', 
	'SpeechRecognition', 'selenium', 'gtts', 'pyalsaaudio', 'pygame',
	'playsound', 'requests', 'wikipedia', 'emoji', 'opencv-python']

	for lib2 in libs_pip:
		b = sp.run(f'pip3 install {lib2}', shell=True, capture_output=True)
		if (b.returncode != 0):
			print('\033[1;31mFATAL ERROR\033[m')
			print(f"\033[1;31mNao foi possivel installar a biblioteca {lib2}!\033[m")
			exit()
		else:
			print(f"\033[32mA biblioteca {lib2} foi instalada com sucesso!\033[m")

	PipInstall.status = 'Fim'


if os.uname().sysname == 'Linux':
	os.system("clear")
	if os.getuid() != 0:
		print("\033[1;31mVoce DEVE rodar esse programa como superusuario(root)!\033[m")
		print("\033[4;33mSe vc executar como usuario normal isso pode nn funcionar corretamente.\033[m")
		while True:
			escolha = input("\n\nVoce realmente quer rodar como um usuario comum?[Sim/Nao]")
			if (escolha == 'nao') or (escolha == 'Nao') or (escolha == 'n') or (escolha == 'N'):
				exit()
			elif (escolha == 'sim') or(escolha == 'Sim') or (escolha == 's') or (escolha == 'S'):
				print("Prosseguindo....")
				break
			else:
				print("Vc nn digitou uma opcao valida")

	
	thread1 = threading.Thread(target=TermInstall)
	thread2 = threading.Thread(target=PipInstall)
	thread1.start()
	thread2.start()

	while True:
		try:
			if TermInstall.status == 'Fim':
				break
		except:
			pass
	
	while True:
		try:
			if PipInstall.status == 'Fim':
				break
		except:
			pass

	libs_pip2 = ['pyaudio', 'pytesseract']
	for lib in libs_pip2:
		c = sp.run(f'pip install {lib}', shell=True, capture_output=True)
		
		if (c.returncode != 0):
			print(f"\033[1;31mNao foi possivel instalar {lib}!\033[m")
			exit()
		else:
			print(f"\033[32mA biblioteca {lib} foi instalada com sucesso!\033[m")

	print("\n\n\n\033[4;33mInstalando o playwright, isso pode demorar alguns minutos.\033[m")
	print("\033[4;33mPor favor aguarde...\033[m")
	d = sp.run("playwright install", shell=True, capture_output=True)
	
	if (c.returncode != 0):
		print("\033[1;31mNao foi possivel rodar o comando {playwright install}\033[m")
		exit()
	else:
		print("Todas as instalacoes foram concluidas \U0001f609")
		input("Pressione Enter para sair! ")
		sp.run("clear")


elif os.uname().sysname == 'Windows':
	print("coming soon")
