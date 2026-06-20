import streamlit as st
import pandas as pd

st.title("강원생활도우미앱 3.0 - 막국수 맛집 추천")

# 데이터 불러오기
def load_data(uploaded_file):
    place_df = pd.read_excel(uploaded_file, sheet_name="장소정보")
    recommend_df = pd.read_excel(uploaded_file, sheet_name="추천정보")
    return place_df, recommend_df



# 사이클 1: join_data
# - 장소정보 + 추천정보를 place_id 기준으로 결합
def join_data(place_df, recommend_df):
    merged_df = pd.merge(
        recommend_df,
        place_df,
        on="place_id",
        how="left"
    )
    return merged_df



# 원본 데이터 보기

def show_original_data(place_df, recommend_df):
    st.subheader("장소정보 시트")
    st.dataframe(place_df)

    st.subheader("추천정보 시트")
    st.dataframe(recommend_df)



# 조인 데이터 보기

def show_joined_data(df):
    st.subheader("조인된 데이터")
    st.dataframe(df)



# 사이클 2: search_places
# - 7개 조건(지역/추천목적/추천상황/추천대상/예산/매운맛선택/단체석여부)으로 검색

def search_places(df):
    st.subheader("막국수 맛집 검색")

    selected_region = st.selectbox("지역 선택", df["지역"].unique())
    selected_purpose = st.selectbox("추천목적 선택", df["추천목적"].unique())
    selected_situation = st.selectbox("추천상황 선택", df["추천상황"].unique())
    selected_target = st.selectbox("추천대상 선택", df["추천대상"].unique())
    selected_spicy = st.selectbox("매운맛선택", df["매운맛선택"].unique())
    selected_group = st.selectbox("단체석여부", df["단체석여부"].unique())

    selected_budget = st.number_input(
        "최대 예산 (원)",
        min_value=0,
        value=10000,
        step=500
    )

    result = df[
        (df["지역"] == selected_region) &
        (df["추천목적"] == selected_purpose) &
        (df["추천상황"] == selected_situation) &
        (df["추천대상"] == selected_target) &
        (df["매운맛선택"] == selected_spicy) &
        (df["단체석여부"] == selected_group) &
        (df["예산"] <= selected_budget)
    ]

    st.subheader("검색 결과")

    if len(result) > 0:
        
        show_cols = ["이름", "지역", "주소", "운영시간", "추천목적",
                     "추천상황", "추천대상", "막국수종류", "대표메뉴가격",
                     "매운맛선택", "단체석여부"]
        st.dataframe(result[show_cols])
    else:
        st.warning("조건에 맞는 맛집이 없습니다. 조건을 다시 선택해보세요.")



# 데이터 시각화

def show_chart(df):
    st.subheader("데이터 시각화")

    chart_option = st.selectbox(
        "시각화 기준 선택",
        ["지역", "추천목적", "추천상황", "추천대상", "매운맛선택", "단체석여부"]
    )

    chart_data = df[chart_option].value_counts()

    st.bar_chart(chart_data)



# 메인 화면

uploaded_file = st.file_uploader(
    "강원도 막국수 맛집 엑셀 파일을 업로드하세요",
    type=["xlsx"]
)

if uploaded_file is not None:
    place_df, recommend_df = load_data(uploaded_file)
    merged_df = join_data(place_df, recommend_df)

    menu = st.sidebar.radio(
        "메뉴 선택",
        ["원본 데이터 보기", "조인 데이터 보기", "맛집 검색", "데이터 시각화"]
    )

    if menu == "원본 데이터 보기":
        show_original_data(place_df, recommend_df)

    elif menu == "조인 데이터 보기":
        show_joined_data(merged_df)

    elif menu == "맛집 검색":
        search_places(merged_df)

    elif menu == "데이터 시각화":
        show_chart(merged_df)
else:
    st.info("왼쪽 위 업로드 버튼으로 gangwon_makguksu_data.xlsx 파일을 올려주세요.")
