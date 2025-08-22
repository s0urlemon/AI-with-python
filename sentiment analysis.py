from textblob import TextBlob

text="""
I love programming.
Python is really easy to learn.
But sometimes debugging can be frustrating.
Overall,coding makes me happy!
"""
print("Input text:\n",text)

blob=TextBlob(text)
sentences=blob.sentences

print('\nSentence wise Sentiment Analysis:')
for i,sentence in enumerate(sentences,1):
    polarity=sentence.sentiment.polarity
    subjectivity=sentence.sentiment.subjectivity

    if polarity>0:
        sentiment_label="Positive 😊"
    elif polarity<0:
        sentiment_label="Negative 😞"    
    else:
        sentiment_label="Neutral 😐"

    print(f"{i}.{sentence}")
    print(f"Polarity:{polarity},Subjectivity:{subjectivity} ➡ {sentiment_label}")

avg_polarity=sum(s.sentiment.polarity for s in sentences)/len(sentences)
print("\nOverall average polarity",avg_polarity)

if avg_polarity>0:
    print("Overall sentiment:Positive 😊")
elif avg_polarity<0:
    print("Overall sentiment:Negative 😞")
else:
    print("Overall sentiment:Neutral 😐")