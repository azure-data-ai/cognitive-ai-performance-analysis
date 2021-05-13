import sys
import azure.cognitiveservices.speech as speechsdk

from config import DefaultConfig
from linetimer import CodeTimer

config = DefaultConfig()
audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"


def stt_from_mic_pub_ep():
    speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.service_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("Say Something...")
    return speech_recognizer.recognize_once().text    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.


def stt_from_file_pub_ep(inputAudioFile):
    try:
        speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.service_region)
        audio_input = speechsdk.AudioConfig(filename=inputAudioFile)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        print(speech_recognizer.recognize_once_async().get().text)
    except:
        print(sys.exc_info()[0])
        raise


def stt_from_file_pvt_ep(inputAudioFile):
    try:
        speech_config = speechsdk.SpeechConfig(endpoint=config.privateSTTEndpointUrl, subscription=config.speech_key)
        audio_input = speechsdk.AudioConfig(filename=inputAudioFile)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        result = speech_recognizer.recognize_once_async().get()
        print(result.text)
                
    except:
        print(sys.exc_info()[0])
        raise




with CodeTimer('STT_FILE_PUB_E:'):
    stt_from_file_pub_ep(audio_in)

# with CodeTimer('STT_FILE_PVT_E:'):
#     stt_from_file_pvt_ep(audio_in)