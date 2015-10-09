from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'Tv3Hg4aD2S7KBTWb7prlX86P5'
consumer_secret = 'AfFzuWkWH0PWsn3pobOQRKSBXALq46sdlVNRs1biKyzOAkoN7j'
access_token = '882362557-2YUj5o6bNlcOQDstlyTnVEeE9XCeKpmDxwFLrGwW'
access_secret = 'V6H67JM1hc06lq7ot4EEEUX4GZ2jUO4tAMzz4WBOLuh4w'

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status
        
        
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
stream = Stream(auth, l)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['Hollywood','Movies','Music','Health','Politic','Election','Syria'])