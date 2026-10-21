import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang
st.set_page_config(
    page_title="Đào tạo nhân sự - Điện Máy Tây Đô",
    page_icon="💧",
    layout="wide"
)

def render_html_template():
    file_name = "template.html"  # Gọi đúng tên ngắn gọn vừa đổi
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h3 style='color:red; text-align:center;'>Lỗi: Không tìm thấy file template.html trên GitHub!</h3>"

# Hiển thị giao diện trực tiếp
html_string = render_html_template()
components.html(html_string, height=1200, scrolling=True)
