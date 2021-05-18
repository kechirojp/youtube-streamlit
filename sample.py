import streamlit as st
import  numpy as np
import  pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start"

latest_iteration = st.empty()
bar  = st.progress(0)


for i in range(100):
    latest_iteration.text(f"iteration{i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done"


st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})


st.write(df)

st.dataframe(df.style.highlight_max(axis = 0), width=1000, height=1000)

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import  numpy as np
import  pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ["a", "b", "c"]
)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

st.vega_lite_chart(df2, {
         'mark': {'type': 'circle', 'tooltip': True},
         'encoding': {
                 'x': {'field': 'a', 'type': 'quantitative'},
                 'y': {'field': 'b', 'type': 'quantitative'},
                 'size': {'field': 'c', 'type': 'quantitative'},
                 'color': {'field': 'c', 'type': 'quantitative'},
        },
    })


df4 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]#地図をプロットするときのカラム名は必ずこれ　lat = 緯度　lon = 経度
)
st.map(df4)

st.write("Interactive Widgets")

expander1 = st.beta_expander("お問い合わせ")
expander1.write("よくある質問")
expander1.write("通報")
expander2 = st.beta_expander("店舗情報")
expander2.write("関東")
expander2.write("新宿店: 　　　03-2455-1257")
expander2.write("東急文化村店: 03-3723-9577")
                
left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:# buttonが押されたら
    right_column.write("ボタンが押されたので文字を表示　ここは右カラム")

option_hobby = st.text_input("あなたの趣味を教えてください")
"あなたの趣味は、", option_hobby, "です。"

option_condition = st.slider(
    "あなたの今の調子は？", 0, 100, 50)  # 最小値0　最大値100　スタートの値50
"あなたのコンディションは、", option_condition

# sidebar
# option_hobby = st.sidebar.text_input("あなたの趣味を教えてください")
# "あなたの趣味は、", option_hobby, "です。"

# option_condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)# 最小値0　最大値100　スタートの値50
# "あなたのコンディションは、", option_condition

option = st.selectbox(
    "あなたが好きな数字を入れてください",
    list(range(1, 11))# セレクトボックスの中身　ここはリストじゃなきゃならない　ここに株式銘柄を入れる
)

"あなたの好きな数字は、", option, "です。"

img = Image.open("streamlit\sample.png")
st.image(img, caption="Gargantua Boss", use_column_width= True)

if st.checkbox("Show Image"):
    img = Image.open("streamlit\sample.png")
    st.image(img, caption="Gargantua Boss", use_column_width=True)
