# Install snscrape first if you don't have it
# pip install snscrape

import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(profile_url, max_tweets=100):
    """
    profile_url: full X/Twitter URL, e.g. "https://x.com/noob4141"
    max_tweets: max number of tweets to fetch
    """
    username = profile_url.rstrip("/").split("/")[-1]  # extract handle
    tweets_list = []

    for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
        if i >= max_tweets:
            break
        tweets_list.append({
            'date': tweet.date,
            'content': tweet.content,
            'url': tweet.url
        })
    
    df = pd.DataFrame(tweets_list)
    return df

# Example usage
profile_link = "https://x.com/noob4141"
df = scrape_tweets(profile_link, max_tweets=50)
print(df)

# Optionally, save to CSV
df.to_csv("tweets.csv", index=False)
