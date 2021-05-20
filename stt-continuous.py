import sys
import time
import azure.cognitiveservices.speech as speechsdk

from config import DefaultConfig
from utility import CodeTimer, getUserInput

config = DefaultConfig()


def stt_continuous_mic_pub_ep():
    speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.service_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("Say Something...")

    done = False
    
    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
    
    with CodeTimer('TTS_FILE_CONTAINER_PUB_EP'):
        speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt.result.text)))
    with CodeTimer('TTS_FILE_CONTAINER_PUB_EP'):
        speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt.result.text)))

    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)
    
    speech_recognizer.start_continuous_recognition()
    
    while not done:
        time.sleep(.5)

    # speech_recognizer.stop_continuous_recognition()    


stt_continuous_mic_pub_ep()
