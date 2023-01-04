import streamlit as st
import re
import base64
# @st.cache(suppress_st_warning=True)
def passcheker(test):
    regExLower=re.compile(r'[a-z]+')
    regeExUpper=re.compile(r'[A-Z]+')
    regExNum=re.compile(r'\d')
    regExSC = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
    lower=regExLower.findall(test)
    upper=regeExUpper.findall(test)
    num=regExNum.findall(test)
    spchar= regExSC.findall(test)

    flag=True
    if len(test)>=8:
        if lower:
            if upper:
                if num:
                    if spchar:
                        flag=True
                        st.success(test+" is a strong password",icon="✅")
                    else:
                        flag=False
                        st.error("Include atleast one special character")
                else:
                    flag=False
                    st.error("Include atleast one number")
            else:
                flag=False
                st.error("Include atleast one Uppercase")
        else:        
            flag=False
            st.error("Include atleast one lower case alphabet")
    else:
        flag=False
        st.error("Length of the password should be atleast 8")

    if not flag:
        st.error(test+" is a weak password")


def input_form():
    st.markdown(f'<h1 style="text-align:center; padding 25px">{"Password checker"}</h1>',unsafe_allow_html=True)
    with st.form('input form'):
        pschk = st.text_input('Pasword')
        res= st.form_submit_button("Check")
    if pschk =='' and res:
        st.error("Input cannot be empty")
    elif pschk!="" and res:
        passcheker(pschk)

        # elif res==False:
        #     file_ = open("./assets/password.gif", "rb")
        #     contents = file_.read()
        #     data_url = base64.b64encode(contents).decode("utf-8")
        #     file_.close()
        #     st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="">',unsafe_allow_html=True,)

