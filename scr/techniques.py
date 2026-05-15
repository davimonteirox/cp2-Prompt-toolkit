from src.prompt_builder import montar_prompt, adicionar_exemplos, adicionar_cot

def zero_shot(tarefa, input_data):

    return montar_prompt(tarefa['instrucao'], "", input_data, tarefa['formato_output'])

def few_shot(tarefa, input_data, exemplos):

    p = zero_shot(tarefa, input_data)

    return adicionar_exemplos(p, exemplos) if exemplos else p

def chain_of_thought(tarefa, input_data, passos):

    p = zero_shot(tarefa, input_data)

    return adicionar_cot(p, passos) if passos else p

def role_prompting(tarefa, input_data, persona):

    sys = f"Persona: {persona['nome']}. Especialidade: {persona['especialidade']}."

    user = zero_shot(tarefa, input_data)

    return (sys, user)
 
