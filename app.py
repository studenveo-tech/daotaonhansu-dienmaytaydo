import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang
st.set_page_config(
    page_title="Đào tạo nhân sự - Điện Máy Tây Đô",
    page_icon="💧",
    layout="wide"
)

def render_html_template():
    # Thay "template.html" thành đúng tên file HTML dài của bạn trên GitHub
    file_name = "h_th_ng_o_t_o_nh_n_s_n_i_b_i_n_m_y_t_y_dienmaytaydo_com.html"
    ...
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h3 style='color:red; text-align:center;'>Lỗi: Không tìm thấy file template.html trên GitHub!</h3>"

# Hiển thị giao diện trực tiếp
html_string = render_html_template()
components.html(html_string, height=1200, scrolling=True)
