import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang chiếm toàn bộ chiều rộng
st.set_page_config(
    page_title="Đào tạo nhân sự - Điện Máy Tây Đô",
    page_icon="💧",
    layout="wide"
)

def render_html_template():
    # Khớp chính xác 100% với tên file HTML bạn đã tải lên GitHub
    file_name = "h_th_ng_o_t_o_nh_n_s_n_i_b_i_n_m_y_t_y_dienmaytaydo_com.html"
    
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        return f"""
        <div style="padding: 20px; font-family: sans-serif; color: #721c24; background-color: #f8d7da; border: 1px solid #f5c6cb; border-radius: 5px;">
            <h3>Lỗi hệ thống: Không tìm thấy tệp giao diện ({file_name})</h3>
            <p>Vui lòng kiểm tra lại tên file HTML trên kho lưu trữ GitHub.</p>
        </div>
        """

# Hiển thị giao diện trực tiếp không cần đăng nhập tài khoản
html_string = render_html_template()
components.html(html_string, height=1200, scrolling=True)
