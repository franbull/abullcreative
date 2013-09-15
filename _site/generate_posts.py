import os
body = """---
layout: post
title:  "%(title)s"
date:   2013-09-14 16:09:44
categories: cover
image: %(url)s 
thumbnail: %(thumb)s
---
![%(title)s][image]

[image]: %(url)s "%(title)s"
"""

files = [
('augustfolly.jpg', 'August Folly'),
('cheerfulmoney.jpg', 'Cheerful Money'),
('cheever.jpg', 'Cheever'),
('darlene.jpg', 'Business Cards'),
('destinydisrupted.jpg', 'Destiny Disrupted'),
('emilypost.jpg', 'Emily Post'),
('karaoke.jpg', 'Karaoke Flyers'),
('madamebovary.jpg', 'Madame Bovary'),
('nadya.jpg', 'Nadya'),
('odmagic.jpg', 'Od Magic'),
('paulandlyns.jpg', 'Wedding Invitations'),
('siskiyouchallenge.jpg', 'Siskyou Challenge'),
('siskiyouchallenge2.jpg', 'More Siskyou Challenge'),
('theace.jpg', 'The Ace'),
('travelwriting.jpg', 'Travel Writing'),
('thezebramurders.jpg', 'The Zebra Murders'),
]
for fn, title in files:
    url = '/images/%s' % fn
    fn_title = title.lower().replace(' ', '-')
    filename = '2013-09-14-%s.markdown' % fn_title
    thumb = '/images/thumbs/%s.gif' % fn.split('.')[0]
    text = body % {'title': title, 'url': url, 'thumb': thumb}
    with open('_posts/%s' % filename, 'w') as fout:
        fout.write(text)
    

