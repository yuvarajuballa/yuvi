import streamlit as st
import pandas as pd
import pickle
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

df=pickle.load(open('df.pkl','rb'))
tfidf_matrix=pickle.load(open('tfidf_matrix.pkl','rb'))



def jobs_recommendation(Title):
    idx=df[df['skills']==Title].index[0]
    idx=df.index.get_loc(idx)
    similarity_scores = sorted(list(enumerate(tfidf_matrix[idx])), key=lambda x: x[1], reverse=True)[1:5]
    newsindices = [i[0] for i in similarity_scores]
    return df[['jobtitle', 'skills', 'company']].iloc[newsindices]





#web app
if __name__=="__main__":


    st.title('Job Recommendation System')
    Title=st.selectbox('search job',df['skills'])

    if st.button('Get Recommendation'):
        st.subheader('Recommended Jobs')

        jobs=jobs_recommendation(Title)


        st.write(jobs)


