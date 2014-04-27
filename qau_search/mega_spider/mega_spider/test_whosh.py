# encoding: utf-8
import os

from whoosh.fields import Schema, ID, KEYWORD, TEXT
from whoosh.index import create_in
from whoosh.query import Term 

from pymongo import Connection
from bson.objectid import ObjectId
# from test_jieba import ChineseAnalyzer

from jieba.analyse import ChineseAnalyzer 
analyzer = ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True, analyzer=analyzer),
                nid=ID(unique=True,stored=True), tags=KEYWORD)

if not os.path.exists("index"):
    os.mkdir("index")

index = create_in("index", schema)

connection = Connection()
db = connection.blog
posts = db.siteTables

writer = index.writer()
for post in posts.find():
    # print post
    writer.update_document(title=post['title'],
                            content=post['content'],
                            nid=unicode(post["_id"]),
                            tags=post['url'])
writer.commit()

with index.searcher() as searcher:
    resp = searcher.search(Term("content", u"昆虫"))
    if resp:
        for one in resp:
            post = posts.find_one(ObjectId(one["nid"]))
            print one["title"]
            # print one["tags"]
            print post['url']
            print one.highlights("content")
            print "###############"
            # print post["content"]
    else:
        print 'no content!!'
    # result = searcher.search(Term("content", "tomorrow"))[0]
    # post = posts.find_one(ObjectId(result["nid"]))
    # print result["title"]
    # print post["content"]