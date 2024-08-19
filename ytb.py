from googleapiclient.discovery import build

api_key = "AIzaSyBkZd3mQSNiZDdUagxegcTi9jPuFWQKeUw"

aa = build('youtube', 'v3', developerKey=api_key)

video_id = "***********************************"

bb = aa.videos().list(
    part='snippet,statistics',
    id=video_id
)

""" Execute the API request """
cc = bb.execute()

video_inf = cc['items'][0]

title = video_inf['snippet']['title']
print(f"Title: {title}")

description = video_inf['snippet']['description']
print(f"Description: {description}")

view = video_inf['statistics']['viewCount']
print(f"Views: {view}")

like = video_inf['statistics'].get('likeCount', 'Likes = 0')
print(f"Likes: {like}")

comment = video_inf['statistics'].get('commentCount', 'Comments = 0')
print(f"Comments: {comment}")
