import sys
import azure.cognitiveservices.speech as speechsdk

from config import DefaultConfig
from linetimer import CodeTimer

config = DefaultConfig()
audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"

speech_config = speechsdk.SpeechConfig(endpoint=config.privateTTSEndpointUrl, subscription=config.speech_key)

def tts_to_file(textToSynthesize):
    audio_output_config = speechsdk.AudioConfig(filename=audio_out)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
    #synthesizer.speak_text_async("A simple test to write to a file.")
    synthesizer.speak_text_async(textToSynthesize)
      

with CodeTimer('TTS'):
    tts_to_file('A simple test to write to a file.')

#with CodeTimer('TTS'):
    #tts_to_file(stt_from_file(audio_in))
