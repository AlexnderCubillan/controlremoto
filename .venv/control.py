# Instala las bibliotecas si aún no lo has hecho
# pip install speechrecognition selenium

import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import apagarpc
# Configura el navegador (en este caso, Chrome)
driver = webdriver.Chrome()

# Abre la página web deseada
driver.get('https://airtek.tv/')

# Función para seleccionar elementos por voz
def select_element_by_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Dime qué elemento deseas seleccionar o di "cerrar" para terminar...')
        audio = recognizer.listen(source)

    try:
        # Reconoce el comando de voz
        command = recognizer.recognize_google(audio, language="es-ES")
        print(f'Comando de voz: {command}')

        # Cierra el navegador y termina el programa si el comando de voz es "cerrar"
        if "Carola cerrar" in command:
            print('Cerrando el navegador y finalizando el programa...')
            driver.quit()
            return "EXIT"  # Devuelve un indicador para finalizar el programa

        # Aquí puedes definir los comandos y las acciones correspondientes
        if "Carola Sony" in command:
            # Encuentra y haz clic en el botón de inicio
            start_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/section/div[2]/div/div[1]/div[4]/div/div/img'))
            )
            start_button.click()

        if "Carola next" in command:
            # Encuentra y haz clic en el botón de inicio
            start_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/section/div[2]/div/div[1]/div[5]/div/div/img'))
            )
            start_button.click()

        if "Carola back" in command:
            # Encuentra y haz clic en el botón de inicio
            start_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/section/div[2]/div/div[2]'))
            )
            start_button.click()
            start_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/section/div[2]/div/div[1]/div[4]/div/div/img'))
            )
            start_button.click()

        if "Carola dormir" in command:
            # Encuentra y haz clic en el botón de inicio
            apagarpc.apagar_pc()
        # Agrega más comandos según tus necesidades

    except sr.UnknownValueError:
        print('No te he entendido, por favor intenta de nuevo.')
    except sr.RequestError as e:
        print(f'Error al procesar el audio: {e}')

# Ejecuta la función en un bucle para que puedas seguir dando comandos
while True:
    if select_element_by_voice() == "EXIT":
        break  # Sale del bucle y termina el programa