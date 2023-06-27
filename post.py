import requests
import os
import images

def story(access_token, user_id):
    image_url = images.upload_image()
    media_type = 'STORIES'
    try:
        container_id = requests.post(f'https://graph.facebook.com/v17.0/{user_id}/media?image_url={image_url}&media_type={media_type}&access_token={access_token}').json()['id']
        print(container_id)
        return container_id
    except requests.exceptions.HTTPError as e:
        print(e.response.text)

def story_publish(access_token, user_id):
    container_id = story(access_token, user_id)
    try:
        res = requests.post(f'https://graph.facebook.com/v17.0/{user_id}/media_publish?creation_id={container_id}&access_token={access_token}')
        return res.json()['id']
    except requests.exceptions.HTTPError as e:
        print(e.response.text)

    