from reddit import scrape_reddit_politics
import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import spacy

class RedditStats:
    def __init__(self):
        #open database connection
        conn = sqlite3.connect('Final.sqlite')
        cur = conn.cursor()

        cur.execute('SELECT * FROM Reddit')
        self.data = cur.fetchall()

    def generate_word_cloud(self):
        #natural language processing
        nlp = spacy.load("en_core_web_sm")

        #all_words = []
        words_dict = {}
        #words to ignore in most common
        ignore = ["'m", '|', 'if', 'to', 'of', 'in', 'is', 'on', 'and', 'for', 'it', 'as', 'a', 'not', "n't", "n’t", "that", "the", "or", "with", "are", "we", "’s", "'s", "his", "say", "says", "from", "do", "be", "he", "i", "out", "at", "after", "new", "about", "by", "was", "has"]

        title_list = [item[2] for item in self.data]

        for title in title_list:
            #words = tup[0].split()
            doc = nlp(title)
            for token in doc:
                word = token.text
                word = word.rstrip('.')
                word = word.lower()

                if not word in ignore and not token.is_punct and not token.pos_ == "SYM":
                    words_dict[word] = words_dict.get(word,0) + 1
                    #all_words.append(word)

        #print(sorted(words_dict.items(), key = lambda tup : tup[1]))

        wc = WordCloud(background_color="white",width=1000,height=1000, max_words=30,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(words_dict)
        plt.axis("off")
        plt.imshow(wc)
        plt.show()

    def most_common_authors(self):

        author_dict = {}

        author_list = [item[1] for item in self.data]

        for author in author_list:
            author_dict[author] = author_dict.get(author,0) + 1

        sorted_authors = sorted(author_dict.items(), key = lambda tup : tup[1], reverse=True)
        x_axis = [item[0] for item in sorted_authors[:5]]
        y_axis = [item[1] for item in sorted_authors[:5]]

        graph = plt.bar(x=x_axis, height=y_axis)
        plt.show()

    def authors_numPosts_ratings(self):

        author_list = [item[1] for item in self.data]
        ratings_list = [item[5] for item in self.data]
        comments_list = [item[6] for item in self.data]

        ratings_dict = {}
        numPosts_dict = {}
        comments_dict = {}

        for i in range(len(author_list)):
            author = author_list[i]
            numPosts_dict[author] = numPosts_dict.get(author,0) + 1

            #calculates total scores and total comments
            ratings_dict[author] = ratings_dict.get(author,0) + ratings_list[i]
            comments_dict[author] = comments_dict.get(author,0) + comments_list[i]

        #calculates average ratings
        print("Getting Averages!")
        for author in ratings_dict:

            print("Rating total:", ratings_dict[author])
            print("Comments total:", comments_dict[author])

            ratings_dict[author] = (ratings_dict[author] / numPosts_dict[author])
            comments_dict[author] = (comments_dict[author] / numPosts_dict[author])

            print("Rating average:", ratings_dict[author])
            print("Comments average:", comments_dict[author])

        all_data = []
        for author in numPosts_dict:
            tup = (numPosts_dict[author] * 20, ratings_dict[author], comments_dict[author])
            #print(tup)
            all_data.append(tup)


        x_axis = [item[2] for item in all_data]
        y_axis = [item[1] for item in all_data]
        radius = [item[0] for item in all_data]

        graph = plt.scatter(x=x_axis, y=y_axis, s=radius, alpha=0.5)
        plt.title("Ratings, Comments, and Posts by Author")
        plt.xlabel("Number of Comments")
        plt.ylabel("Rating")
        plt.show()


if __name__ == '__main__':
    #define a reddit object
    reddit = RedditStats()

    #reddit.generate_word_cloud()
    #reddit.most_common_authors()
    reddit.authors_numPosts_ratings()
