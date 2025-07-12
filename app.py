import streamlit as st
import pandas as pd
import numpy as np

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")

VIDEO_URL = "https://example.com/not-youtube.mp4"
st.video(VIDEO_URL, subtitles="subtitles.vtt")
