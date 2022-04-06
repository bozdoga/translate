
from io import StringIO
import streamlit as st
import boto3


languages = ['auto','en','de','fr','cn','tr','nl']

st.title('Translator')

to_translate = st.text_area('Please specify the text you need translated')

col1,col2=st.columns(2)
with col1:
    trigger=st.button('Translate')
with col2:
    add_file = st.file_uploader('Please add your file',type=['pdf','doc'])
    if add_file is not None:
        stringio=StringIO(add_file.getvalue().decode("utf-8"))
        text_data = stringio.read()
        st.write(text_data)




source_language = st.selectbox('Translate from',languages)
target_language = st.selectbox('to language',languages)


def translate(to_translate):
    translate = boto3.client(service_name='translate',region_name="us-east-1",use_ssl=True)
    result=translate.translate_text(Text=to_translate,SourceLanguageCode=source_language, TargetLanguageCode=target_language)
    st.write(str(result.get('TranslatedText')))


if trigger:
    translate(to_translate)




