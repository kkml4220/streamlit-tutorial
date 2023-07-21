import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
from PIL import Image
import time



st.title("Streamlit 入門")

st.header('Progress bar')

st.write("何も読み込んでませんが，Progress barも使えます UX向上間違いなし!")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(0, 100):
    latest_iteration.text(f"loading {i + 1}%")
    bar.progress(i + 1)
    time.sleep(0.01)

st.header('DataFrame')

df = pd.DataFrame(
    {
        "1列目": [1, 2, 3, 4],
        "2列目": [10, 20, 30, 40]
    }
)
# ハイライト
st.dataframe(df.style.highlight_max(axis=0))

st.header('DataFrameの編集')
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.header('Interactive Widgets')

st.text_input("Tell me your hobby")


age = st.slider("Tell me your age", 0 , 100, 30)
st.write(f"{age} years old.")


if st.checkbox("Show secret image"):
    img = Image.open("./imaegs/image.png")
    st.image(img, caption="キャプションも追加できます", use_column_width=True)


st.header('Markdown')

"""

#### Markdownも書くことができる


**シンタックスハイライト**もしてくれるらしい．

```python
import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \frac{1-r^{n}}{1-r} 
    ''')
```


- 箇条書きもできる
- これも箇条書き
"""



st.header('数式')
st.write("複雑な数式も記述可能です")


st.latex(r'''
    \left( \int_0^\infty \frac{\sin x}{\sqrt{x}} dx \right)^2 =
    \sum_{k=0}^\infty \frac{(2k)!}{2^{2k}(k!)^2} \frac{1}{2k+1} =
    \prod_{k=1}^\infty \frac{4k^2}{4k^2 - 1} = \frac{\pi}{2}
    ''')




st.header('折れ線グラフ')

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(df)


st.header('棒グラフ')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(df)



st.header('バブルチャート')

chart_data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

st.header('3D plot')

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))





