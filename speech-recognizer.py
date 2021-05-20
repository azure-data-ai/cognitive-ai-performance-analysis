import sys
import azure.cognitiveservices.speech as speechsdk

from config import DefaultConfig
from utility import CodeTimer, getUserInput

config = DefaultConfig()
audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"


def stt_from_mic_pub_ep():
    try:
        speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.service_region)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        print("Say Something...")
        return speech_recognizer.recognize_once().text    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    except RuntimeError:
        print('\033[41m EXCEPTION: MIC NOT AVAILABLE \033[0m')

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


def stt_from_file_container_pub_ep(inputAudioFile):
    try:
        speech_config = speechsdk.SpeechConfig(endpoint=config.stt_container_pub_endpoint)
        audio_input = speechsdk.AudioConfig(filename=inputAudioFile)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        result = speech_recognizer.recognize_once_async().get()
        print(result.text)
                
    except:
        print(sys.exc_info()[0])
        raise

def stt_from_file_container_pvt_ep(inputAudioFile):
    try:
        speech_config = speechsdk.SpeechConfig(endpoint=config.stt_container_pvt_endpoint)
        audio_input = speechsdk.AudioConfig(filename=inputAudioFile)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        result = speech_recognizer.recognize_once_async().get()
        print(result.text)
                
    except:
        print(sys.exc_info()[0])
        raise


options = ["STT SDK - TO MIC - PUBLIC API",   
        "STT SDK - TO FILE - PUBLIC API", 
        "STT SDK - TO FILE - PRIVATE ENDPOINT" , 
        "STT SDK - TO FILE - CONTAINER - PUBLIC EP",
        "STT SDK - TO FILE - CONTAINER - PRIVATE EP"]

def executeModule():
    option = getUserInput(options)
    print(f'Executing option: {option}')
    if option == 1:
        with CodeTimer('STT_MIC_PUB_E:'):
            print(stt_from_mic_pub_ep())
    elif option == 2:
        with CodeTimer('STT_FILE_PUB_E:'):
            stt_from_file_pub_ep(audio_in)
    elif option == 3:
        with CodeTimer('STT_FILE_PVT_E:'):
            stt_from_file_pvt_ep(audio_in)
    elif option == 4:
        with CodeTimer('STT_FILE_CONTAINER_PUB_EP:'):
            stt_from_file_container_pub_ep(audio_in)   
    elif option == 5:
        with CodeTimer('STT_FILE_CONTAINER_PVT_EP'):   
            stt_from_file_container_pvt_ep(audio_in)
    else:
        print('Invalid choice')


executeModule()




 