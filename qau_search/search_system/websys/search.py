import sys
sys.path.append('/mnt/hgfs/vir_share/qau_search/qau_search')
from flask import Flask, abort, render_template, request
import logging

from search_system.mega_spider.index_db import SearchIndex
# import mega_spider
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,filename='search.log')
logger = logging.getLogger("STATISTIC")


@app.before_request
def before_request():
    # g.db = connect_db()
    pass

@app.route('/')
def hello_world():
    # return "hello world"
    # abort(402)
    return render_template('search.html', name="name")
@app.route('/result', methods=['GET', 'POST'])
def search():
    first_name = unicode(request.form.get("baidu"))

    index = SearchIndex()
    index.create_index()
    result,length = index.get_index_info(first_name)
    logger.debug("##########")
    logger.debug(length)
    # return render_template('baidu.html', name="name")
    return render_template('after_search.html', 
        results = result,
        query=first_name,
        count=length,
        time=0,
        page=0,
        total_page=0,
        host='192.168.44.131',
        port='5000',
        nextpage=1
    	)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

