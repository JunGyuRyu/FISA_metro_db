import pandas as pd
import streamlit as st
import pandas as pd

color = {'서해선':'#81A914',
         '자기부상선':'#FFCD12',
         '경강선':'#003DA5',
         '1호선':'#005244',
         '2호선':'#00A84D',
         '3호선':'#EF7C1C',
         '4호선':'#00A5DE',
         '5호선':'#996CAC',
         '6호선':'#CD7C2F',
         '7호선':'#747F00',
         '8호선':'#E6186C',
         '9호선':'#BB8336',
         '경춘선':'#0C8E72',
         '인천1호선':'#7CA8D5',
         '중앙선':'#77C4A3',
         '경의중앙선':'#77C4A3',
         '신분당선':'#D4003B',
         '수인선':'#F5A200',
         '공항철도':'#0090D2',
         '수인분당선':'#F5A200',
         '의정부':'#FDA600',
         '인천2호선':'#ED8B00',
         '우이신설':'#B0CE18'}


fix_지하철역_호선명매핑 = pd.read_csv('fix_지하철역_호선명매핑.csv', encoding='utf_8_sig')
master_path = pd.read_csv('master_path.csv', encoding='utf_8_sig')

col1, col2, col3 = st.columns([1,1,1])
col1.write("TEST")

with col1:
    i = st.text_input('출발역')
    o = st.text_input('도착역')

condition1 = (master_path.이전지하철역명 == i)
condition2 = (master_path.다음지하철역명 == o)

df1 = master_path.loc[condition1]
df2 = df1.loc[condition2]
df = []
temp = []

id_list1 = df2.iloc[0].SHT_STATN_ID.split('.')
id_list2 = df2.iloc[0].SHT_STATN_NM.split('.')
id_list3 = df2.iloc[0].지하철호선명.split('.')

for i in id_list1:
    temp.append(i)
temp.pop()
df.append(temp)
temp = []

for i in id_list2:
    temp.append(i)
temp.pop()
df.append(temp)
temp = []

df.append([])

for i in df[0]:
    int(i)
    a = fix_지하철역_호선명매핑.loc[fix_지하철역_호선명매핑.지하철역ID == int(i)].지하철호선명
    for _ in a:
        df[2].append(_)
temp = []

df = pd.DataFrame(df)
df = df.T

df.rename(columns = {0:"ID", 1:"역", 2:"호선"}, inplace=True)

def color_survived(c_name):
    path_color = color[c_name]
    return f'background-color: {path_color}; color: white'


with col2:
    st.dataframe(df.style.applymap(color_survived, subset=['호선']), hide_index=True)

with col3:
    st.text_area(label="소요 시간", value=str(df2.iloc[0].SHT_TRAVEL_MSG))
