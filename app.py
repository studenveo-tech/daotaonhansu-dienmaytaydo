import streamlit as st
import pandas as pd
import json

# Cấu hình trang
st.set_page_config(page_title="Đào tạo nhân sự - Điện Máy Tây Đô", page_icon="🎓", layout="wide")

# 1. CƠ SỞ DỮ LIỆU TÀI KHOẢN
USERS_DB = {
    "minh.nv": {"password": "123", "name": "Nguyễn Văn Minh", "role": "Sale Showroom", "progress": 20},
    "hoa.tt": {"password": "123", "name": "Trần Thị Hoa", "role": "CSKH Online", "progress": 45},
    "tuan.kt": {"password": "123", "name": "Lê Anh Tuấn", "role": "Kỹ thuật Lắp đặt", "progress": 80}
}

# 2. DỮ LIỆU SẢN PHẨM & CÂU HỎI TRẮC NGHIỆM
PRODUCTS_DATA = [
    {"id": "KGHP11S5", "name": "Máy Lọc Nước Kangaroo Hydrogen Infinity KGHP11S5", "category": "Máy Lọc Nước Kangaroo", "features": "Dòng cao cấp Hydrogen Infinity, thiết kế hiện đại, tạo nguồn nước khỏe."},
    {"id": "KG12S3H3", "name": "Máy Lọc Nước RO Nóng Nguội Lạnh Hydrogen Kangaroo KG12S3H3", "category": "Máy Lọc Nước Kangaroo", "features": "Hệ thống 12 lõi lọc mạnh mẽ, 3 chế độ Nóng - Nguội - Lạnh."},
    {"id": "GHUF15003C", "name": "Bộ Lọc Tổng Đầu Nguồn Greenhome UF 1500L/H 3 Cốc", "category": "Lọc Tổng - UF", "features": "Công suất 1500L/h, xử lý cặn bùn, phèn nhẹ cho sinh hoạt."},
    {"id": "GHBCN150L", "name": "Máy Lọc Nước Bán Công Nghiệp Greenhome GHBCN150L", "category": "Máy Bán Công Nghiệp", "features": "Công suất 150L/h, phù hợp xí nghiệp, trường học, bệnh viện."},
    {"id": "KGWD45P1", "name": "Máy Tắm Nóng Trực Tiếp Kangaroo 450W KGWD45P1 (Có Bơm)", "category": "Máy Tắm Nóng", "features": "Tích hợp bơm trợ lực cho khu vực nước yếu, chống giật ELCB."}
]

QUIZ_DATA = [
    {"question": "Điện Máy Tây Đô là đại lý phân phối chính thức của thương hiệu nào?", "options": ["Sunhouse", "Kangaroo & Greenhome", "Karofi", "Daikin"], "answer": "Kangaroo & Greenhome"},
    {"question": "Dòng Máy lọc nước Kangaroo KG12S3H3 có tổng cộng bao nhiêu lõi lọc?", "options": ["9 lõi", "10 lõi", "11 lõi", "12 lõi"], "answer": "12 lõi"},
    {"question": "Khách hàng ở Miền Tây có nước nhiễm phèn, nên tư vấn sản phẩm nào?", "options": ["Máy làm mát không khí", "Bộ Lọc Tổng Đầu Nguồn Composite", "Cây nước nóng lạnh", "Thay lõi số 1"], "answer": "Bộ Lọc Tổng Đầu Nguồn Composite"}
]

df_products = pd.DataFrame(PRODUCTS_DATA)

# 3. KHỞI TẠO PHIÊN ĐĂNG NHẬP
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''
    st.session_state['name'] = ''
    st.session_state['role'] = ''
    st.session_state['progress'] = 0

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

def logout():
    st.session_state['logged_in'] = False
    st.rerun()

# 4. GIAO DIỆN CHÍNH SAU KHI ĐĂNG NHẬP
if not st.session_state['logged_in']:
    login()
else:
    # Header cá nhân hóa
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

    if st.button("🚪 Đăng xuất tài khoản", type="secondary"):
        logout()

    # Menu chức năng chính
    tab1, tab2, tab3 = st.tabs(["📚 Tra cứu Sản phẩm & Cẩm nang", f"🎓 Học phần Đào tạo ({st.session_state['role']})", "📝 Sát hạch & Kiểm tra"])

    with tab1:
        st.subheader("📚 Tra cứu Nhanh Sản phẩm Điện Máy Tây Đô")
        search_term = st.text_input("Tìm kiếm theo tên hoặc mã sản phẩm (VD: KGHP11S5):")
        
        filtered_df = df_products
        if search_term:
            filtered_df = filtered_df[filtered_df['name'].str.contains(search_term, case=False) | filtered_df['id'].str.contains(search_term, case=False)]
            
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader(f"🎓 Nội dung Đào tạo chuyên sâu cho vị trí: {st.session_state['role']}")
        if st.session_state['role'] == "Kỹ thuật Lắp đặt":
            st.info("🛠️ **Học phần Kỹ thuật:**\n- Hướng dẫn lắp đặt máy lọc nước RO Nóng Nguội Lạnh.\n- Quy trình lắp đặt hệ thống lọc tổng Composite / UF cho nhà dân và doanh nghiệp miền Tây.\n- Cách xử lý sự cố rò rỉ nước, thay lõi định kỳ.")
        elif st.session_state['role'] == "Sale Showroom":
            st.success("💬 **Học phần Bán hàng:**\n- Kỹ thuật tư vấn dòng máy Hydrogen Ion Kiềm cao cấp.\n- Xử lý các tình huống từ chối giá cả của khách hàng tại Cần Thơ.\n- Kịch bản chốt đơn hàng B2C và B2B.")
        else:
            st.success("📞 **Học phần CSKH:**\n- Kỹ năng tiếp nhận thông tin bảo hành, bảo dưỡng qua Hotline & Zalo OA.\n- Quy trình nhắc lịch thay lõi lọc định kỳ cho khách hàng cũ.")

    with tab3:
        st.subheader("📝 Bài kiểm tra sát hạch nghiệp vụ")
        score = 0
        with st.form("quiz_form"):
            user_answers = {}
            for i, q in enumerate(QUIZ_DATA):
                st.write(f"**Câu {i+1}: {q['question']}**")
                user_answers[i] = st.radio("Chọn đáp án đúng:", q['options'], key=f"q_{i}", index=None)
                st.write("---")
            
            submitted = st.form_submit_button("Nộp bài sát hạch")
            if submitted:
                for i, q in enumerate(QUIZ_DATA):
                    if user_answers[i] == q['answer']:
                        score += 1
                    else:
                        st.error(f"❌ Câu {i+1} chưa chính xác. Đáp án đúng: **{q['answer']}**")
                st.success(f"🎯 Kết quả bài thi của bạn: {score}/{len(QUIZ_DATA)}")
                if score == len(QUIZ_DATA):
                    st.balloons()
