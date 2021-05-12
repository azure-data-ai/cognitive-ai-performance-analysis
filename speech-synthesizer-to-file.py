import sys
import azure.cognitiveservices.speech as speechsdk

from linetimer import CodeTimer

# speech_key, service_region = "46c25f13ea9447a1be6c7433cf863031", "southeastasia"
# speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_key, service_region = "91c99592e2fb41608478722d3302fef8", "southeastasia"
endpointUrl = "https://welyspeechmay19.cognitiveservices.azure.com/voice/cognitiveservices/v1?deploymentId=905e3e23-f1c7-4405-9f4b-5bb9487ed57f"

audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"

speech_config = speechsdk.SpeechConfig(endpoint=endpointUrl, subscription=speech_key)

def tts_to_file(textToSynthesize):
    audio_output_config = speechsdk.AudioConfig(filename=audio_out)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
    #synthesizer.speak_text_async("A simple test to write to a file.")
    synthesizer.speak_text_async(textToSynthesize)
      

with CodeTimer('TTS'):
    tts_to_file('A simple test to write to a file.')

#with CodeTimer('TTS'):
    #tts_to_file(stt_from_file(audio_in))
