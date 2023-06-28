import os
import post

if __name__ == '__main__':
    user_id = os.environ['USER_ID']
    access_token = os.environ['TOKEN']
    id = post.story_publish(access_token, user_id)
