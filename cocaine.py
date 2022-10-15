import subprocess as sp
from multiprocessing.pool import ThreadPool

libs_pip = ['playwright', 'pywhatkit', 'pyautogui', 'SpeechRecognition',
'selenium', 'gtts', 'pyalsaaudio', 'pygame', 'playsound', 'requests', 
'wikipedia', 'emojis', 'opencv-python']

libs_t = ['tesseract-ocr', 'libtesseract-dev', 'tesseract-ocr-por',
'libasound-dev', 'portaudio19-dev', 'libportaudio2', 'libportaudiocpp0']

pool = ThreadPool(processes=1)
def TermInstall():
	sp.run('sudo apt -y update', shell=True, capture_output=True)
	sp.run("wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz", shell=True, capture_output=True)
	sp.run("tar -xvzf geckodriver-v0.30.0-linux64.tar.gz", shell=True, capture_output=True)
	sp.run("mv geckodriver /usr/bin", shell=True, capture_output=True)
	sp.run("rm -f -r -d -v geckodriver-v0.30.0-linux64.tar.gz",shell=True, capture_output=True)
	for lib1 in libs_t:
		a = sp.run(f'sudo apt -y install {lib1}', shell=True, capture_output=True)
		if a.returncode != 0:
			print(f'Nao foi possivel installar:  [{lib1}]')
			return 0
		else:
			print(f'A biblioteca {lib1} foi instalada com sucesso!')

		
def PipInstall():
	async_call = pool.apply_async(TermInstall)
	for lib2 in libs_pip:
		b = sp.run(f'pip3 install {lib2}', shell=True, capture_output=True)
		if (b.returncode != 0):
			print('FATAL ERROR')
			print(f"Nao foi possivel installar a biblioteca {lib2}")
			return 0
		else:
			print(f"A biblioteca {lib2} foi instalada com sucesso!")


retorno = PipInstall()

libs_pip2 = ['pyaudio', 'pytesseract']
for lib in libs_pip2:
	#async_call = pool.apply_async(TermInstall)
	c = sp.run(f'pip install {lib}', shell=True, capture_output=True)
	if (c.returncode != 0):
		print(f"Nao foi possivel instalar {lib}")
		exit()
	else:
		print(f"A biblioteca {lib} foi instalada com sucesso")

sp.run("playwright install", shell=True, capture_output=True)
print("Todas as instalacoes foram concluidas ;)")
input("Digite qualquer coisa para sair: ")
sp.run("clear")
