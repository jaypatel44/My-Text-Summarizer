import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


text=""" Text summarization plays a crucial role in efficiently condensing large volumes of textual information into concise and informative summaries. 
This paper presents a comprehensive overview of text summarizers, focusing on the two main approaches: extractive and abstractive summarization. 
Extractive summarization involves the selection of important sentences or phrases from the source text, while abstractive summarization aims to generate summaries by understanding the content and producing human-like condensed versions. 
The paper examines the underlying techniques and algorithms used in text summarization, including natural language processing (NLP), machine learning, and deep learning. 
Various evaluation metrics for assessing the quality of summaries are discussed, such as ROUGE scores, semantic similarity, and coherence measures.
 Additionally, the challenges and limitations of text summarization systems, such as handling domain-specific texts or preserving the original meanings are explored. """

def summarizer(rawdocs):
    stopwords =list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)
    tokens = [token.text for token in doc]
    # print(tokens)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] =1
            else:
                word_freq[word.text] +=1
    # print(word_ferq)
    max_freq = max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
    # print(word_freq)
    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)
    sent_scores ={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] =word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    # print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)
    # print(select_len)
    summary = nlargest(select_len,sent_scores,key=sent_scores.get)
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(text)
    # print(summary)
    # print("Length of original text" ,len(text.split(' ')))
    # print("Length of summary text",len(summary.split(' ')))
    return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))




