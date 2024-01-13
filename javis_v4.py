import openai
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Set your OpenAI GPT API key
openai.api_key = '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'

def text_generation(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # Use the GPT-3 engine
        prompt=prompt,
        max_tokens=100
    )
    return response['choices'][0]['text'].strip()

def speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speech_synthesis(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    playsound("output.mp3")

def main():
    while True:
        # Step 1: Speech Recognition
        user_input = speech_recognition()

        # Break the loop if no user input is detected
        if not user_input:
            break

        # Step 2: Text-to-Text Generation
        ai_response = text_generation(user_input)

        # Step 3: Speech Synthesis
        print(f"AI: {ai_response}")
        speech_synthesis(ai_response)

if __name__ == "__main__":
    main()
