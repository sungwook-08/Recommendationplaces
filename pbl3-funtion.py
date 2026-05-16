def load_data(uploaded_file):
  df = pd.read_excel(uploaded_file)
  return df

def showdata(df):
  st.subheader("업로드한 장소 목록")
  st.dataframe(df)
  return df

def get_user_input(df)
  selected_regjion = st.selectbox(
