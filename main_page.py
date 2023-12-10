import streamlit as st
# from streamlit.web.cli import main
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
master_data_path = './data/'
file_name   = '1page_mst.csv'

master_data = pd.read_csv(f'{master_data_path}{file_name}')
st.header('메인페이지')
master_data['lon'] = round(master_data['지하철역X좌표'], 7)
master_data['lat'] = round(master_data['지하철역Y좌표'], 7)
# master_data = master_data.rename(columns = {'지하철역X좌표' : 'lon', '지하철역Y좌표' : 'lat'})
temp = master_data[master_data['지하철역명'] != '쌍용(나사렛대)']
temp2 = temp[['lat', 'lon']]
temp = temp.rename(columns = {'지하철역명' : 'info'})
trans = pd.read_csv(f'{master_data_path}환승정보_중복제거.csv')

with st.sidebar:
    add_radio = st.radio(
        "궁금한 정보를 고르세요",
        ("빠른 환승 정보", "지하철 경로 및 소요 시간")
    )
def trans_info(x, trans_x) :
    trans_list = trans[trans['지하철호선명'] == x | trans['환승후호선명'] == trans_x]['환승위치'].to_list()
    return trans_list

col1, col2 = st.columns([6,3])
col1.write('[지하철역 위치 정보]')
st.data_editor(master_data)
fig = px.scatter_mapbox(master_data, lat='지하철역X좌표', lon='지하철역Y좌표'
                        , hover_name="지하철역명"
                        # , hover_data=["지하철호선명", "환승후호선명", "환승위치"]
                        , hover_data=["지하철호선명", "환승후호선명", trans_info(지하철호선명, 환승후호선명)]
                        
                     )
fig.update_layout(mapbox_style="open-street-map")
test_fig = fig
with col1:
    st.plotly_chart(test_fig, use_container_width=True)


col2.write('[역 선택]')
with col2 :
    station = st.text_input('역을 입력하세요 ')
    st.write('The selected subway station is', station)
    select_number = st.selectbox(
        '몇 호선인지 선택하세요',
        ('서해선',
    '자기부상선',
    '에버라인',
    '경강선',
    '1호선',
    '2호선',
    '3호선',
    '4호선',
    '5호선',
    '6호선',
    '8호선',
    '7호선',
    '9호선',
    '경춘선',
    '인천1호선',
    '중앙선',
    '경의중앙선',
    '신분당선',
    '수인선',
    '공항철도',
    '수인분당선',
    '의정부',
    '인천2호선',
    '우이신설선'))
    지하철역_호선명 = pd.read_csv("C:/Users/GAYOUNG/Downloads/fix_지하철역_호선명매핑.csv")
    역_호선명 = 지하철역_호선명.loc[:,['지하철역명','지하철호선명']]
    df = pd.DataFrame(역_호선명)
    # Add vertical scroll for radio.
    st.markdown("""
        <style>
            .row-widget {
            height: 100px;
            overflow-y: scroll;
            }
        </style>
        """,
        unsafe_allow_html=True)
    if select_number == '서해선':
        station = st.radio("Which station are you curious about?", list(df.지하철역명[역_호선명.지하철호선명=='서해선']))
    elif select_number == '자기부상선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='자기부상선']))
    elif select_number == '에버라인':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='에버라인']))
    elif select_number == '경강선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='경강선']))
    elif select_number == '1호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='1호선']))
    elif select_number == '2호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='2호선']))
    elif select_number == '3호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='3호선']))
    elif select_number == '4호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='4호선']))
    elif select_number == '5호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='5호선']))
    elif select_number == '6호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='6호선']))
    elif select_number == '8호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='8호선']))
    elif select_number == '7호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='7호선']))
    elif select_number == '9호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='9호선']))
    elif select_number == '경춘선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='경춘선']))
    elif select_number == '인천1호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='인천1호선']))
    elif select_number == '중앙선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='중앙선']))
    elif select_number == '경의중앙선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='경의중앙선']))
    elif select_number == '신분당선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='신분당선']))
    elif select_number == '수인선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='수인선']))
    elif select_number == '공항철도':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='공항철도']))
    elif select_number == '수인분당선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='수인분당선']))
    elif select_number == '의정부':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='의정부']))
    elif select_number == '인천2호선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='인천2호선']))
    elif select_number == '우이신설선':
        station = st.radio("Which station are you curious about?",list(df.지하철역명[역_호선명.지하철호선명=='우이신설선']))
with col2 :
    st.write('The selected subway station is', station)
