import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Đào tạo nhân sự - Điện Máy Tây Đô", page_icon="🎓", layout="wide")

# CƠ SỞ DỮ LIỆU TÀI KHOẢN MẪU (Tên đăng nhập và mật khẩu của nhân viên)
USERS_DB = {
    "minh.nv": {"password": "123", "name": "Nguyễn Văn Minh", "role": "Sale Showroom", "progress": 15},
    "hoa.tt": {"password": "123", "name": "Trần Thị Hoa", "role": "CSKH Online", "progress": 45},
    "tuan.kt": {"password": "123", "name": "Lê Anh Tuấn", "role": "Kỹ thuật Lắp đặt", "progress": 80}
}

# Khởi tạo trạng thái phiên làm việc (Session State)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''
    st.session_state['name'] = ''
    st.session_state['role'] = ''
    st.session_state['progress'] = 0

# Hàm giao diện đăng nhập
def login():
    st.markdown("<h2 style='text-align: center; color: #059669;'>ĐĂNG NHẬP HỆ THỐNG ACADEMY</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Điện Máy Tây Đô - Đại Lý Kangaroo Cần Thơ & Miền Tây</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("Tên đăng nhập (Thử: minh.nv, hoa.tt, hoặc tuan.kt)")
            password = st.text_input("Mật khẩu (Mặc định: 123)", type="password")
            submit_button = st.form_submit_button("Đăng nhập", use_container_width=True)

            if submit_button:
                if username in USERS_DB and USERS_DB[username]["password"] == password:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.session_state['name'] = USERS_DB[username]["name"]
                    st.session_state['role'] = USERS_DB[username]["role"]
                    st.session_state['progress'] = USERS_DB[username]["progress"]
                    st.rerun()
                else:
                    st.error("❌ Tên đăng nhập hoặc mật khẩu không đúng!")

# Hàm đăng xuất
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''
    st.session_state['name'] = ''
    st.session_state['role'] = ''
    st.session_state['progress'] = 0
    st.rerun()

# Kiểm tra trạng thái đăng nhập
if not st.session_state['logged_in']:
    login()
else:
    # GIAO DIỆN CHÍNH SAU KHI ĐĂNG NHẬP (Hiển thị đúng tên và vị trí của người đó)
    st.markdown(f"""
        <div style="background: linear-gradient(to right, #065f46, #047857); padding: 15px; border-radius: 10px; color: white; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <div>
                <h3 style="margin: 0;">ĐIỆN MÁY TÂY ĐÔ ACADEMY</h3>
                <span style="font-size: 12px; color: #a7f3d0;">Hệ thống Đào tạo & Sát hạch Nhân sự Nội bộ</span>
            </div>
            <div style="display: flex; gap: 15px; align-items: center;">
                <div style="background: rgba(255,255,255,0.1); padding: 5px 15px; border-radius: 5px; font-size: 14px;">
                    Vị trí: <b>{st.session_state['role']}</b>
                </div>
                <div style="background: white; color: #065f46; padding: 5px 15px; border-radius: 5px; font-weight: bold; font-size: 14px;">
                    NV: {st.session_state['name']} <span style="background: #d1fae5; color:#065f46; padding: 2px 8px; border-radius: 10px; margin-left: 5px;">{st.session_state['progress']}%</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Nút đăng xuất nằm ở góc
    if st.button("🚪 Đăng xuất tài khoản", type="secondary"):
        logout()

    st.write("---")
    
    # Phân quyền hiển thị nội dung học tập theo từng vị trí công việc
    if st.session_state['role'] == "Kỹ thuật Lắp đặt":
        st.subheader("🛠️ Khu vực đào tạo: Kỹ thuật Lắp đặt & Bảo hành")
        st.info("Nội dung: Sơ đồ lắp đặt máy lọc nước Kangaroo, hệ thống lọc tổng Greenhome, quy trình bảo trì định kỳ tại nhà khách ở Cần Thơ & Miền Tây.")
    else:
        st.subheader(f"💬 Khu vực đào tạo chuyên sâu dành cho: {st.session_state['role']}")
        st.success("Nội dung: Cẩm nang sản phẩm, thông số kỹ thuật máy lọc nước Hydrogen, kịch bản tư vấn chốt sale và xử lý từ chối.")
