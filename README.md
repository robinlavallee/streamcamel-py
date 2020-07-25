# streamcamel-py
StreamCamel Python API

# Introduction
This is the official Python API to access the Stream Camel API.

# Example Usage to get top streamers

```
from StreamCamel import StreamCamel
st = StreamCamel()
streamers = st.top_streamers()
for streamer in streamers:
    print(repr(game))
```

    
