

post = """---
layout: post
title:  "%(title)s"
date:   2013-09-21 16:09:44
categories: poster
image: /images/posters/%(image_name)s.jpg 
thumbnail: /images/posters/%(thumb_name)s.jpg
---
![%(title)s][image]

[image]: /images/posters/%(image_name)s.jpg "%(title)s"
"""

title = raw_input('title:')
image = raw_input('image_name:')
thumb = raw_input('thumb_name:')

print post % {'title': title, 'image_name': image, 'thumb_name': thumb}