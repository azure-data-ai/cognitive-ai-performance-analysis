import sys
import azure.cognitiveservices.speech as speechsdk

from config import DefaultConfig
from utility import CodeTimer, getUserInput

config = DefaultConfig()

lampfilename = "./audio-in/3s.wav"

def recognize_intent_once_from_mic():
    intent_config = speechsdk.SpeechConfig(subscription=config.intent_key, region=config.intent_service_region)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    intent_recognizer = speechsdk.intent.IntentRecognizer(speech_config=intent_config, audio_config=audio_config)
    print("Say Something...")
    
    # set up the intents that are to be recognized. These can be a mix of simple phrases and
    # intents specified through a LanguageUnderstanding Model.
    model = speechsdk.intent.LanguageUnderstandingModel(app_id=config.language_understanding_app_id)
    intents = [
        (model, "HomeAutomation.TurnOn"),
        (model, "HomeAutomation.TurnOff"),
        ("This is a test.", "test"),
        ("Switch to channel 34.", "34"),
        ("what's the weather like", "weather"),
    ]
    intent_recognizer.add_intents(intents)

    intent_result = intent_recognizer.recognize_once()
    print(intent_result.text)


    # Check the results
    if intent_result.reason == speechsdk.ResultReason.RecognizedIntent:
        print("Recognized: \"{}\" with intent id `{}`".format(intent_result.text, intent_result.intent_id))
    elif intent_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(intent_result.text))
    elif intent_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(intent_result.no_match_details))
    elif intent_result.reason == speechsdk.ResultReason.Canceled:
        print("Intent recognition canceled: {}".format(intent_result.cancellation_details.reason))
        if intent_result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(intent_result.cancellation_details.error_details))
    # </IntentRecognitionOnceWithMic>


def recognize_intent_once_from_file():
    """performs one-shot intent recognition from input from an audio file"""
    # <IntentRecognitionOnceWithFile>
    try:
        intent_config = speechsdk.SpeechConfig(subscription=config.intent_key, region=config.intent_service_region)
        audio_config = speechsdk.audio.AudioConfig(filename=lampfilename)

        intent_recognizer = speechsdk.intent.IntentRecognizer(speech_config=intent_config, audio_config=audio_config)

        model = speechsdk.intent.LanguageUnderstandingModel(app_id=config.language_understanding_app_id)
        intents = [
            (model, "HomeAutomation.TurnOn"),
            (model, "HomeAutomation.TurnOff"),
            ("This is a test.", "test"),
            ("Switch to the channel 34.", "34"),
            ("what's the weather like", "weather"),
            ("Please turn off the light", "turn off" )
        ]
        intent_recognizer.add_intents(intents)

        intent_result = intent_recognizer.recognize_once()
        print(intent_result.text)
    except:
        print(sys.exc_info()[0])
        raise

# with CodeTimer('INTENT REC:'):
#     recognize_intent_once_from_mic()

with CodeTimer('INTENT REC:'):
    recognize_intent_once_from_file()