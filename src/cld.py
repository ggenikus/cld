import sys,os
import urllib
libs = os.path.join(os.path.dirname(os.path.abspath(__file__)),"libs")
sys.path.append(libs)

from workflow import Workflow
from bs4 import BeautifulSoup

__version__ = '0.0.1'

def main(wf):
    url = "http://clojuredocs.org"
    r = urllib.urlopen(url + "/search?q=" + wf.args[0]).read()
    soup = BeautifulSoup(r,'html.parser')
    sr = soup.find_all(class_="search-result")
    for s in sr:
        fname = s.find("h2").get_text()
        href = s.find("h2").find("a")['href']
        desc = s.find("p").get_text()
        wf.add_item(title=fname,
                    subtitle=desc,
                    quicklookurl=url + href,
                    valid=True,
                    icon='icons/f.icns',
                    arg=url + href)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow(update_settings={
        'version': __version__,
        'github_slug': 'ggenikus/cld',
        'frequency': 1,
    })

    if wf.update_available:
        wf.start_update()
    sys.exit(wf.run(main))
