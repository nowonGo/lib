import streamlit as st

st.title('🔅상호작용을 위한 앱 만들기')
st.link_button('맞춤법 확인하기', 'http://speller.cs.pusan.ac.kr/')
# st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9jxOUyg4MpboK4U-hkBQyL1OemvizgggsHA&s', width = 500)
col1, col2 = st.columns(2)
with col1:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9jxOUyg4MpboK4U-hkBQyL1OemvizgggsHA&s')
with col2:
    answer = st.text_input('이 과일의 이름을 입력해주세요')
    if answer == '사과':
        st.success('당신은 천재입니다')
    else:
        st.error('오답입니다. 아쉽네요.')

st.latex('f=ma')

tab1, tab2 = st.tabs(['봄', '여름'])

tab1.success('봄입니다')
tab2.success('여름입니다')