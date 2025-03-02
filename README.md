Twitter Sentiment Analysis

Bu proje, Tweepy kütüphanesi kullanarak Twitter'dan belirli bir anahtar kelimeye sahip tweet'leri çekip, VADER kütüphanesi ile duygu analizi yapar. Sonuçlar grafiksel olarak görselleştirilir.

Gereksinimler

Bu projeyi çalıştırmadan önce aşağıdaki bağımlılıkların kurulu olduğundan emin olun:

Python 3.x

Tweepy

Pandas

Matplotlib

Seaborn

VaderSentiment

Bağımlılıkları yüklemek için:

pip install tweepy pandas matplotlib seaborn vaderSentiment

Kullanım

Twitter API Anahtarlarını Ayarlayın:

api_key, api_secret ve bearer_token değişkenlerini kendi Twitter API anahtarlarınız ile değiştirin.

Kodu Çalıştırın:

python script.py

Anahtar Kelimeyi Güncelleyin:

query değişkenini istediğiniz anahtar kelimeyle değiştirerek farklı veriler üzerinde analiz yapabilirsiniz.

Çalışma Prensibi

Twitter API kullanılarak belirli bir anahtar kelime ile tweet'ler çekilir.

Çekilen tweet'ler pandas DataFrame'e aktarılır.

Sadece Türkçe tweetler analiz edilir.

VADER SentimentIntensityAnalyzer kullanılarak her tweet'in duygu skoru hesaplanır.

Tweet'ler üç kategoriye ayrılır: Positive, Neutral, Negative.

Sonuçlar histogram ve sütun grafikleri ile görselleştirilir.

Çıktılar

Tweet'lerin duygu analizi sonucunda oluşturulan histogram ve dağılım grafikleri.

Terminalde tweet sayıları ve duygu kategorileriyle ilgili özet bilgi.

Örnek Görselleştirme

Tweet Compound Skorlarının Dağılımı: Tweet'lerin duygu skorlarının histogramı.

Duygu Kategorilerine Göre Tweet Sayıları: Positive, Neutral ve Negative duygu dağılımı.
