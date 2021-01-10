from pathlib import Path
from nozomi import api
import random
import os

# The tags that the posts retrieved must contain
positive_tags = ['helltaker']
downLoadPath = Path('/Users/leolee/Documents/Project/pythonProject/DownloadFile')


def search(tags=list()):
    print('start search')
    positive_tags = tags

    length = 0

    posts1 = api.get_posts(positive_tags)
    posts2 = posts1
    for post in posts1:
        length += 1
        if (length > 20):
            break

    if length == 0:
        return ''

    print(length)
    randomIndex = random.randrange(0, length)
    print(randomIndex)

    count = 0
    #posts = api.get_posts(positive_tags)
    for post in posts2:
        if count == randomIndex:
            print("start download")
            imageName = api.download_media(post, downLoadPath)
            return imageName[0]
            break
        else:
            count += 1

    print(count)


def clear_downloadDir(fileName:str):
    os.remove(str(downLoadPath)+'/'+fileName)
