import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

class NeuralNetwork:


    def __init__(self, base_prompt: str | None = None):

        """
        when you initialize a new instance of this class,
        it will set itself up with a 'client' connection to OpenAI
        and an optional 'base_prompt' that will be added before all queries
        """
        
        # the 'client' connection to OpenAI
        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            raise ValueError("OPENAI_API_KEY is not set")
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        # the optional 'base_prompt' that will be added before all queries
        self.base_prompt = base_prompt


    def change_base_prompt(self, base_prompt: str | None):
        """
        This method replaces the 'base_prompt'
        that will be added before all queries.
        """
        self.base_prompt = base_prompt


    def query(self, prompt: str | list[str], max_tokens: int = 1000):
        """
        This method sends a chat completion to
        OpenAI's GPT-3.5 model and returns the response.
        It will prepend the 'base_prompt' if it was set.
        """
        # create the chat messages
        messages = []
        if isinstance(prompt, str):
            messages.append({
                "role": "user",
                "content": prompt,
            })
        else:
            for p in prompt:
                messages.append({
                    "role": "user",
                    "content": p,
                })
        # add the 'base_prompt' if it was set
        if self.base_prompt:
            messages.insert(0, {
                "role": "system",
                "content": self.base_prompt,
            })
        # send the chat completion to OpenAI
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )
        # return the response
        return chat_completion.choices[0].message.content
