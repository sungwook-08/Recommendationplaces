import streamlit as st

if "placelist" not in st.session_state:
    st.session_state.placelist = [
        {"이름": "가톨릭관동대학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "잔디가 좋지만, 관객석이 더러운 곳"},
        {"이름": "문성고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "고지대에 있어서 산에서 축구하는 느낌이 나는 곳"},
        {"이름": "강릉고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "소나무가 많아서 공기가 좋은곳"},
        {"이름": "제일고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "축구부가 있어 최고의 잔디를 느낄 수 있는 곳"},
        {"이름": "강원대학교 강릉캠퍼스", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 20000, "한줄설명": "밤 11시까지 불이 켜지는 밤에도 축구하기 좋은 곳"},
        {"이름": "강남축구공원", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 50000, "한줄설명": "풋살장2개, 축구장2개가 있는 곳"},
        {"이름": "엑스포잔디광장", "지역": "속초", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "청초호 옆에 있어 호수도 갈 수 있지만, 골대가 없는 곳"},
        {"이름": "공지천인조잔디구장", "지역": "춘천", "잔디상태": "좋음", "시간당 사용료": 10000, "한줄설명": "손흥민이 어린시절 아버지와 함께 훈련하던 곳"}
    ]

def show_all_places(place_list):
    st.subheader("전체 장소 보기")
    for place in place_list:
        st.write(f"**장소 이름:** {place['이름']}")
        st.write(f"지역: {place['지역']} | 잔디상태: {place['잔디상태']}")
        st.write(f"시간당 사용료: {place['시간당 사용료']:,} 원")
        st.write(f"설명: {place['한줄설명']}")
        st.divider()

def find_places(place_list, region, turf_condition, max_fee):
    result = []
    for place in place_list:
        if (place["지역"] == region and 
            place["잔디상태"] == turf_condition and 
            int(place["시간당 사용료"]) <= max_fee):
            result.append(place)
    return result

def add_place(name, region, turf_condition, fee, description):
    new_place = {
        "이름": name,
        "지역": region,
        "잔디상태": turf_condition,
        "시간당 사용료": fee,
        "한줄설명": description
    }
    st.session_state.placelist.append(new_place)

st.title("⚽ 강원생활도우미앱")

menu = st.sidebar.selectbox("기능을 선택하세요", ["전체 보기", "무료 장소 보기", "추천 받기", "장소 추가"])

current_placelist = st.session_state.placelist

if menu == "전체 보기":
    show_all_places(current_placelist)

elif menu == "무료 장소 보기":
    st.subheader("💰 무료 장소 목록")
    free_places = [place for place in current_placelist if place["시간당 사용료"] == 0]
    
    if free_places:
        for place in free_places:
            st.success(f"📍 {place['이름']}")
            st.write(f"**지역:** {place['지역']} | **잔디:** {place['잔디상태']}")
            st.write(f"**설명:** {place['한줄설명']}")
            st.divider()
    else:
        st.write("등록된 무료 장소가 없습니다.")

elif menu == "추천 받기":
    st.subheader("맞춤형 축구장 추천")
    region = st.selectbox("지역을 선택하세요", ["강릉", "속초", "춘천"])
    turf_condition = st.selectbox("잔디상태를 선택하세요", ["좋음", "안좋음"])
    max_fee = st.number_input("사용 가능한 예산(최대 사용료)을 입력하세요", min_value=0, step=1000, value=50000)

    if st.button("추천 결과 확인"):
        result_places = find_places(current_placelist, region, turf_condition, max_fee)
        if result_places:
            for place in result_places:
                st.info(f"**{place['이름']}**\n\n- 설명: {place['한줄설명']}\n- 가격: {place['시간당 사용료']}원")
        else:
            st.warning("조건에 맞는 장소가 없습니다.")

elif menu == "장소 추가":
    st.subheader("새로운 장소 등록")
    with st.form("add_new_place"):
        name = st.text_input("장소 이름")
        region = st.selectbox("지역", ["강릉", "속초", "춘천"])
        turf_condition = st.selectbox("잔디상태", ["좋음", "안좋음"])
        fee = st.number_input("시간당 사용료", min_value=0, step=1000)
        description = st.text_input("한줄 설명")
        
        submit = st.form_submit_button("추가하기")
        if submit:
            if name and description:
                add_place(name, region, turf_condition, fee, description)
                st.success(f"'{name}' 장소가 성공적으로 추가되었습니다!")
            else:
                st.error("장소 이름과 설명을 모두 입력해주세요.")
                st.error("장소 이름과 설명을 모두 입력해주세요.")
