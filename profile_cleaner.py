from instagrapi import Client
from getpass import getpass

# TODO: Docker-ize

client = Client()

print("\nHello! This is a tool that automatically unfollows normal (i.e. non-celebrity) Instagram accounts that don't follow back. \nEnter your Instagram username and password below to get started.\n")

username = input("username: ")
password = getpass("password: ")

logged = False

client.login(
    username=username,
    password=password
)

user = client.user_info_by_username(client.username)

print(
    f"\nSuccesfully logged into @{user.username}.\n\tfollower count: {user.follower_count}\n\tfollowing count: {user.following_count}\n")

threshold = int(input(
    "Celebrity threshold (the number of followers beyond which you wish to stay following): "))

followers = client.user_followers(user.pk)
following = client.user_following(user.pk)

print(
    f"\nWill proceed to unfollow all users with under {threshold} followers who don't follow back:")

for acct in following:
    if (not (acct in followers)):
        acct_profile = client.user_info_by_username(
            client.username_from_user_id(acct))
        if acct_profile.follower_count < threshold:
            try:
                client.user_unfollow(acct)
                print(f"Unfollowing @{acct_profile.username}...")
            except:
                print(
                    f"would unfollow @{acct_profile.username} if Instagram weren't being a little shit and blocking me from making requests on your behalf...")
