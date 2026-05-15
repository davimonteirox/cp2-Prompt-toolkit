import requests

import time

import os

class LLMClient:

    def __init__(self):

        self.url = os.getenv("OLLAMA_HOST", "http://localhost:11434/api/chat")

        self.model = "gpt-oss:120b"

    def chat(self, prompt, system="", temp=0.1, max_tokens=500):

        payload = {

            "model": self.model,

            "messages": [

                {"role": "system", "content": system},

                {"role": "user", "content": prompt}

            ],

            "options": {"temperature": temp, "num_predict": max_tokens},

            "stream": False

        }

        try:

            start_time = time.time()

            response = requests.post(self.url, json=payload, timeout=30)

            elapsed_ms = (time.time() - start_time) * 1000

            if response.status_code == 200:

                data = response.json()

                return {

                    "resposta": data['message']['content'],

                    "tokens_prompt": data.get('prompt_eval_count', 0),

                    "tokens_resposta": data.get('eval_count', 0),

                    "tempo_ms": elapsed_ms

                }

        except:

            pass

        return {"resposta": "Erro", "tokens_prompt": 0, "tokens_resposta": 0, "tempo_ms": 0}
 
