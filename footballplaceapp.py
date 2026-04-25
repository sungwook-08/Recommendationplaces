import streamlit as st

# 1. 초기 데이터 세팅 (쉼표 누락 오류 수정)
if "placelist" not in st.session_state:
    st.session_state.placelist = [
        {"이름": "가톨릭관동대학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "잔디가 좋지만, 관객석이 더러운 곳"},
        {"이름": "문성고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "고지대에 있어서 산에서 축구하는 느낌이 나는 곳"},
        {"이름": "강릉고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "소나무가 많아서 공기가 좋은곳"},
        {"이름": "제일고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "축구부가 있어 최고의 잔디를 느낄 수 있는 곳"},
        {"이름": "강원대학교 강릉캠퍼스", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 20000, "한줄설명": "밤 11시까지 불이 켜지는 밤에도 축구하기 좋은 곳"},
        {"이름": "강남축구공원", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 50000 , "한줄설명": "풋살장2개, 축구장2개가 있는 곳"}
    ]

def show_all_places(place_list):
    st.subheader("전체 장소 보기")
    for place in place_list:
        st.write("장소 이름:", place["이름"])
        st.write("지역:", place["지역"])
        st.write("잔디상태:", place["잔디상태"])
        st.write("시간당 사용료:", place["시간당 사용료"], "원")
        st.write("설명:", place["한줄설명"])
        st.write("---")

def find_places(place_list, region, turf_condition, max_fee):
    result = []
    for place in place_list:
        # 지역과 잔디상태가 일치하고, 사용료가 입력한 예산(max_fee) 이하인 곳 필터링
        if place["지역"] == region and place["잔디상태"] == turf_condition and place["시간당 사용료"] <= max_fee:
            result.append(place)
    return result

def add_place(place_list, name, region, turf_condition, fee, description):
    new_place = {
        "이름": name,
        "지역": region,
        "잔디상태": turf_condition,
        "시간당 사용료": fee,
        "한줄설명": description
    }
    place_list.append(new_place)

st.title("강원생활도우미앱")

menu = st.selectbox("기능을 선택하세요", ["전체 보기", "추천 받기", "장소 추가"])

# session_state에 저장된 리스트를 사용해야 데이터가 유지됩니다.
current_placelist = st.session_state.placelist

if menu == "전체 보기":
    show_all_places(current_placelist)

elif menu == "추천 받기":
    region = st.selectbox("지역을 선택하세요", ["강릉", "속초", "춘천"])
    turf_condition = st.selectbox("잔디상태를 선택하세요", ["좋음", "안좋음"])
    max_fee = st.number_input("사용 가능한 예산(시간당 사용료)을 입력하세요", min_value=0, step=1000, value=5000)

    result_places = find_places(current_placelist, region, turf_condition, max_fee)

    st.subheader("추천 결과")

    if result_places: # 리스트에 값이 하나라도 있다면 (추천 결과가 있다면)
        for place in result_places:
            st.write("장소 이름:", place["이름"])
            st.write("설명:", place["한줄설명"])
            st.write("시간당 사용료:", place["시간당 사용료"], "원")
            st.write("---")
    else:
        st.write("조건에 맞는 장소가 없습니다")

elif menu == "장소 추가":
    name = st.text_input("장소 이름을 입력하세요")
    region = st.selectbox("지역을 선택하세요", ["강릉", "속초", "춘천"])
    turf_condition = st.selectbox("잔디상태를 선택하세요", ["좋음", "안좋음"])
    fee = st.number_input("시간당 사용료를 입력하세요", min_value=0, step=1000)
    description = st.text_input("한줄 설명을 입력하세요")

    if st.button("장소 추가"):
        add_place(current_placelist, name, region, turf_condition, fee, description)
        st.success("새 장소가 추가되었습니다")
