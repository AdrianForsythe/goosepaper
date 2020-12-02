import logging
from datetime import datetime

from goosepaper.goosepaper import Goosepaper
from goosepaper.reddit import RedditHeadlineStoryProvider
from goosepaper.rss import RSSFeedStoryProvider
from goosepaper.twitter import MultiTwitterStoryProvider
from goosepaper.weather import WeatherStoryProvider
from goosepaper.wikipedia import WikipediaCurrentEventsStoryProvider
from goosepaper.upload import upload


FNAME = datetime.now().strftime("%Y-%m-%d") + ".pdf"
logging.info(f"Honk! I will save your temporary PDF to {FNAME}.")


logging.info(f"Generating paper...")
Goosepaper(
    [
        WikipediaCurrentEventsStoryProvider(),
        WeatherStoryProvider(woe="906057",F=false),
        RSSFeedStoryProvider("https://www.npr.org/feed/", limit=5),
        RSSFeedStoryProvider("https://www.theatlantic.com/feed/all/", limit=5),
#        RSSFeedStoryProvider("https://medium.com/feed/@eLife"),
#	RSSFeedStoryProvider("http://www.nature.com/subjects/microbiology",limit=5),
#	RSSFeedStoryProvider("https://www.microbiologyresearch.org/rss/content/journal/jmmcr/latestissue?fmt=rss",limit=5),
        #RSSFeedStoryProvider("https://www.statnews.com/feed/", limit=2),
        # MultiTwitterStoryProvider(
        # Pending this issue: https://github.com/j6k4m8/goosepaper/issues/5
        #    ["reuters", "bbcWorld", "axios", "BethanyAllenEbr", "NPR"], limit_per=5
        # ),
	#RSSFeedStoryProvider("http://xkcd.com/atom.xml"),
        RedditHeadlineStoryProvider("news"),
        RedditHeadlineStoryProvider("todayilearned")
    ]

).to_pdf(FNAME)
logging.info(f"Saved to PDF, now transferring...")


# upload(FNAME)
logging.info(f"HONK! I'm done :)")
