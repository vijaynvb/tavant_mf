import os
import azure.cognitiveservices.speech as speechsdk #pip install azure-cognitiveservices-speech
from dotenv import load_dotenv

load_dotenv()

speech_key = os.getenv("SPEECH_KEY")
speech_region = os.getenv("SPEECH_REGION")

print("Speech Key: " + speech_key)
print("Speech Region: " + speech_region)

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='hi-IN-AnanyaNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want to speak >")
text = "कर्नाटक भारत के दक्षिण-पश्चिमी क्षेत्र में स्थित एक विशाल और सांस्कृतिक रूप से समृद्ध राज्य है। इसकी मुख्य भाषा कन्नड़ है, जो द्रविड़ भाषा परिवार की सबसे पुरानी और प्रभावशाली भाषाओं में से एक है।"
# text = input()

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")