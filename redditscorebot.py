import praw
import config
import time
from twilio.rest import Client

def main():

    client = Client(config.account_sid, config.auth_token)

    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Upvotetextbot v0.1 by /u/zoopybot")
    cache = []
    def sms_at_score_threshold(subreddit, score):
        #subreddit is taken in as string and score as int
        assert type(subreddit) == str
        assert type(score) == int
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.new(limit=15):
            if submission.score >= score and submission.url not in cache:
                cache.append(submission.url)
                url = (submission.url)
                title = (submission.title)
                message = client.messages.create(
                    to=config.to_phone,
                    from_=config.from_phone,
                    body="\n %s \nHere is the url: %s" % (title, url))
                print(message.sid)
                print "Message sent successfully!"
    while True:
        sms_at_score_threshold("funny", 1000)
        #Edit line above to a differnent subreddit if you would like.
        print "Sleeping for 5 minutes"
        print cache
        time.sleep(300)


if __name__ == '__main__':
    main()
