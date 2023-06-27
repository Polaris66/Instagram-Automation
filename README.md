## Get Access Token

Make an app and get access token

## Get User Id

https://graph.facebook.com/me?fields=id&access_token={access_token}

## Make Story

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?image_url={video-url}
  &media_type={media-type}
  &access_token={access-token}

## Publish Story

POST https://graph.facebook.com/{api-version}/{ig-user-id}/media_publish
  ?creation_id={creation-id}
  &access_token={access-token}

## Environment Variables

IMAGE_KEY
USER_ID
TOKEN
