import os
from datetime import datetime

if __name__ == '__main__':
    doc_dir = 'docs/'

    if not os.path.exists(doc_dir):
        os.mkdir(doc_dir)

    now = datetime.now()
    html_source = now.strftime('%Y/%m/%d %H:%M:%S')

    with open(doc_dir+'index.html', 'w', encoding='utf-8') as f:
        f.write(html_source)
