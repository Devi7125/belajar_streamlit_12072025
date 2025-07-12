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
st.text("This is text\n[and more text](that's not a Markdown link).")

st.success('This is a success message!', icon="✅")

st.line_chart(chart_data, x="col1", y="col2", color="col3")

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")

st.text("This is text\n[and more text](that's not a Markdown link).")

