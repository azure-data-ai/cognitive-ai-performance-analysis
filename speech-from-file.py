import sys
import time
import azure.cognitiveservices.speech as speechsdk

from linetimer import CodeTimer

# speech_key, service_region = "46c25f13ea9447a1be6c7433cf863031", "southeastasia"
# speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_key, service_region = "91c99592e2fb41608478722d3302fef8", "southeastasia"
endpointUrl = "wss://welyspeechmay19.cognitiveservices.azure.com/stt/speech/recognition/conversation/cognitiveservices/v1?language=en-US"
# endpointUrl = "https://welyspeechmay19.cognitiveservices.azure.com/voice/cognitiveservices/v1?deploymentId=905e3e23-f1c7-4405-9f4b-5bb9487ed57f"
speech_config = speechsdk.SpeechConfig(endpoint=endpointUrl, subscription=speech_key)

audio_in = "./audio-in/3s.wav"
audio_out = "./audio-out/tts-output.wav"

def stt_from_file(audioFile):
    try:
        audio_input = speechsdk.AudioConfig(filename=audioFile)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        
        
       # result = ['result1', 'result2','result3', 'result4','result5', 'result6','result7', 'result8','result9', 'result10', 'result11', 'result12']
        i = 0
        while i < 1 :
           # resultName = 'Result'
            with CodeTimer('RESULT-' + str(i)):
                result = speech_recognizer.recognize_once_async().get()
                print(result.text)
                i += 1
               # time.sleep(30)

        # with CodeTimer('RESULT-2'):
        #     result2 = speech_recognizer.recognize_once_async().get()
        #     print(result2.text)
    except:
        print(sys.exc_info()[0])
        raise



def tts_to_file(textToSynthesize):
    audio_output_config = speechsdk.AudioConfig(filename=audio_out)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
    #synthesizer.speak_text_async("A simple test to write to a file.")
    synthesizer.speak_text_async(textToSynthesize)

#with CodeTimer('STT'):
stt_from_file(audio_in)
      

# with CodeTimer('TTS'):
#     tts_to_file('A simple test to write to a file.')

#with CodeTimer('TTS'):
    #tts_to_file(stt_from_file(audio_in))
