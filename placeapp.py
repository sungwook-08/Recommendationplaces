
if "placelist" not in st.session_state:
    st.session_state.placelist = [
   {"이름": "가톨릭관동대학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "잔디가 좋지만, 관객석이 더러운 곳"},
   {"이름": "문성고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "고지대에 있어서 산에서 축구하는 느낌이 나는 곳"},
   {"이름": "강릉고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "소나무가 많아서 공기가 좋은곳"},
   {"이름": "제일고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "축구부가 있어 최고의 잔디를 느낄 수 있는 곳"}
   {"이름": "강원대학교 강릉캠퍼스", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 20000, "한줄설명": "밤 11시까지 불이 켜지는 밤에도 축구하기 좋은 곳"}
   {"이름": "강남축구공원", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 50000 , "한줄설명": "풋살장2개, 축구장2개가 있는 곳"}
]



def show_all_places(place_list):
    st.subheader("전체 장소 보기")
    for place in place_list:
        # 아래 빈칸을 완성하세요
        st.write("장소 이름:", 강남축구공원)
        st.write("지역:",강릉)
        st.write("좋음/안좋음:", 안좋음)
        st.write("예산:", ____________________, "원")
        st.write("설명:", 운동장이 4개나 있는곳)
        st.write("---")


def find_places(place_list, region, place_type, budget):
    result = []
    for place in place_list:
        # 아래 조건문을 완성하세요
        if ______________________________________________:
              result.append(place)
      return result


def add_place(place_list, name, region, place_type, budget, description):
    new_place = {
        "이름": ____________________,
        "지역": ____________________,
        "실내여부": ____________________,
        "예산": ____________________,
        "한줄설명": ____________________
    }
    place_list.append(new_place)


st.title("강원생활도우미앱")

menu = st.selectbox("기능을 선택하세요", ["전체 보기", "추천 받기", "장소 추가"])

if menu == "전체 보기":
    show_all_places(placelist)

elif menu == "추천 받기":
    region = st.selectbox("지역을 선택하세요", ["강릉", "속초", "춘천"])
    place_type = st.selectbox("실내/실외를 선택하세요", ["실내", "실외"])
    budget = st.number_input("사용 가능한 예산을 입력하세요", min_value=0, step=1000, value=5000)

    result_places = find_places(placelist, region, place_type, budget)

    st.subheader("추천 결과")

    # 아래 빈칸을 완성하세요
    if __________________________________:
        for place in result_places:
            st.write("장소 이름:", place["이름"])
            st.write("설명:", place["한줄설명"])
            st.write("예산:", place["예산"], "원")
            st.write("---")
    else:
        st.write("조건에 맞는 장소가 없습니다")

elif menu == "장소 추가":
    name = st.text_input("장소 이름을 입력하세요")
    region = st.selectbox("지역을 선택하세요", ["강릉", "속초", "춘천"])
    place_type = st.selectbox("실내/실외를 선택하세요", ["실내", "실외"])
    budget = st.number_input("예산을 입력하세요", min_value=0, step=1000)
    description = st.text_input("한줄 설명을 입력하세요")

    if st.button("장소 추가"):
        # 아래 함수 호출을 완성하세요
        ______________________________________________
        st.success("새 장소가 추가되었습니다")
