import configparser
import tweepy
from datetime import date

def main():
    #Read security tokens from external .ini file
    config = configparser.ConfigParser()
    config.read('config.ini')
    print('Read configuration file.')
    print(config.sections())

    #Pass tokens for authorization
    auth = tweepy.OAuthHandler(config['API']['Key'], config['API']['Secret'])
    auth.set_access_token(config['Access']['Token'], config['Access']['Secret'])

    #Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True)

    #Get the user object
    user = api.get_user(screen_name=config['General']['ScreenName'])

    print(user.screen_name)
    print(config['General']['ScreenName'] + ' has ' + str(user.followers_count) + ' friends')

    #List to put the friends in
    friends_to_unfollow = [];

    for friend in tweepy.Cursor(api.get_friends, screen_name=user.screen_name).items(): 
        friends_to_unfollow.append(friend)
        
        if (len(friends_to_unfollow) >= int(config['General']['BatchSize'])):
            break

    #output the result
    if (len(friends_to_unfollow) > 0):
        print('The following % s friends will be unfollowed:' % len(friends_to_unfollow))
        for friend in friends_to_unfollow:
            print(friend.screen_name)

        print('Unfollowing %s friends..' % len(friends_to_unfollow))

        #To unfollow wothout prompt, comment the following 2 lines
        answer = input("Are you sure? [Y/n]").lower()
        if answer and answer[0] == "y":
            for friend in friends_to_unfollow:
                print("Unfollowing " + friend.screen_name)
                friend.unfollow()


if __name__ == "__main__":
    main()
