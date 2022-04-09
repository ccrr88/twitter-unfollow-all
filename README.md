# Twitter Unfollow All Friends

## Twitter API keys
Before calling the twitter API, you must have the Twitter Developer account and a set of keys and tokens. 
https://developer.twitter.com/en/portal/dashboard
This should only take 5 minutes or so

select your project settings -> authentication -> OAuth 1.0a, choose read-write
callback url: http://localhost:3000
website url: just filled in smth random

When you want to unfollow friends, you need to upgrade the essential access to elevated access. You need to do it in the dashboard: https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api . You need to motivate why you need additional access. This process goes very quickly. As motivation I said the following: " I am currently writing a program in python for unfollowing friends
When I try to do this I get the following message:
tweepy.errors.Forbidden: 403 Forbidden
453 - You currently have Essential access which includes access to Twitter API v2 endpoints only. If you need access to this endpoint, you’ll need to apply for Elevated access via the Developer Portal.
It would be great if I could do the unfollowing via the API, many thanks!"

On the question "Will your App use Tweet, Retweet, Like, Follow, or Direct Message functionality?" I said: It will only use unfollow functionality, none of the other. The app will not tweet, follow or use direct messaging

## Install required packages
The script works with the following python packages:
* Tweepy
* configmanager

The required dependencies are on the **requirements.txt** file. To install them run:
```
python3 -m pip install --user -r requirements.txt
```

## Script Configuration
The project comes with an example.ini file that you can use to fill with your own Twitter API credentials.
```
### Configuration parameters
* **API.Key and API.Secret**: Think of these as the user name and password that represents your Twitter developer app when making API requests.
* **Bearer.Token**: OAuth 2.0 Bearer Token authenticates requests on behalf of your developer App.
* **Access.Token and Access.Secret**: user-specific credentials used to authenticate OAuth 1.0a API requests.
* **General.ScreenName**: your twitter account screen name.
* **General.BatchSize**: the maximum number of friend acconts you wish to be able to remove on each run.
```
NO QUOTES

## Run program
```
python program.py
```



