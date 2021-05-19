import sys
import azure.cognitiveservices.speech as speechsdk

from config import DefaultConfig
from linetimer import CodeTimer

config = DefaultConfig()
audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"


def tts_to_mic_pub_ep(textToSynthesize):
    speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.service_region) 
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config) 
    speech_synthesizer.speak_text_async(textToSynthesize).get() 

def tts_to_file_pub_ep(textToSynthesize):
    speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.service_region) 
    speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "./log/log.txt")
    
    audio_output_config = speechsdk.audio.AudioOutputConfig(filename=audio_out)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
    synthesizer.speak_text_async(textToSynthesize).get()

def tts_to_file_pvt_ep(textToSynthesize):
    speech_config = speechsdk.SpeechConfig(endpoint=config.privateTTSEndpointUrl, subscription=config.speech_key)
    audio_output_config = speechsdk.AudioConfig(filename=audio_out)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
    synthesizer.speak_text_async(textToSynthesize).get()

def tts_to_file_container_pub_ep(textToSynthesize):
    speech_config = speechsdk.SpeechConfig(endpoint=config.tts_container_endpoint)
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)
    audio_output_config = speechsdk.audio.AudioOutputConfig(filename=audio_out)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
    synthesizer.speak_text_async(textToSynthesize).get()


# with CodeTimer('TTS_MIC_PUB_E'):
#     tts_to_mic_pub_ep("Please turn off all the lights.")

# with CodeTimer('TTS_FILE_PUB_E'):
#     tts_to_file_pub_ep("Please turn off all the lights.")

# with CodeTimer('TTS_FILE_PVT_E'):
#     tts_to_file_pvt_ep("Please turn off all the lights.")

with CodeTimer('TTS_FILE_CONTAINER_EP'):   
    tts_to_file_container_pub_ep("hello world")