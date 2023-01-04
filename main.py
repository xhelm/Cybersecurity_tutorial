import streamlit as st
import input
body = """
1. Password should be longer than or equal to 8 characters.
2. Include atleast one lower case alphabet.
3. Include atleast one Uppercase.
4. Include atleast one number.
5. Include atleast one special character.
"""
def main():
    st.set_page_config(page_title='Password Checker',  initial_sidebar_state = 'auto')
    input.input_form()
    
    my_expander = st.expander(label='Expand me')
    with my_expander:
        body



if __name__ == '__main__':
    main()

