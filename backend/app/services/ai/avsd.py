from transformers import pipeline

# Carregar o modelo pré-treinado
nlp = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

def get_avsd_response(question):
    context = """
    Bem-vindo ao SSDI. O SSDI é uma plataforma que oferece proteção abrangente contra ameaças cibernéticas, 
    gestão de privacidade e um assistente virtual para ajudá-lo com questões de segurança digital.
    """
    result = nlp(question=question, context=context)
    return result['answer']
