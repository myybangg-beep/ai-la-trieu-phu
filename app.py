import streamlit as st
import random

st.set_page_config(page_title="Ai Là Triệu Phú - Bác Hồ", page_icon="🌟", layout="wide")

# CSS tạo kiểu giao diện
st.markdown("""
    <style>
    .main-title { text-align: center; color: #FFD700; font-size: 2.5rem; font-weight: bold; }
    .question-box { background-color: #1E222A; border: 2px solid #FFD700; border-radius: 10px; padding: 20px; text-align: center; font-size: 1.3rem; color: #FFFFFF; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Bộ 15 câu hỏi về Bác Hồ
QUESTIONS = [
    {"question": "Bác Hồ sinh ngày tháng năm nào?", "options": ["A. 19/05/1890", "B. 02/09/1945", "C. 05/06/1911", "D. 30/04/1975"], "answer": "A. 19/05/1890"},
    {"question": "Tên khai sinh của Chủ tịch Hồ Chí Minh là gì?", "options": ["A. Nguyễn Tất Thành", "B. Nguyễn Sinh Cung", "C. Văn Ba", "D. Nguyễn Ái Quốc"], "answer": "B. Nguyễn Sinh Cung"},
    {"question": "Bác Hồ ra đi tìm đường cứu nước vào năm nào?", "options": ["A. 1905", "B. 1911", "C. 1920", "D. 1930"], "answer": "B. 1911"},
    {"question": "Bác Hồ ra đi tìm đường cứu nước từ cảng nào?", "options": ["A. Cảng Ba Son", "B. Cảng Nhà Bè", "C. Cảng Nhà Rồng", "D. Cảng Hải Phòng"], "answer": "C. Cảng Nhà Rồng"},
    {"question": "Khi rời Việt Nam năm 1911, Bác Hồ lấy tên là gì?", "options": ["A. Văn Ba", "B. Lý Thụy", "C. Nguyễn Ái Quốc", "D. Thầu Chín"], "answer": "A. Văn Ba"},
    {"question": "Bác Hồ đọc bản 'Tuyên ngôn Độc lập' vào ngày nào?", "options": ["A. 19/05/1945", "B. 02/09/1945", "C. 19/08/1945", "D. 22/12/1944"], "answer": "B. 02/09/1945"},
    {"question": "Bản 'Tuyên ngôn Độc lập' được Bác Hồ đọc tại đâu?", "options": ["A. Quảng trường Ba Đình", "B. Bến Nhà Rồng", "C. Hang Pác Bó", "D. Tân Trào"], "answer": "A. Quảng trường Ba Đình"},
    {"question": "Tác phẩm 'Đường Kách mệnh' của Bác Hồ xuất bản vào năm nào?", "options": ["A. 1925", "B. 1927", "C. 1930", "D. 1941"], "answer": "B. 1927"},
    {"question": "Tập thơ 'Nhật ký trong tù' được Bác sáng tác trong giai đoạn nào?", "options": ["A. 1930 - 1931", "B. 1941 - 1942", "C. 1942 - 1943", "D. 1945 - 1946"], "answer": "C. 1942 - 1943"},
    {"question": "Quê nội của Chủ tịch Hồ Chí Minh ở làng nào?", "options": ["A. Làng Hoàng Trù", "B. Làng Sen", "C. Làng Nam Kim", "D. Làng Kim Liên"], "answer": "B. Làng Sen"},
    {"question": "Bác Hồ trở về nước trực tiếp lãnh đạo cách mạng vào năm nào?", "options": ["A. 1930", "B. 1941", "C. 1945", "D. 1954"], "answer": "B. 1941"},
    {"question": "Địa danh nào là nơi Bác Hồ sống và hoạt động đầu tiên khi về nước năm 1941?", "options": ["A. Tân Trào", "B. Pác Bó (Cao Bằng)", "C. Định Hóa", "D. Mường Phăng"], "answer": "B. Pác Bó (Cao Bằng)"},
    {"question": "Bác Hồ tham gia thành lập Đảng Cộng sản Pháp vào năm nào?", "options": ["A. 1919", "B. 1920", "C. 1925", "D. 1930"], "answer": "B. 1920"},
    {"question": "TP. Sài Gòn - Gia Định chính thức đổi tên thành TP. Hồ Chí Minh vào năm nào?", "options": ["A. 1975", "B. 1976", "C. 1977", "D. 1980"], "answer": "B. 1976"},
    {"question": "UNESCO ra NGHỊ QUYẾT vinh danh Chủ tịch Hồ Chí Minh vào năm nào?", "options": ["A. 1987", "B. 1990", "C. 1995", "D. 2000"], "answer": "A. 1987"}
]

PRIZE_TREE = [
    "15. 150.000.000 VNĐ", "14. 85.000.000 VNĐ", "13. 60.000.000 VNĐ",
    "12. 40.000.000 VNĐ", "11. 30.000.000 VNĐ", "10. 22.000.000 VNĐ (MỐC VÀNG)",
    "9. 14.000.000 VNĐ",  "8. 10.000.000 VNĐ",  "7. 6.000.000 VNĐ",
    "6. 3.000.000 VNĐ",   "5. 2.000.000 VNĐ (MỐC VÀNG)",  "4. 1.000.000 VNĐ",
    "3. 600.000 VNĐ",     "2. 400.000 VNĐ",     "1. 200.000 VNĐ"
]

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.lifelines = {"5050": True, "phone": True, "audience": True}
    st.session_state.disabled_options = []
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.hint_text = ""

def reset_game():
    st.session_state.current_q = 0
    st.session_state.lifelines = {"5050": True, "phone": True, "audience": True}
    st.session_state.disabled_options = []
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.hint_text = ""

st.markdown("<h1 class='main-title'>🌟 AI LÀ TRIỆU PHÚ 🌟</h1>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; color: #FFD700;'>Chủ đề: Tìm hiểu về Chủ tịch Hồ Chí Minh</p>", unsafe_allow_html=True)
st.divider()

col_left, col_right = st.columns([3, 1])

with col_right:
    st.subheader("🏆 Thang Tiền Thưởng")
    for idx, prize in enumerate(PRIZE_TREE):
        q_idx = 14 - idx
        if q_idx == st.session_state.current_q and not st.session_state.game_over:
            st.markdown(f"**👉 <span style='color:#FFD700;'>{prize}</span>**", unsafe_allow_html=True)
        elif q_idx in [4, 9, 14]:
            st.markdown(f"<span style='color:#00FF00;'>{prize}</span>", unsafe_allow_html=True)
        else:
            st.write(f"{prize}")

with col_left:
    if st.session_state.game_over:
        if st.session_state.won:
            st.balloons()
            st.success("🎉 CHÚC MỪNG BẠN ĐÃ TRỞ THÀNH TRIỆU PHÚ!")
        else:
            st.error(f"❌ Bạn đã trả lời sai ở câu hỏi số {st.session_state.current_q + 1}!")
        if st.button("🔄 Chơi lại", on_click=reset_game, type="primary"):
            st.rerun()
    else:
        q_data = QUESTIONS[st.session_state.current_q]
        
        st.write("### 🛟 Quyền Trợ Giúp:")
        col_h1, col_h2, col_h3 = st.columns(3)
        
        with col_h1:
            if st.button("⚖️ 50:50", disabled=not st.session_state.lifelines["5050"]):
                st.session_state.lifelines["5050"] = False
                wrong_ops = [op for op in q_data["options"] if op != q_data["answer"]]
                st.session_state.disabled_options = random.sample(wrong_ops, 2)
                st.rerun()

        with col_h2:
            if st.button("📞 Gọi người thân", disabled=not st.session_state.lifelines["phone"]):
                st.session_state.lifelines["phone"] = False
                st.session_state.hint_text = f"🤖 Người thân: 'Tôi nghĩ đáp án đúng là **{q_data['answer']}**!'"
                st.rerun()

        with col_h3:
            if st.button("👥 Hỏi khán giả", disabled=not st.session_state.lifelines["audience"]):
                st.session_state.lifelines["audience"] = False
                st.session_state.hint_text = f"📊 Khán giả chọn cao nhất: **{q_data['answer']}** (80%)"
                st.rerun()

        if st.session_state.hint_text:
            st.info(st.session_state.hint_text)

        st.divider()
        st.markdown(f"### Câu {st.session_state.current_q + 1}:")
        st.markdown(f"<div class='question-box'>{q_data['question']}</div>", unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        cols = [col_a, col_b, col_a, col_b]
        
        for idx, option in enumerate(q_data["options"]):
            is_disabled = option in st.session_state.disabled_options
            with cols[idx]:
                if st.button(option, key=f"btn_{idx}", disabled=is_disabled, use_container_width=True):
                    if option == q_data["answer"]:
                        st.toast("Chính xác! 👏", icon="✅")
                        st.session_state.disabled_options = []
                        st.session_state.hint_text = ""
                        if st.session_state.current_q == 14:
                            st.session_state.game_over = True
                            st.session_state.won = True
                        else:
                            st.session_state.current_q += 1
                        st.rerun()
                    else:
                        st.session_state.game_over = True
                        st.rerun()
