import sys
import os

# TODO: There must be a better way. :)
sys.path.insert(1, os.path.abspath('../streamcamel'))
from streamcamel import StreamCamel

st = StreamCamel()
companies = st.top_companies()
for company in companies:
    print(repr(company))

games = st.top_games(50)
for game in games:
    print(repr(game))

streamers = st.top_streamers(5000)
for streamer in streamers:
    print(repr(streamer))
