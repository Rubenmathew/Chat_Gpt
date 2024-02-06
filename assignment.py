import yfinance as yf
import pandas as pd 
from transformers import pipeline

msft = yf.Ticker("msft")


print(type(msft.history(period="max")))
print(msft.actions)
df = pd.DataFrame(msft.history(period="max"))

# Convert each row to a list
list = df['Volume'].values.tolist()
for i in range(1,len(list)-1):
        if list[i]==0:
           print("Pani paali")

def calc_returns(prices):
    value=[]
    for i in range(1,len(prices)-1):
            r=(prices[i]/prices[i-1])-1
            value.append(round(r,2))   
    return value

answer=calc_returns(list)
print(len(list))
print(len(answer))


def calc_simple_moving_average(prices, windows_size):
    value=[]
    for i in range(1, len(prices)-1):
         if i < 0 or windows_size < 1 or i + windows_size > len(prices):
          print("Invalid window parameters")
         else :
              window_sum = sum(prices[i:i + windows_size])
              average = window_sum / windows_size
              value.append(round(average,2))
    return value


print(calc_simple_moving_average(list,5))
news=[]
for i in range(0,len(msft.news)):
    info=msft.news[i]['title']
    news.append(info)
print(news)

def sentimental_model(text):
    sentiment_analysis = pipeline('sentiment-analysis')
    result=sentiment_analysis(text)
    return(result)

# # answers=sentimental_model(news)
# # print(answers)

# for j in news:
#     print("\033[0m The sentence--"+j+"is"+sentimental_model(j)[0]['label'])
# text="The moonlit night embraces the quiet town with a serene glow"
# sentiment_analysis = pipeline('sentiment-analysis')
# result=sentiment_analysis(text)
# print("The sentence  "+text+" is "+result[0]['label'])
# print(result)