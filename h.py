import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import time

# 페이지 설정
st.set_page_config(
    page_title="배민식의 자기소개",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    
    .gradient-text {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: bold;
    }
    
    .slide-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 1rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .skill-badge {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    
    .timeline-item {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .metric-card {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        padding: 1rem;
        border-radius: 1rem;
        text-align: center;
        color: white;
        margin: 0.5rem;
    }
    
    .contact-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin: 1rem 0;
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0
if 'auto_play' not in st.session_state:
    st.session_state.auto_play = False

# 슬라이드 목록
slides = [
    "🔥 안녕하세요!",
    "🌱 성장 배경",
    "📚 학업 경험",
    "🏆 활동 및 수상",
    "💼 프로젝트 경험",
    "🛠️ 기술 및 역량",
    "🚀 미래 비전",
    "📞 마무리 & 연락처"
]

# 사이드바 네비게이션
with st.sidebar:
    st.markdown("### 📋 슬라이드 목록")

    # 슬라이드 선택
    selected_slide = st.selectbox(
        "슬라이드 선택:",
        range(len(slides)),
        format_func=lambda x: slides[x],
        index=st.session_state.current_slide
    )

    if selected_slide != st.session_state.current_slide:
        st.session_state.current_slide = selected_slide

    st.markdown("---")

    # 네비게이션 버튼
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 이전", disabled=st.session_state.current_slide == 0):
            st.session_state.current_slide = max(0, st.session_state.current_slide - 1)
            st.rerun()  # Changed from st.experimental_rerun()

    with col2:
        if st.button("다음 ➡️", disabled=st.session_state.current_slide == len(slides) - 1):
            st.session_state.current_slide = min(len(slides) - 1, st.session_state.current_slide + 1)
            st.rerun()  # Changed from st.experimental_rerun()

    # 자동 재생
    auto_play = st.checkbox("🎬 자동재생 (5초)", value=st.session_state.auto_play)
    st.session_state.auto_play = auto_play

    # 진행률
    progress = (st.session_state.current_slide + 1) / len(slides)
    st.progress(progress)
    st.write(f"진행률: {progress*100:.1f}%")

# 메인 헤더
st.markdown("""
<div class="main-header">
    <h1>🔥 배민식의 자기소개 프레젠테이션</h1>
    <p>재난안전소방학과 | 건양대학교</p>
</div>
""", unsafe_allow_html=True)

# 현재 슬라이드 표시
current_slide = st.session_state.current_slide

# 슬라이드 1: 안녕하세요
if current_slide == 0:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("## 👋 안녕하세요!")
        st.markdown('<h2 class="gradient-text">배민식입니다! 🔥</h2>', unsafe_allow_html=True)
        st.markdown("""
        **재난안전소방학**을 전공하며   
        **안전한 사회를 만들어가는 전문가**로 성장하고 있습니다.
        
        오늘 저의 특별한 이야기를 들려드리겠습니다! ✨
        """)

    # 메트릭 카드들
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🔥 열정", "100%", "최고 수준")
    with col2:
        st.metric("🎓 전문성", "85%", "지속 성장")
    with col3:
        st.metric("🤝 협업", "90%", "팀워크 중시")
    with col4:
        st.metric("💪 책임감", "95%", "신뢰성 확보")

    st.markdown('</div>', unsafe_allow_html=True)

# 슬라이드 2: 성장 배경
elif current_slide == 1:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("## 🌱 성장 배경")

    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown("### 🏠 가족과의 협력 경험")
    st.write("다양한 활동을 통해 협력의 중요성과 팀워크를 배웠습니다.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown("### 💪 끈기와 도전정신")
    st.write("어려운 상황에서도 포기하지 않는 강인한 정신력을 기를 수 있었습니다.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown("### ❤️ 봉사정신의 발견")
    st.write("남을 돕는 일에서 큰 보람을 느끼며 소방 분야에 관심을 갖게 되었습니다.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 스킬 배지들
    st.markdown("### 💫 핵심 가치")
    badges = ["협력", "끈기", "도전정신", "봉사정신", "리더십"]
    badge_html = "".join([f'<span class="skill-badge">{badge}</span>' for badge in badges])
    st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 슬라이드 3: 학업 경험
elif current_slide == 2:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("## 📚 학업 경험")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 건양대학교 재난안전소방학과")
        st.metric("📊 학업 성취도", "3.8/4.5", "전공 평점")

    # 전공 과목별 성적 차트
    subjects = ['소방학개론', '재난관리론', '건축소방설비', '화재조사', '위험물관리']
    grades = [4.0, 3.8, 4.2, 3.9, 4.1]

    fig = px.bar(
        x=subjects,
        y=grades,
        title="📈 전공 과목별 성적",
        color=grades,
        color_continuous_scale="viridis"
    )
    fig.update_layout(
        xaxis_title="과목",
        yaxis_title="성적",
        yaxis=dict(range=[0, 4.5])
    )
    st.plotly_chart(fig, use_container_width=True)

    # 학습 영역
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### 📖 핵심 전공 과목")
        st.write("소방학 개론, 재난관리론, 건축소방설비 등 체계적 학습")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### 🧪 실습 경험")
        st.write("소방서 현장실습, 재난대응 시뮬레이션을 통한 실무 역량 강화")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### 🔬 연구 활동")
        st.write("화재 예방 시스템 개선 방안 연구 프로젝트 참여")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 슬라이드 4: 활동 및 수상
elif current_slide == 3:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("## 🏆 활동 및 수상")

    # 주요 활동 메트릭
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 봉사활동", "100+시간", "지역 소방서 안전교육")
    with col2:
        st.metric("👥 리더십", "회장 역임", "응급처치 동아리")

    # 수상 내역
    st.markdown("### 🏅 주요 수상 내역")

    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown("### 🥈 전국 대학생 소방안전 아이디어 공모전")
    st.write("**우수상 수상** - 혁신적인 안전 아이디어로 인정받음")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown("### 🥇 교내 안전캠페인 기획 대회")
    st.write("**최우수상 수상** - 창의적인 캠페인 기획으로 1등 달성")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown("### 📜 보유 자격증")
    st.write("응급처치 강사 자격증, 소방설비기사 필기 합격")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 슬라이드 5: 프로젝트 경험
elif current_slide == 4:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("## 💼 프로젝트 경험")

    # 주요 프로젝트
    st.markdown("### 🔥 화재 예방 시설 점검 시스템 개발")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👨‍💼 역할", "팀장", "")
    with col2:
        st.metric("👥 팀원", "5명", "")
    with col3:
        st.metric("⚙️ 기술", "IoT 센서", "")
    with col4:
        st.metric("🤝 협력기관", "지역 소방서", "")

    st.info("💡 실시간 모니터링 시스템 구축으로 실제 적용 가능성까지 검증 완료!")

    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown("### 🗺️ 대학 내 안전지도 제작")
    st.write("캠퍼스 위험 요소 분석 및 학생 안전 가이드라인 제작")
    st.caption("학생들의 안전한 캠퍼스 생활을 위한 실용적 프로젝트")
    st.markdown('</div>', unsafe_allow_html=True)

    # 프로젝트 스킬
    st.markdown("### 🎯 프로젝트를 통해 습득한 역량")
    skills = ["팀 리더십", "IoT 기술", "데이터 분석", "협업", "문제해결"]
    skill_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
    st.markdown(skill_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 슬라이드 6: 기술 및 역량
elif current_slide == 5:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("## 🛠️ 기술 및 역량")

    # 기술 카테고리
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🚑 전문 기술")
        tech_skills = ["응급처치", "심폐소생술", "소방설비관리", "재난대응"]
        for skill in tech_skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 💻 IT 활용")
        it_skills = ["Python", "AutoCAD", "데이터분석", "안전관리SW"]
        for skill in it_skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

    with col3:
        st.markdown("### 🤝 소프트 스킬")
        soft_skills = ["위기대처", "팀워크", "리더십", "커뮤니케이션"]
        for skill in soft_skills:
            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

    # 레이더 차트
    st.markdown("### 📊 핵심 역량 레이더 차트")

    categories = ['응급처치', '소방설비', 'Python', '리더십', '팀워크']
    values = [95, 85, 75, 90, 95]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='스킬 레벨',
        line_color='rgba(102, 126, 234, 1)',
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="핵심 역량 분석"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 슬라이드 7: 미래 비전
elif current_slide == 6:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("## 🚀 미래 비전")

    st.markdown('<h2 class="gradient-text">"안전한 세상을 만드는 전문가"</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### 🎯 단기 목표 (1-2년)")
        st.markdown("""
        - ✅ 소방설비기사 자격증 취득
        - 📈 현장 실무 경험 쌓기   
        - 📚 전문 지식 심화 학습
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### ⭐ 장기 목표 (5-10년)")
        st.markdown("""
        - 🔥 재난안전 분야 전문가
        - 🏢 안전한 사회 구축 기여
        - 👨‍🏫 후배 교육 및 멘토링
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # 사회적 기여 계획
    st.markdown("### 🌍 사회적 기여 계획")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("#### 📢 안전문화 확산")
        st.write("지역사회 안전 의식 향상")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("#### ⚙️ 시스템 개선")
        st.write("재난 예방 기술 발전")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("#### 📖 교육 프로그램")
        st.write("체계적 안전 교육 개발")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# 슬라이드 8: 마무리 & 연락처
elif current_slide == 7:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("## 🎁 마무리 & 연락처")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<h1 class="gradient-text">"안전한 세상을 만드는 것이 저의 사명입니다"</h1>', unsafe_allow_html=True)

        st.info("""
        지금까지 쌓아온 **경험과 지식**을 바탕으로   
        더 나은 미래를 만들어가겠습니다. ⭐
        
        함께 성장할 수 있는 기회를 주신다면   
        **최선을 다해 기여**하겠습니다!
        """)

    # 연락처 정보
    st.markdown("### 📞 연락처 정보")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.markdown("#### 📧 이메일")
        st.write("baeminsick@naver.com")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.markdown("#### 📱 연락처")
        st.write("010-3904-1745")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.markdown("#### 🏫 소속")
        st.write("건양대학교   \n재난안전소방학과")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🙏✨ 감사합니다!")

    st.markdown('</div>', unsafe_allow_html=True)

# 자동 재생 기능
if st.session_state.auto_play and st.session_state.current_slide < len(slides) - 1:
    time.sleep(5)
    st.session_state.current_slide += 1
    st.rerun() # This is the line that was causing the error and has now been fixed!
elif st.session_state.auto_play and st.session_state.current_slide == len(slides) - 1:
    st.session_state.auto_play = False

# 하단 정보
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### 🔥 배민식의 자기소개 프레젠테이션")
    st.caption("Streamlit으로 제작된 대화형 프레젠테이션")