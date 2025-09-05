import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from wikipedia import languages

# Opciones de voz-idioma
# id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
# id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# id3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# Escuchar nuestro microfono y devolver audio como texto
def speech2text():

    # Almacenar el recognizer en una variable
    r = sr.Recognizer()

    # Configurar microfono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 1.3

        # Informa que se comenzo la grabacion
        print('En qué puedo ayudarte')

        # Guardar audio
        audio = r.listen(origen)

        try:
            # Buscar en Google
            pedido = r.recognize_google(audio, language='es-mx')

            # Prueba ingreso
            print('Dijiste: ' + pedido)

            # Devolver pedido
            return pedido

        # En caso de no comprender audio
        except sr.UnknownValueError:

            # Prueba de que no comprendio audio
            speak('Podrías repetirlo')

            # Devolver error
            return 'Sigo esperando'

        # En caso de no resolver pedido
        except sr.RequestError:

            # Prueba de que no comprendio audio
            speak('Lo siento, aún no puedo hacer eso')

            # Devolver error
            return 'Sigo esperando'

        # Error inesperado
        except:

            # Prueba de que no comprendio audio
            speak('Algo ha malido sal')

            # Devolver error
            return 'Sigo esperando'

# Funcio para que el asistente hable
def speak(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    # engine.setProperty('voice', id1)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar dia de la semana
def pedir_dia():

    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear una variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombres de los dias
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sábado',
                  6:'Domingo'}

    # Decir el dia de la semana
    speak(f'Hoy es {calendario[dia_semana]}')

# Informar hora
def pedir_hora():

    # Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # Decir hora
    speak(hora)

# Saludo inicial
def saludo():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif  6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    speak(f'{momento}, soy Sabina, tu asistente personal')

# Funcion central de Asistente
def pedidos():

    # Activar saludo inicial
    saludo()

    # Variable de corte
    comenzar = True

    # Loop central
    while comenzar:

        # Activar el microfono y guardar el pedido en un string
        pedido = speech2text().lower()

        if 'youtube' in pedido:
            speak('De acuerdo, estoy en ello')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'google' in pedido:
            speak('De acuerdo, estoy en ello')
            webbrowser.open('https://www.google.com.mx/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            try:
                speak('Buscando eso en wikipedia')
                pedido = pedido.replace('busca en wikipedia', '')
                wikipedia.set_lang('es')
                resultado = wikipedia.summary(pedido, sentences=1)
                speak('Wikipedia dice lo siguiente: ')
                speak(resultado)
            except wikipedia.exceptions.DisambiguationError:
                speak('Lo siento, debes ser mas especifico')
            except wikipedia.exceptions.PageError:
                speak('Lo siento, no encontre lo que buscabas')
            except wikipedia.exceptions.WikipediaException:
                speak('Lo siento, ocurrió algo inesperado')
            continue
        elif 'busca en internet' in pedido:
            speak('Estoy en ello')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            speak('Esto es lo que encontre')
            continue
        elif 'reproducir' in pedido:
            speak('Claro, en este momento lo reproduzco')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            speak(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                      'amazon':'AMZN',
                      'google':'GOOGL'}
            try:
                accion_buscar = cartera[accion]
                accion_buscar = yf.Ticker(accion_buscar)
                precio_actual = accion_buscar.info['regularMarketPrice']
                speak(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                speak('Perdon pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            speak('Hasta luego, recuerda que si necesitas algo más estaré aquí para ayudarte')
            break

pedidos()
