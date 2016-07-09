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


def get_wall_comments(owner_id, post_id, offset, count):
    req = urllib2.Request('https://api.vk.com/method/wall.getComments?owner_id='+str(owner_id)+'post_id=' + str(post_id) + '&count=' + str(count) + '&offset=' + str(offset) + '&preview_length=0&need_likes=1')
    response = urllib2.urlopen(req)
    data = json.loads(response.read())
    for c_dict in data['response'][1:]:
        yield [str(post_id), str(c_dict['cid']), c_dict['uid'], post_dict['text'], str(post_dict['date']), str(post_dict['likes']['count'])]


def download_all_posts(comm_name, fr, to, step):
    with open("all_posts_" + comm_name + ".tsv", "w+") as res_file:      
        res_file.write("\t".join(["id", "post_type", "text", "date", "likes_count", "reposts_count", "comments_count"]) + "\n")  
        for curr_from in xrange(fr, to, step):
            print curr_from, curr_from + step
            data = get_wall_posts_json(name, curr_from, step)
            for post in data:
                res_file.write("\t".join(post).encode("UTF-8") + "\n")
"""
def download_all_comments(club_name, club_id, max_posts, max_comments):
    
    with open("all_comments_" + comm_name + ".tsv", "w+") as res_file:      
        res_file.write("\t".join(["post_id", "cid", "uid", "text", "date", "likes_count"]) + "\n")  
        for curr_from in xrange(fr, to, step):
            print curr_from, curr_from + step
            data = get_wall_posts_json(name, curr_from, step)
            for post in data:
                res_file.write("\t".join(post).encode("UTF-8") + "\n")
"""
if __name__ == '__main__':
    name = 'baneks'
    fr = 0
    to = 8000
    step = 90
    #download_all_posts(name, fr, to, step)
    owner_id = -45491419
    


