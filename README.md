# Twitter Sentiment Analysis

Bu proje, Tweepy kütüphanesi kullanarak Twitter'dan belirli bir anahtar kelimeye sahip tweet'leri çekip, VADER kütüphanesi ile duygu analizi yapar. Sonuçlar grafiksel olarak görselleştirilir.

## Gereksinimler

Bu projeyi çalıştırmadan önce aşağıdaki bağımlılıkların kurulu olduğundan emin olun:

- Python 3.x
- Tweepy
- Pandas
- Matplotlib
- Seaborn
- VaderSentiment

Bağımlılıkları yüklemek için:
```bash
pip install tweepy pandas matplotlib seaborn vaderSentiment
```

## Kullanım

1. **Twitter API Anahtarlarını Ayarlayın:**
   - `api_key`, `api_secret` ve `bearer_token` değişkenlerini kendi Twitter API anahtarlarınız ile değiştirin.

2. **Kodu Çalıştırın:**
   ```bash
   python script.py
   ```

3. **Anahtar Kelimeyi Güncelleyin:**
   - `query` değişkenini istediğiniz anahtar kelimeyle değiştirerek farklı veriler üzerinde analiz yapabilirsiniz.

## Çalışma Prensibi

1. Twitter API kullanılarak belirli bir anahtar kelime ile tweet'ler çekilir.
2. Çekilen tweet'ler pandas DataFrame'e aktarılır.
3. Sadece Türkçe tweetler analiz edilir.
4. VADER SentimentIntensityAnalyzer kullanılarak her tweet'in duygu skoru hesaplanır.
5. Tweet'ler üç kategoriye ayrılır: **Positive**, **Neutral**, **Negative**.
6. Sonuçlar histogram ve sütun grafikleri ile görselleştirilir.

## Çıktılar

- Tweet'lerin duygu analizi sonucunda oluşturulan histogram ve dağılım grafikleri.
- Terminalde tweet sayıları ve duygu kategorileriyle ilgili özet bilgi.

## Örnek Görselleştirme

- **Tweet Compound Skorlarının Dağılımı**: Tweet'lerin duygu skorlarının histogramı.
- **Duygu Kategorilerine Göre Tweet Sayıları**: Positive, Neutral ve Negative duygu dağılımı.

---

Bu proje, sosyal medya verilerinden duygu analizi yapmak isteyenler için temel bir başlangıç noktası sunmaktadır.

