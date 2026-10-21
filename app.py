import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang chiếm toàn bộ chiều rộng
st.set_page_config(
    page_title="Đào tạo nhân sự - Điện Máy Tây Đô",
    page_icon="💧",
    layout="wide"
)

# Hàm đọc file HTML giao diện
def render_html_template():
    # Thay "dienmaytaydo.html" bằng tên chính xác của file HTML bạn đã tải lên GitHub
    file_name = "dienmaytaydo.html" 
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        return f"""
        <div style="padding: 20px; font-family: sans-serif; color: #721c24; background-color: #f8d7da; border: 1px solid #f5c6cb; border-radius: 5px;">
            <h3>Lỗi hệ thống: Không tìm thấy tệp giao diện ({file_name})</h3>
            <p>Vui lòng kiểm tra lại xem bạn đã tải file HTML lên kho lưu trữ GitHub chưa và tên file trong code đã khớp hoàn toàn chưa.</p>
        </div>
        """

# Hiển thị giao diện HTML trực tiếp công khai cho mọi người truy cập
html_string = render_html_template()
components.html(html_string, height=1200, scrolling=True)
