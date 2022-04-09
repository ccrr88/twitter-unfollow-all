# Twitter Unfollow All Friends

## Twitter API keys
Before calling the twitter API, you must have the Twitter Developer account and a set of keys and tokens. 
https://developer.twitter.com/en/portal/dashboard
This should only take 5 minutes or so

Please note, when creating the Twitter app on the developer portal, you must define it as read/write, otherwise the unfollow command will fail with an error. 

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

## Run program
```
python program.py
```



