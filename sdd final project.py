import streamlit as st
import pandas as pd

st.title("강원생활도우미앱 - 막국수 맛집 추천")


def load_data(uploaded_file):
    place_df = pd.read_excel(uploaded_file, sheet_name="장소정보")
    recommend_df = pd.read_excel(uploaded_file, sheet_name="추천정보")
    return place_df, recommend_df


def join_data(place_df, recommend_df):
    merged_df = pd.merge(
        recommend_df,
        place_df,
        on="place_id",
        how="left"
    )
    return merged_df


def show_original_data(place_df, recommend_df):
    st.subheader("장소정보 시트")
    st.dataframe(place_df)
    st.subheader("추천정보 시트")
    st.dataframe(recommend_df)


def show_joined_data(df):
    st.subheader("조인된 데이터")
    st.dataframe(df)


def search_places(df):
    st.subheader("막국수 맛집 검색")

    region_options   = ["전체"] + sorted(df["지역"].unique().tolist())
    situation_options = ["전체"] + sorted(df["추천상황"].unique().tolist())
    spicy_options    = ["전체"] + sorted(df["매운맛선택"].unique().tolist())
    group_options    = ["전체"] + sorted(df["단체석여부"].unique().tolist())

    selected_region    = st.selectbox("지역 선택",    region_options)
    selected_situation = st.selectbox("추천상황 선택", situation_options)
    selected_spicy     = st.selectbox("매운맛선택",   spicy_options)
    selected_group     = st.selectbox("단체석여부",   group_options)

    selected_budget = st.number_input(
        "최대 예산 (원)", min_value=0, value=11000, step=500
    )
    selected_rating = st.slider(
        "최소 평점", min_value=0.0, max_value=5.0, value=4.0, step=0.1
    )

    result = df.copy()
    if selected_region    != "전체": result = result[result["지역"]    == selected_region]
    if selected_situation != "전체": result = result[result["추천상황"] == selected_situation]
    if selected_spicy     != "전체": result = result[result["매운맛선택"] == selected_spicy]
    if selected_group     != "전체": result = result[result["단체석여부"] == selected_group]
    result = result[result["예산"] <= selected_budget]
    result = result[result["평점"] >= selected_rating]

    st.subheader("검색 결과")
    if len(result) > 0:
        show_cols = ["이름", "지역", "주소", "운영시간", "평점",
                     "대표막국수", "대표메뉴가격", "추천상황", "매운맛선택", "단체석여부"]
        st.dataframe(result[show_cols])
    else:
        st.warning("조건에 맞는 맛집이 없습니다. 조건을 다시 선택해보세요.")


def show_chart(df):
    st.subheader("데이터 시각화")
    chart_option = st.selectbox(
        "시각화 기준 선택",
        ["지역", "추천상황", "매운맛선택", "단체석여부"]
    )
    chart_data = df[chart_option].value_counts()
    st.bar_chart(chart_data)


def sort_by_rating(result):
    out = result.copy()
    out = out.sort_values("평점", ascending=False)
    return out


def make_reason(result):
    out = result.copy()
    def 문장만들기(row):
        return (f"{row['이름']}은(는) {row['지역']}에 위치하며 "
                f"평점 {row['평점']}, 예산 {row['대표메뉴가격']}이에요! "
                f"추천상황: {row['추천상황']}")
    out['추천이유'] = out.apply(문장만들기, axis=1)
    return out


def show_top_recommendation(df):
    st.subheader("평점순 맛집 추천")

    region_options = ["전체"] + sorted(df["지역"].unique().tolist())
    selected_region = st.selectbox("지역 선택", region_options)

    result = df.copy()
    if selected_region != "전체":
        result = result[result["지역"] == selected_region]

    정렬결과 = sort_by_rating(result)
    최종결과 = make_reason(정렬결과)

    show_cols = ["이름", "지역", "평점", "대표메뉴가격", "추천상황", "추천이유"]
    st.dataframe(최종결과[show_cols].drop_duplicates(subset=["이름", "추천상황"]))


uploaded_file = st.file_uploader(
    "강원도 막국수 맛집 엑셀 파일을 업로드하세요",
    type=["xlsx"]
)

if uploaded_file is not None:
    place_df, recommend_df = load_data(uploaded_file)
    merged_df = join_data(place_df, recommend_df)

    menu = st.sidebar.radio(
        "메뉴 선택",
        ["원본 데이터 보기", "조인 데이터 보기", "맛집 검색", "데이터 시각화", "평점순 추천"]
    )

    if menu == "원본 데이터 보기":
        show_original_data(place_df, recommend_df)
    elif menu == "조인 데이터 보기":
        show_joined_data(merged_df)
    elif menu == "맛집 검색":
        search_places(merged_df)
    elif menu == "데이터 시각화":
        show_chart(merged_df)
    elif menu == "평점순 추천":
        show_top_recommendation(merged_df)
else:
    st.info("왼쪽 위 업로드 버튼으로 gangwon_makguksu_data.xlsx 파일을 올려주세요.")
