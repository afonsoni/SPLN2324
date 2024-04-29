from transformers import pipeline

context = """Afinal, as obras no Jardim Teófilo Braga, na Praça da República, só avançam depois do início do terceiro trimestre de 2024. O “refúgio da sueca” continua assim, aberto, pelo menos até julho, altura em que deverão arrancar as obras de requalificação do espaço.
Após a publicação da notícia, que anunciava para breve o encerramento do jardim, a Câmara Municipal do Porto retificou a informação que havia enviado ao Porto Canal, relativamente ao início da empreitada.
As novas informações apontam que a obra nunca avançará antes do terceiro trimestre do ano, ou seja, só a partir de julho é que a requalificação do Jardim de Teófilo Braga, na Praça da República, deverá arrancar, não havendo, para já, uma data precisa.
O Jardim de Teófilo Braga vai ser alvo de intervenção, num investimento feito pela autarquia, cujo orçamento rondará os 1,5 milhões de euros.
A intervenção tem um prazo previsto de 300 dias, segundo avançou o vice-presidente do executivo, na apresentação do projeto.
“Este é um projeto que vem na sequência daquilo que temos feito ao longo dos últimos anos de requalificação, de recuperação de expansão de muitas das áreas verdes da cidade” começou por explicar o vereador com o pelouro do Ambiente e Transição Climática.
“A Praça da República é muito especial para a cidade, mas está num estado de degradação muito adiantado e por isso é um bom dia para o Porto perceber que estamos a breve trecho a lançar o concurso”, frisou Filipe Araújo."
"""
perguntas = ["Quando começam as obras?", "Onde fica o jardim Teófilo Braga?", "Qual o orçamento da empreitada?", "Quem é o vice-presidente do executivo?", "Quem é o vereador com o pelouro do Ambiente e Transição Climática?", "Qual o prazo previsto para a intervenção?"]

question_answerer = pipeline("question-answering", model = "lfcc/bert-portuguese-squad")
for p in perguntas:
    print(f"Question: {p}")
    result = question_answerer(question=p, context=context)
    print(f"Score: {result['score']} | {result['answer']}")
