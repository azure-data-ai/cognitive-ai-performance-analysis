let sdk = require('microsoft-cognitiveservices-speech-sdk')
let fs = require('fs')

const subscriptionKey = "46c25f13ea9447a1be6c7433cf863031";
const serviceRegion = "southeastasia"; 
const filename = "./audio-in/3s.wav";

const speechConfig = sdk.SpeechConfig.fromSubscription(subscriptionKey, serviceRegion); 

function recognizeFromFile() {
  
  let audioConfig = sdk.AudioConfig.fromWavFileInput(fs.readFileSync(filename));
  let recognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);

  recognizer.recognizeOnceAsync(result => {
    console.log(`RECOGNIZED: Text=${result.text}`);
    recognizer.close();
  });
}


//Synthesize to File
const outputFile = "./audio-out/tts-output.wav"
function synthesizeToAudioFile(textToSynthesize) {
  const audioConfig = sdk.AudioConfig.fromAudioFileOutput(outputFile);
  const synthesizer = new sdk.SpeechSynthesizer(speechConfig, audioConfig);
  synthesizer.speakTextAsync(
    textToSynthesize,
      result => {
          synthesizer.close();
          if (result) {
              // return result as stream
              return fs.createReadStream(outputFile);
          }
      },
      error => {
          console.log(error);
          synthesizer.close();
      });
}


function callSync() {
  console.time('STT Time :');
  recognizeFromFile();
  console.timeEnd('STT Time :');

  console.time('TTS Time :');
  synthesizeToAudioFile("Please turn off all the lights.");
  console.timeEnd('TTS Time :');

  // console.time('Combined Time :');
// synthesizeSpeech(recognizeFromFile());
// console.timeEnd('Combined Time :');
}

callSync();