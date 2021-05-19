#!/bin/bash

## Run this in bash shell ###

read -p "SUBSCRIPTION_KEY: " subscriptionKey

# echo  $subscriptionKey

### Speech-to-Text #######

# curl --location --request POST 'https://southeastasia.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US' \
# --header 'Ocp-Apim-Subscription-Key: 46xxxxyyyyyy47azzzzyy6c74ffggs31' \
# --header 'Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000' \
# --data-binary @'./audio-in/3s.wav'

time curl --location --request POST 'https://southeastasia.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US' \
--header "Ocp-Apim-Subscription-Key: $subscriptionKey" \
--header 'Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000' \
--data-binary @'./audio-in/1s.wav'


### Text-to-Speech ######

# curl --location --request POST 'https://southeastasia.tts.speech.microsoft.com/cognitiveservices/v1' \
# --header 'Ocp-Apim-Subscription-Key: 46xxxxyyyyyy47azzzzyy6c74ffggs31' \
# --header 'Content-Type: application/ssml+xml' \
# --header 'X-Microsoft-OutputFormat: audio-16khz-128kbitrate-mono-mp3' \
# --header 'User-Agent: curl' \
# --data-raw '<speak version='\''1.0'\'' xml:lang='\''en-US'\''>
#     <voice xml:lang='\''en-US'\'' xml:gender='\''Female'\'' name='\''en-US-AriaRUS'\''>
#         Please turn off all the lights.
#     </voice>
# </speak>' > ./audio-out/rest-output.wav

time curl --location --request POST 'https://southeastasia.tts.speech.microsoft.com/cognitiveservices/v1' \
--header "cp-Apim-Subscription-Key: $subscriptionKey" \
--header 'Content-Type: application/ssml+xml' \
--header 'X-Microsoft-OutputFormat: audio-16khz-128kbitrate-mono-mp3' \
--header 'User-Agent: curl' \
--data-raw '<speak version='\''1.0'\'' xml:lang='\''en-US'\''>
    <voice xml:lang='\''en-US'\'' xml:gender='\''Female'\'' name='\''en-US-AriaRUS'\''>
        Please turn off all the lights.
    </voice>
</speak>' > ./audio-out/rest-output.wav