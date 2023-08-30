from google.cloud import language_v1


def analyze_entities(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(request={'document': document})
    
    entities = []
    for entity in response.entities:
        entities.append({
            'name': entity.name,
            'type': language_v1.Entity.Type(entity.type_).name,
            'salience': entity.salience,
        })
    
    return entities

if __name__ == '__main__':
    texts = [
        "El río Amazonas es el río más largo de América del Sur.",
        "La Mona Lisa fue pintada por Leonardo da Vinci.",
    ]
    
    for text in texts:
        entities = analyze_entities(text)
        print(f"Entidades en el texto: '{text}':")
        for entity in entities:
            print(f"Nombre: {entity['name']}, Tipo: {entity['type']}, Importancia: {entity['salience']}")
        print("=" * 50)
