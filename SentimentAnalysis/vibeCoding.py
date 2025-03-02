import tweepy # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # type: ignore

def fetch_tweets(client, query, limit):
    tweets = []
    try:
        # Paginator kullanarak belirtilen limitte tweet çekiyoruz
        for tweet in tweepy.Paginator(client.search_recent_tweets,
                                      query=query,
                                      tweet_fields=['created_at', 'lang'],
                                      max_results=100).flatten(limit=limit):
            tweets.append(tweet)
            print(len(tweets))
    except tweepy.errors.TooManyRequests:
        print(len(tweets))
        print("Rate limit aşıldı. 15 dakika bekleyip tekrar denenecek...")
        time.sleep(900)  # 15 dakika bekle
        tweets = fetch_tweets(client, query, limit)  # Tekrar deneme
    return tweets

def main():
    # API anahtarlarınızı buraya ekleyin
    api_key = "WzrVLZB65tA5pnKhfuZG5bHlB"  # noqa: F841
    api_secret = "84vTDsbmmkq6PMAaeDX1XMneevCn4uiOqytYuACtyq1z0bzfO0"  # noqa: F841
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAE6ozgEAAAAAIRKmDYr0V0FqvRcc9eMCbJshrsY%3DTFdkRvP16LUGGmiThCmFqVErpvdG5c0yjvuEChGAcdhkys0CrE"

    # Tweepy Client oluştururken rate limit ayarını aktif ediyoruz
    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

    # Analiz etmek istediğiniz sorgu (örneğin "Maldini")
    query = "patlama"
    tweet_limit = 200  # Çekmek istediğiniz tweet sayısı

    tweets = fetch_tweets(client, query, tweet_limit)
    print(f"Toplanan tweet sayısı: {len(tweets)}")

    # Tweet verilerini DataFrame'e aktarıyoruz
    data = {
        "text": [tweet.text for tweet in tweets],
        "created_at": [tweet.created_at for tweet in tweets],
        "lang": [tweet.lang for tweet in tweets]
    }
    df = pd.DataFrame(data)

    # Sadece Türkçe tweetleri analiz etmek için filtreleme (isteğe bağlı)
    df = df[df["lang"] == "tr"]
    print(f"Türkçe tweet sayısı: {len(df)}")

    # VADER ile sentiment analizi
    analyzer = SentimentIntensityAnalyzer()
    df["sentiment_scores"] = df["text"].apply(lambda x: analyzer.polarity_scores(x))
    df["compound"] = df["sentiment_scores"].apply(lambda score: score["compound"])

    # Tweetlerin duygu kategorilerini belirleme
    def classify(compound):
        if compound >= 0.05:
            return "Positive"
        elif compound <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    df["sentiment"] = df["compound"].apply(classify)
    sentiment_counts = df["sentiment"].value_counts()
    print("Duygu Kategorileri:")
    print(sentiment_counts)

    # Görselleştirme: Compound skoru dağılımı
    plt.figure(figsize=(10,6))
    sns.histplot(df["compound"], bins=20, kde=True)
    plt.title("Tweet Compound Skorlarının Dağılımı")
    plt.xlabel("Compound Skoru")
    plt.ylabel("Tweet Sayısı")
    plt.show()

    # Görselleştirme: Duygu kategorilerinin dağılımı
    plt.figure(figsize=(8,6))
    order = ["Positive", "Neutral", "Negative"]
    sns.countplot(x="sentiment", data=df, order=order)
    plt.title("Duygu Kategorilerine Göre Tweet Sayıları")
    plt.xlabel("Duygu")
    plt.ylabel("Tweet Sayısı")
    plt.show()

if __name__ == "__main__":
    main()