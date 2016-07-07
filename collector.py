# coding: utf-8

import urllib2
import json
import time


def get_wall_posts_json(domain, offset, count):
    req = urllib2.Request('https://api.vk.com/method/wall.get?domain=' + domain + '&count=' + str(count) + '&offset=' + str(offset))
    response = urllib2.urlopen(req)
    data = json.loads(response.read())
    for post_dict in data['response'][1:]:
        yield [str(post_dict['id']), post_dict['post_type'], post_dict['text'], str(post_dict['date']), str(post_dict['likes']['count']), str(post_dict['reposts']['count']), str(post_dict['comments']['count'])]


if __name__ == '__main__':
    name = 'baneks'
    fr = 0
    to = 8000
    step = 90
    
    with open("all_posts.tsv", "w+") as res_file:      
        res_file.write("\t".join(["id", "post_type", "text", "date", "likes_count", "reposts_count", "comments_count"]) + "\n")  
        for curr_from in xrange(fr, to, step):
            print curr_from, curr_from + step
            data = get_wall_posts_json(name, curr_from, step)
            for post in data:
                res_file.write("\t".join(post).encode("UTF-8") + "\n")


