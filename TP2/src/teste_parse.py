import ijson

# Example JSON data
json_data = '''
[
{
    "claint": 176640,
    "doc_type": "DESPACHO",
    "number": "15563/2004",
    "dr_number": "182/2004",
    "series": 2,
    "emiting_body": [
        "MINISTRO ADJUNTO-PRESID\u00caNCIA DO CONSELHO DE MINISTROS"
    ],
    "source": "DIARIO DA REPUBLICA - 2.\u00aa SERIE, N\u00ba 182, de 04.08.2004, P\u00e1g. 11661",
    "dre_key": "",
    "in_force": true,
    "conditional": false,
    "processing": false,
    "date": "2004-08-04",
    "notes": "Nomeia representante da parte p\u00fablica na assemb\u00e7eia geral da MOVIJOVEM a licenciada Maria da Concei\u00e7\u00e3o Alves dos Santos Besa Ru\u00e3o Pinto e suplente, nas faltas ou impedimentos daquela, o licenciado Mauro Renato Dias Xavier.",
    "plain_text": "",
    "dre_pdf": "",
    "pdf_error": true,
    "timestamp": "2012-11-10 13:31:32.700522"
},
{
    "claint": 2,
    "doc_type": "AVISO",
    "number": "DD1099/85",
    "dr_number": "110/1985",
    "series": 1,
    "emiting_body": [
        "MINIST\u00c9RIO DOS NEG\u00d3CIOS ESTRANGEIROS"
    ],
    "source": "DIARIO DA REPUBLICA - 1.\u00aa SERIE, N\u00ba 110, de 14.05.1985",
    "dre_key": "19851226@s1",
    "in_force": true,
    "conditional": false,
    "processing": false,
    "date": "1985-05-14",
    "notes": "Torna p\u00fablico ter o embaixador da Rep\u00fablica Hel\u00e9nica na Haia depositado, em conformidade com o artigo 10.\u00ba, segunda al\u00ednea, o instrumento de ratifica\u00e7\u00e3o, pela Gr\u00e9cia da Conven\u00e7\u00e3o Relativa \u00e0 Supress\u00e3o da Exist\u00eancia da Legaliza\u00e7\u00e3o de Actos P\u00fablicos Estrangeiros.",
    "plain_text": "http://digestoconvidados.dre.pt/digesto//pdf/LEX/2/2.PDF",
    "dre_pdf": "http://www.dre.pt/util/getpdf.asp?s=dig&serie=1&iddip=19851226",
    "pdf_error": false,
    "timestamp": "2012-08-16 20:46:39.315403"
}
]
'''


# Define paths to the items you want to extract
paths = {
    "claint": "claint",
    "notes": "notes"
}

# Extract the items from the JSON data
def extract_items(json_data, paths):
    parser = ijson.parse(json_data)
    for prefix, event, value in parser:
        for key, path in paths.items():
            if prefix.endswith(path):
                yield key, value

# Iterate over extracted items and print them
for key, value in extract_items(json_data, paths):
    print(f"{key}: {value}")