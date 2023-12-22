import pathlib
import textwrap
import os
import google.generativeai as genai

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')
  
genai.configure(api_key="AIzaSyD5LFvK9nIg-JJXI_lpVn4zsVNjUPCZz4w")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')