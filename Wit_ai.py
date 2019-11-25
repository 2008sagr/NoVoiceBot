import speech_recognition as sr
import soundfile as sf

def wit_ai():
    try:
        data, samplerate = sf.read('speech.ogg')
        sf.write('speech.wav', data, samplerate)
        f = open('speech.wav', 'rb')
        wav = f.read()
        f.close()
        r = sr.Recognizer()
        WIT_AI_KEY = "PS7JLNHQ22G3IPWIQYZ7BQ6LHZ3WFRTV"
        try:
            text = r.recognize_wit(wav, key=WIT_AI_KEY)
        except:
            print('Ошибка Wit.AI')
    except:
        print("Ошибка модуля Wit.AI")
    return (text)
