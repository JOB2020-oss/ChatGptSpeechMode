import streamlit as st
import speech_recognition as sr
import openai
import config
import pyttsx3
import time
model_engine = "text-davinci-003" 
openai.api_key = "Your api key here...."


def get_gpt_response(request):
	raw_results = openai.Completion.create(
		engine = model_engine,
		prompt = request, # A request to be sent
		max_tokens = 2000,
		n = 1,
		temperature = 0.5
		)
	results = raw_results.choices[0].text
	return results

def get_voice():
	r = sr.Recognizer()
	with sr.Microphone() as src:
		with st.spinner("Speak now then wait for me !!!!: "):
		    audio_data = r.listen(src)
		    txt = r.recognize_google(audio_data)
	with st.spinner("Fetching your results prepare another Question"):
		response = get_gpt_response(txt)
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		engine.setProperty('voice',voices[1].id)
		engine.say(response)
		engine.runAndWait()
		time.sleep(1)

with st.sidebar:
	butt1 = st.checkbox("START")
	st.markdown("1.Press Ask")
	st.markdown("2.Talk while spining speak now")
	st.markdown("3.Wait while fetching results")
	st.markdown("4.Repeat procedure 1")
st.header("TALK WITH CHATGPT")	
st.success("Welcome to simple ChatGpt speech conversation demo where you can talk directly with ChatGpt and perform range of things.Just just talk rather than typing!.Its simple just press ASK button!!!!! have fun!!!!!!")
if butt1:
	if st.button("ASK"):
		get_voice()

if __name__ == "main":
	app.run()