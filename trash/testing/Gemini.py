import pathlib
import textwrap
import os
import google.generativeai as genai
import json



#Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
#
##response = model.generate_content("What is the meaning of life?")


genai.configure(api_key="AIzaSyD5LFvK9nIg-JJXI_lpVn4zsVNjUPCZz4w")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


model = genai.GenerativeModel('gemini-pro')
#Creating context for the AI


#Training the AI with details
file = open("Data.json", "r")
context = json.load(file)["details"]

user_data = [json.dumps(context, indent=4)]
#response = model.start_chat(history=user_data)

Initiator = "please store this information(don't print it though in response), got it?" + user_data[0]
#response = model.generate_content()
#print(response.text)
#response = model.generate_content(Initiator + "Who is the author by the way?")

while(True):
  question = input("Enter your question: ")
  if(question == "exit"):
    break

  response = model.generate_content(Initiator + question)
  print("Answer:= ", response.text)
  print("\n\n")
  pass


#What exactly happens when prompted

