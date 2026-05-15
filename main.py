import os

import json

import pandas as pd

from src.llm_client import LLMClient

from src.techniques import zero_shot, few_shot, chain_of_thought, role_prompting

from src.evaluator import medir_acuracia

from src.report import gerar_graficos

from src.tasks import obter_tarefas

def main():

    client = LLMClient()

    tarefas_def = obter_tarefas()

    with open('data/inputs.json', 'r') as f:

        inputs_data = json.load(f)

    with open('prompts/system_prompts.json', 'r') as f:

        personas = json.load(f)

    resultados = []

    for chave_tarefa, info_tarefa in tarefas_def.items():

        dados_input = inputs_data.get(chave_tarefa, {}).get('inputs', [])

        for item in dados_input:

            input_texto = item['input']

            esperado = item['esperado']

            tecnicas = {

                "Zero-Shot": zero_shot(info_tarefa, input_texto),

                "Few-Shot": few_shot(info_tarefa, input_texto, info_tarefa.get('exemplos_fewshot')),

                "CoT": chain_of_thought(info_tarefa, input_texto, info_tarefa.get('passos_cot')),

                "Role": role_prompting(info_tarefa, input_texto, personas[info_tarefa['persona']])

            }

            for nome_tec, p_content in tecnicas.items():

                system = p_content[0] if isinstance(p_content, tuple) else ""

                user = p_content[1] if isinstance(p_content, tuple) else p_content

                resp = client.chat(user, system=system)

                acuracia = medir_acuracia(resp['resposta'], esperado)

                resultados.append({

                    "Tarefa": info_tarefa['nome'],

                    "Tecnica": nome_tec,

                    "Acuracia": acuracia,

                    "Tokens": resp['tokens_prompt'] + resp['tokens_resposta'],

                    "Tempo_ms": resp['tempo_ms']

                })

    df = pd.DataFrame(resultados)

    if not os.path.exists('output'): os.makedirs('output')

    df.to_csv("output/resultados.csv", index=False)

    gerar_graficos(df)

if __name__ == "__main__":

    main()
 
