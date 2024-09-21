import google.generativeai as genai
from google.generativeai import  GenerativeModel 
from google.generativeai.protos import FunctionResponse, Tool, Part, Content

class Chat_bot:
    def __init__(self, fns, fn_desc, instructions) :
        self.model = GenerativeModel(
            model_name='gemini-1.5-pro-001',
            tools= Tool(function_declarations=fn_desc),
            system_instruction=instructions
        )
        self.chat = self.model.start_chat()
        self.fuc_dict = fns
    
    def send_prompt(self, p: str):
        response = self.chat.send_message(p, )
        while response.parts[0].function_call:
            content = self.call_functions(response.parts)
            response =self.chat.send_message(content)

        return response.text
    
    def call_functions(self, parts):
        res_parts = []
        for part in parts:
            if fn := part.function_call:
                result = self.fuc_dict[fn.name](**fn.args)
                res_part = Part(
                    function_response=FunctionResponse(
                        name=fn.name,
                        response={'result': result}
                    ))
                res_parts.append(res_part)
        
        return Content(parts=res_parts)