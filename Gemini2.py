import pathlib
import textwrap
import os
import google.generativeai as genai
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#1) Downlaod web page and it's content
#2) Prepare to chop piece for appropriate token window
#3) Feed it to the AI to learn

#NOTE: It should work on any given URL

class GeminiParser():

    def __init__(self):
        genai.configure(api_key="AIzaSyD5LFvK9nIg-JJXI_lpVn4zsVNjUPCZz4w")

        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.current_reponse = None
        self.webpage = None
        self.processed_data = []
        self.safety_configs = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        pass

 
    def process_webpage(self, url):
        webpage = requests.get(url)
 
        if(webpage.ok == False):
            print("Server Error or Client Error")
            #return

        #print(webpage.text)
        self.webpage = webpage.text
        
        #-----Divide the downloaded page into chunks------
        token_limit = 30720 - 25720
        token_limit = 3000
        character_limit = token_limit*4
        text_len = len(self.webpage)
        parts = text_len/token_limit

        chunks = []
        chunks.append("")

        def print_chunks(chunk):
            for i in range(len(chunk)):
                print("\x1b[31m {-- \x1b[0m")
                print(chunk[i])
                print("\x1b[31m --} \x1b[0m\n")
                pass
        j = 0

        #print("\x1b[32m", j, "\x1b[0m")
        for i in range(0, text_len):

            if(i == 0):
                chunks[j] += self.webpage[i]
                continue

            if(i % character_limit == 0):
                j += 1
                chunks.append("")
                print("\x1b[32m", j, "\x1b[0m")
            
            
            chunks[j] += self.webpage[i]
            pass
        pass

        
        print_chunks(chunks)
        #-----Feeding extracted chunks into A.I------
        for i in range(0, len(chunks)):
            response = self.model.generate_content("Can you please extract all the text content that reader reads on frontend from this chunk? If text is not present then don't save it " + chunks[i])
            
            try:
                self.processed_data.append(response.text)
            except:
                print(response.text)
                pass
        
        print("\n\n", "len", len(self.processed_data))
        print_chunks(self.processed_data)

    def export_data(self):
        return self.processed_data
        pass
    pass



class Gemini():

    def __init__(self):

        genai.configure(api_key="AIzaSyD5LFvK9nIg-JJXI_lpVn4zsVNjUPCZz4w")

        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.current_response = None
        self.parser = GeminiParser()
        self.safety_configs = [
                 
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
               
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },

            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },

            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }

        ]
        
        print("\033[2J", "\033[H")
        pass
    
    def model_name(self):
        return 'gemini-pro'
    
    def send_message(self, text):
        response = self.chat.send_message(text, safety_settings=self.safety_configs)
        self.current_response = response.text
    
    def print_response(self):
        print("\nA.I >> ", self.get_message())
        print("\n\n")
        pass

    def get_message(self):
        return self.current_response
    
    def print_history(self):
        print(self.chat.history)
    
    def define_safety(self, safety):
        if(isinstance(safety) != list()):
            print("Invalid Safety Configuration")
            return
        self.safety_configs = safety
    
    def set_webpage(self, url):
        self.__context_training__(url)
        pass

    def __context_training__(self, url):
        self.parser.process_webpage(url)
        data = self.parser.export_data()
        
        for i in range(0, len(data)):
            Initiator = "please store this chunks of information of webpage and if chunk doesn't provide information at all then don't store it(don't print anything though in response), got it?" + data[i]
            self.chat.send_message(Initiator)
        pass


ai = Gemini()


#parser = GeminiParser()
#parser.process_webpage("https://jaedon.vercel.app")

#------------------------TRAINING THE A.I----------------------------
URL = "https://jaedon.vercel.app"
#URL = "https://medium.com/mr-ways-guide-to-clash-of-clans/clash-of-clans-the-ultimate-beginners-guide-830f6d7e0a74"
#URL = "https://science.howstuffworks.com/space/aliens-ufos/bob-lazar.htm"
ai.set_webpage(URL)
#-------------------------END OF TRAINING-----------------------------


#"""
while(True):
    print("Webpage Url:= ", URL)
    user_question = input("User >> ")
    if(user_question == "exit"):
        break

    if(user_question == "set url"):
        print("Enter the url of webpage: ")
        URL = input()
        ai.set_webpage(URL)
        print("\n")
        continue
        pass

    ai.send_message(user_question)
    ai.print_response()
    pass
#"""


#NOTE: Need to modify parser to extract content from live DOM and not html