import praw
import sqlite3

def scrape_reddit_politics():

    #reddit object
    reddit = praw.Reddit("bot1")
    sub = reddit.subreddit("politics")

    # make a connection to final project database
    conn = sqlite3.connect('Final.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Reddit(id TEXT, author TEXT, title TEXT, content TEXT, link TEXT, score INTEGER, num_comments INTEGER)')

    num_added = 0

    for submission in sub.hot(limit=20):
        submission_id = str(submission.id)
        author = str(submission.author)
        title = str(submission.title)
        content = str(submission.selftext)
        link = str(submission.url)
        score = int(submission.score)
        num_comments = int(submission.num_comments)

        #if submission not already in table
        cur.execute('SELECT id FROM Reddit WHERE id = "%s"' % submission_id)
        data = cur.fetchone()
        if data == None:
            #add to the table
            cur.execute('INSERT INTO Reddit(id, author, title, content, link, score, num_comments) VALUES (?,?,?,?,?,?,?)', (submission_id, author, title, content, link, score, num_comments))
            num_added += 1


    conn.commit()
    print("Added", num_added, "post(s) to database!")


if __name__ == '__main__':
    scrape_reddit_politics();
