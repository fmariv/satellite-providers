import streamlit as st


def main():
    st. set_page_config(layout="wide")
    # Read README.md file
    with open('README.md', 'r', encoding='utf-8') as file:
        readme_content = file.read()

    # Show README.md file as a web page
    st.markdown(readme_content, unsafe_allow_html=True)


if __name__ == '__main__':
    main()