def obter_tarefas():
   return {
       "classificacao_sentimento": {
           "nome": "Análise de Sentimento",
           "instrucao": "Classifique como POSITIVO ou NEGATIVO",
           "formato_output": "Apenas a palavra",
           "persona": "analista_cx",
           "passos_cot": ["Sinta o tom", "Classifique"],
           "exemplos_fewshot": [{"input": "Bom", "output": "POSITIVO"}]
       }
   }
