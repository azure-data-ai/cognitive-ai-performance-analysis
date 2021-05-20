# cognitive-ai-performance-test
This repo had modules to compare and demonstrate the performance / response time of cognitive services API

## Getting Started
* ```git clone https://github.com/azure-data-ai/cognitive-ai-performance-test.git ```
* Rename ```config-template.py``` to ```config.py``` and add/update all the required properties/key/urls in the config.py
* Run ```pip install -r requirements.txt```

## Module Description
  | Module | Description|
  |-------------|------------|
  |speech-recognizer.py  | Speech-to-text functions for the scenarios - input from mic, input from files, speech-to-text service over private endpoint, speech-to-text container service etc. |
  |speech-synthesizer.py | Text-to-speech functions for - output to mic, output to file, text-to-speech with private endpoint, text-to-speech container api|
  |speech-luis.py        | combination of speech and luis services for intent recognition|
  |stt-continuous.py     | continuous streaming speech recognition |
  |speech-rest-api.sh    | Rest API call response test for speech-to-text and text-to-speech |

## Cognitive Services Performance Test Scenario
* Public IP and Internet
* Through Private Endpoint
* Container API with Public and Private IP
* Combination and Asynchronous interactions of API

 To be updated ...

## Test cases and observations
   (Excel Document) To Be updated ...

## Conclusion
    To be updated ...
    
## System set up
System config :
OS:

  To be updated :

## Notes:
* Install 'MS Visual C++ redistributable' while setting up new VM
