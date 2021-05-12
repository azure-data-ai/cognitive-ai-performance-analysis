import sys
import azure.cognitiveservices.speech as speechsdk

from config import DefaultConfig
from linetimer import CodeTimer

config = DefaultConfig()
audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"

speech_config = speechsdk.SpeechConfig(endpoint=config.privateSTTEndpointUrl, subscription=config.speech_key)

def stt_from_file(audioFile):
    try:
        audio_input = speechsdk.AudioConfig(filename=audioFile)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        result = speech_recognizer.recognize_once_async().get()
        print(result.text)
                
    except:
        print(sys.exc_info()[0])
        raise


with CodeTimer('STT'):
    stt_from_file(audio_in)
      

