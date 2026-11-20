import azure.cognitiveservices.speech as speechsdk

speech_key = ""
speech_region = "koreacentral"

speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    region=speech_region
)

speech_config.speech_synthesis_voice_name = "en-US-AvaMultilingualNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config
)

text = "Hello! Welcome to Azure Text to Speech my name is koushik at madanapalle institute of technology of science."

result = speech_synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech generated successfully!")

elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details

    print("Speech synthesis canceled:", cancellation.reason)
    print("Error details:", cancellation.error_details)