import sys
import os

# TODO: There must be a better way. :)
sys.path.insert(1, os.path.abspath('../streamcamel'))
from streamcamel import StreamCamel

st = StreamCamel()
streamers = st.top_streamers()
for streamer in streamers:
    print(repr(streamer))