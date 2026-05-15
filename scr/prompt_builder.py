def montar_prompt(instrucao, contexto, input_dados, formato_output):

    prompt = f"### CONTEXTO\n{contexto}\n\n" if contexto else ""

    prompt += f"### INSTRUÇÃO\n{instrucao}\n\n"

    prompt += f"### DADOS\n{input_dados}\n\n"

    prompt += f"### FORMATO\n{formato_output}"

    return prompt

def adicionar_exemplos(prompt, exemplos):

    txt = "\n\n### EXEMPLOS"

    for ex in exemplos:

        txt += f"\nInput: {ex['input']}\nOutput: {ex['output']}"

    return prompt + txt

def adicionar_cot(prompt, passos):

    txt = "\n\n### ANALISE PASSO A PASSO"

    for i, p in enumerate(passos, 1):

        txt += f"\n{i}. {p}"

    return prompt + txt
 
src/prompt_builder.py
 
