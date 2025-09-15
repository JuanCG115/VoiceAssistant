Sabina: Your Personal Voice Assistant

This Python script is a voice-activated personal assistant named Sabina. Using libraries like pyttsx3 for text-to-speech and speech_recognition for speech-to-text, it can listen to user commands and perform various tasks. It's a great example of an interactive application that bridges the gap between spoken language and digital actions.

Core Features

- Voice Interaction: Recognizes spoken commands and responds with a synthetic voice.

- Web Browsing: Opens websites like YouTube and Google.

- Information Retrieval:

  - Wikipedia: Searches and summarizes Wikipedia articles.

  - Google Search: Uses a web browser to perform a search for a given query.

  - Financial Data: Fetches and reads out the real-time stock prices of major companies like Apple, Amazon, and Google.

- Entertainment & Utilities:

  - Music: Plays a requested song or video on YouTube.

  - Jokes: Tells a random joke.

  - Time & Date: Announces the current day of the week and the time.

Requirements and Installation

To run this assistant, you'll need a working microphone and the following Python libraries. You can install them using pip:

    Bash
    
    pip install pyttsx3 SpeechRecognition pywhatkit yfinance pyjokes wikipedia
    
How to Use

- Run the script: Execute the script from your terminal.

- Speak your command: The assistant will greet you and then wait for your voice commands. Just say what you need, like "reproducir" (to play music) or "busca en internet" (to search the web).

- Say "adiós" to exit: The program will stop running when you say "adiós".

How to Change the Voice Language

1. To change Sabina's voice to another language, you must modify the voice ID within the speak() function.

2. Uncomment the line engine.setProperty('voice', id1) so the code can use a specific voice.

3. Identify the voice IDs available on your operating system. You can find a complete list by running a simple Python script using pyttsx3.

  Assign the desired voice ID to the engine.setProperty('voice', id).

Here is how it would look in your code:

    Python
    
    def speak(mensaje):
        engine = pyttsx3.init()
        # Uncomment and change the voice ID
        # Voice ID for Spanish: "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
        # Voice ID for English: "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', "VOICE_ID_HERE")
        engine.say(mensaje)
        engine.runAndWait()

"The code in this repository is based on lessons from Federico Garay's course."
