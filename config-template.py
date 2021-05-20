import os

class DefaultConfig:

  	## Speech SDK API Public service ; config - Replace the below dummy speech_key and service_region.
    speech_key, service_region = "46c52f13e736ehd6yedyh433xxyyz031", "southeastasia"
    
    ## Speech SDK API over web socket secure(wss) with private endpoint 
    # URL Format => {your custom name}.cognitiveservices.azure.com/{speech service offering}/{URL path}
    # Replace {myspeechmaysrv} in below url with your custom name
    privateSTTEndpointUrl = "wss://myspeechmaysrv.cognitiveservices.azure.com/stt/speech/recognition/conversation/cognitiveservices/v1?language=en-US"
    privateTTSEndpointUrl =  "wss://myspeechmaysrv.cognitiveservices.azure.com/tts/cognitiveservices/websocket/v1"
    
    ## Speech Container API
    stt_container_pub_endpoint = "<url>"
    tts_container_pub_endpoint = "<url>"

    ## LUIS config
    intent_key = "<key>"
    intent_service_region = "australiaeast"
    language_understanding_app_id = "<app-id>"