import sys
import azure.cognitiveservices.speech as speechsdk

from linetimer import CodeTimer

# speech_key, service_region = "46c25f13ea9447a1be6c7433cf863031", "southeastasia"
# speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_key, service_region = "91c99592e2fb41608478722d3302fef8", "southeastasia"
endpointUrl = "wss://welyspeechmay19.cognitiveservices.azure.com/stt/speech/recognition/conversation/cognitiveservices/v1?language=en-US"

audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"

speech_config = speechsdk.SpeechConfig(endpoint=endpointUrl, subscription=speech_key)

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
      

