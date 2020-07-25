# streamcamel-py
StreamCamel Python API

# Introduction
This is the official Python API to access the Stream Camel API.
See the samples directory for samples how to use the API.

# Example Usage to get top streamers and print information about them

```
import sys
import os

# TODO: There must be a better way. :)
sys.path.insert(1, os.path.abspath('../streamcamel'))
from streamcamel import StreamCamel

st = StreamCamel()
streamers = st.top_streamers()
for streamer in streamers:
    print(repr(streamer))
```

    
