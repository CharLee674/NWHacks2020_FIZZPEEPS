# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def getSentiment(entry):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    #strText = u'This was the worst day of my life!'
    #senti = open('sentiments.txt').read()

    f = open("journal1.txt", "w")
    f.write(entry)

    path = 'journal1.txt'
    f = open(path)
    text = f.read()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    f = open("sentiments.txt", "a")
    f.write(str(sentiment.score) + "\n")
    f.close()

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    return sentiment.score