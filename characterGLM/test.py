import streamlit as st

st.text_input('动态输入框', key='aaa',value='新的值')

def main():
    st.title('动态赋值给输入框示例')
    
    # 创建一个按钮
    button_clicked = st.button('点击我更新输入框的值')
    
    # 如果按钮被点击
    if button_clicked:
        # 通过st.text_input方法创建输入框，并动态赋值
        new_value = st.text_input('动态输入框', key='aaa',value='新的值')

if __name__ == "__main__":
    main()
