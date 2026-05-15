def medir_acuracia(resposta, esperado):

    return 1.0 if esperado.lower() in resposta.lower() else 0.0
 
