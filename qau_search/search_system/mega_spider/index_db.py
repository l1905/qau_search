# encoding: utf-8
import os

from whoosh.fields import Schema, ID, KEYWORD, TEXT
from whoosh.index import create_in, open_dir
from whoosh.query import Term 
from whoosh.qparser import QueryParser

from pymongo import Connection
from bson.objectid import ObjectId

from db import MongoDB
# from test_jieba import ChineseAnalyzer

from jieba.analyse import ChineseAnalyzer 

analyzer = ChineseAnalyzer()
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True, analyzer=analyzer),
                nid=ID(unique=True,stored=True), url=KEYWORD)
posts = MongoDB()

class SearchIndex(object):
    """docstring for SearchIndex"""
    def __init__(self):
        self.schema = schema
        self.collect = MongoDB()

    def create_index(self):
        if not os.path.exists("index"):
            os.mkdir("index")
            index = create_in("index", schema)
            writer = index.writer()
            for post in self.collect.find():
                writer.update_document(title=post['title'],
                                        content=post['content'],
                                        nid=unicode(post["_id"]),
                                        url=post['url'])
            writer.commit()

    def get_index_info(self, query):
        index = open_dir("index")
        with index.searcher() as searcher:
            parser = QueryParser("content", index.schema)
            my_query = parser.parse(query)
            result = []
            resp = searcher.search(my_query, limit=None)
            if resp:
                for one in resp:
                    post = self.collect.find_one(ObjectId(one["nid"]))
                    result.append({"title":one['title'], "url":post['url'], "content":one.highlights("content")})
                    # return one['title']
                    # print one["title"]
                    # print post['url']
                    # print one.highlights("content")
                    # print "###############"
            return result, len(result)


# if not os.path.exists("index"):
#     os.mkdir("index")
#     index = create_in("index", schema)
#     writer = index.writer()
#     for post in posts.find():
#         writer.update_document(title=post['title'],
#                                 content=post['content'],
#                                 nid=unicode(post["_id"]),
#                                 url=post['url'])
#     writer.commit()
# else:
#     index = open_dir("index")

# #第一种搜索方式
# # with index.searcher() as searcher:
# #     resp = searcher.search(Term("content", u"校园 秋色"))
# #     if resp:
# #         for one in resp:
# #             post = posts.find_one(ObjectId(one["nid"]))
# #             print one["title"]
# #             # print one["url"]
# #             print post['url']
# #             print one.highlights("content")
# #             print "###############"
# #             # print post["content"]
# #     else:
# #         print 'no content!!'

# #第二种搜索方式
# with index.searcher() as searcher:
#     parser = QueryParser("content", index.schema)
#     my_query = parser.parse(u"校园 秋色")

#     resp = searcher.search(my_query)
#     if resp:
#         for one in resp:
#             post = posts.find_one(ObjectId(one["nid"]))
#             print one["title"]
#             print post['url']
#             print one.highlights("content")
#             print "###############"
#     else:
#         print 'no content!!'
