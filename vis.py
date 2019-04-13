from reddit import scrape_reddit_politics
import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import spacy

def generate_word_cloud(reddit=True):

    #open database connection
    conn = sqlite3.connect('Final.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT title FROM Reddit')
    title_list = cur.fetchall()

    #natural language processing
    nlp = spacy.load("en_core_web_sm")

    #all_words = []
    words_dict = {}
    #words to ignore in most common
    ignore = ['to', 'of', 'in', 'is', 'on', 'and', 'for', 'it', 'as', 'a', 'not', "n't", "that", "the", "or", "with", "are", "we", "’s", "'s", "his", "say", "says", "from", "do", "be", "he", "i", "out", "at", "after", "new", "about", "by", "was", "has"]

    for tup in title_list:
        #words = tup[0].split()
        doc = nlp(tup[0])
        for token in doc:
            word = token.text
            word = word.rstrip('.')
            word = word.lower()

            if not word in ignore and not token.is_punct:
                words_dict[word] = words_dict.get(word,0) + 1
                #all_words.append(word)

    wc = WordCloud(background_color="white",width=1000,height=1000, max_words=30,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(words_dict)
    plt.axis("off")
    plt.imshow(wc)
    plt.show()

    conn.commit()


if __name__ == '__main__':
    generate_word_cloud()