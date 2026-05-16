def load_data(uploaded_file):
  df = pd.read_excel(uploaded_file)
  return df

def showdata(df):
  st.subheader("업로드한 장소 목록")
  st.dataframe(df)
  return df

def get_user_input(df):
  selected_region = st.selectbox("지역 선택", df["지역"].unique()) 
  selected_budget = st.number_input("가용예산",  min_value=0, value=10000, step=500)
  return df
