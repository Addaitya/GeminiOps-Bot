import os
from dotenv import load_dotenv
import google.generativeai as genai


from lib.actions import search_wikipedia, calculate, currency
from lib.fun_declare import wiki_search_desc, calculate_desc, currency_desc
from lib.chatbot import Chat_bot

load_dotenv()
gemini_api_key = os.getenv('API_KEY')
genai.configure(api_key=gemini_api_key)


instructions = """
You are a chatbot who answers questions. 
Tasks: 
1. If fact related questions are asked, you will search on Wikipedia and based on the search result give answer to user.
2. If mathematical operations are asked you will use calculator function to pass the expression in string format. Answer user question in 'a+b = c' format.
3. If user ask about the exchange rate and which currency they are converting from and converting to search for current currency rates. 
For example, if user ask 'convert 65 usd to inr' first search for currency exchange rate then use calcuator to compute answer and give it.  
Do not perform any other tasks.
""".replace('\n', ' ')
    
functions = {
    'wikipedia_search': search_wikipedia,
    'calculate_expression': calculate,
    'get_exchange_rate': currency
}

function_declarations = [wiki_search_desc, calculate_desc, currency_desc]


bot = Chat_bot(functions, function_declarations, instructions)

print(bot.send_prompt("Convert 23 usd to inr"))

def query(max_turns=5):
    i = 0
    bot = Chat_bot(functions, function_declarations, instructions)
    while i < max_turns:
        next_prompt = input("User: ")
        i += 1
        result = bot.send_prompt(next_prompt)
        print(f"Bot: {result} \n")