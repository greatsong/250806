import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 상담", page_icon="🧑‍🏫")

st.title("🧠 MBTI로 알아보는 초등학생 진로 추천 💡")
st.markdown("MBTI 성격유형을 선택하면, 어울리는 진로와 그 이유를 알려줄게요! 👇")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🧩", mbti_types)

# 진로 추천 딕셔너리
career_recommendations = {
    "ISTJ": {
        "career": "👨‍⚖️ 판사, 👮 경찰, 🧑‍🏫 교사",
        "reason": "정확하고 책임감이 강한 ISTJ는 규칙을 잘 지키고 집중력이 좋아요. 질서를 중요하게 생각하니 정의로운 직업이 잘 어울려요!"
    },
    "ISFJ": {
        "career": "👩‍⚕️ 간호사, 👨‍🏫 초등 교사, 🐶 동물 보호사",
        "reason": "남을 돕는 걸 좋아하고 따뜻한 마음을 가진 ISFJ는 배려심이 커요. 사람과 동물을 돌보는 일이 딱이에요!"
    },
    "INFJ": {
        "career": "🧘 심리상담가, 📚 작가, 🌏 환경운동가",
        "reason": "마음이 깊고 남을 도우려는 INFJ는 세상을 더 나은 곳으로 만들고 싶어 해요. 혼자 조용히 고민하는 것도 잘해요!"
    },
    "INTJ": {
        "career": "🧠 과학자, 🖥️ 프로그래머, 🚀 우주 연구원",
        "reason": "계획적이고 똑똑한 INTJ는 새로운 아이디어를 생각해내는 데 뛰어나요. 혼자 집중해서 하는 일에 강해요!"
    },
    "ISTP": {
        "career": "🔧 기계공, 🚗 자동차 디자이너, 👨‍🔬 실험가",
        "reason": "손으로 만지고 고치는 걸 좋아하는 ISTP는 도구나 기계 다루는 걸 즐겨요. 호기심도 많고 침착해요!"
    },
    "ISFP": {
        "career": "🎨 화가, 🎵 음악가, 🐾 동물 케어 전문가",
        "reason": "조용하지만 감성이 풍부한 ISFP는 예술과 자연을 사랑해요. 자유롭게 표현할 수 있는 직업이 잘 맞아요!"
    },
    "INFP": {
        "career": "📖 동화작가, 🧚 캐릭터 디자이너, 💌 아동상담사",
        "reason": "상상력이 풍부하고 착한 마음을 가진 INFP는 이야기를 만들거나 친구를 위로하는 데 소질 있어요!"
    },
    "INTP": {
        "career": "🧪 연구원, 🧠 뇌과학자, 🎮 게임 개발자",
        "reason": "궁금한 게 많은 INTP는 ‘왜?’라는 질문을 자주 해요. 혼자 깊이 생각하며 새로운 걸 탐구하는 직업이 어울려요!"
    },
    "ESTP": {
        "career": "🎤 방송인, 🎮 게임 스트리머, 🏋️ 운동선수",
        "reason": "활동적이고 사교성이 좋은 ESTP는 에너지가 넘쳐요. 실전에서 활약하고 주목받는 걸 좋아하죠!"
    },
    "ESFP": {
        "career": "🎬 배우, 🕺 댄서, 🎤 엔터테이너",
        "reason": "즐거움을 추구하고 밝은 성격의 ESFP는 무대에서 빛나는 재능을 가졌어요. 사람들과 함께 노는 것도 잘해요!"
    },
    "ENFP": {
        "career": "🌍 여행가, 🗣️ 강연가, 💡 창의기획자",
        "reason": "열정이 넘치고 아이디어가 많은 ENFP는 남들과 다르게 생각하는 걸 좋아해요. 새로운 것에 도전하는 걸 두려워하지 않아요!"
    },
    "ENTP": {
        "career": "💬 토론가, 💻 스타트업 창업가, 🎥 유튜버",
        "reason": "재치 있고 말 잘하는 ENTP는 다양한 아이디어를 실현하는 걸 좋아해요. 사람들과 이야기하며 배우는 걸 즐겨요!"
    },
    "ESTJ": {
        "career": "🏢 공무원, 🧑‍💼 경영자, 👨‍🏫 교장 선생님",
        "reason": "리더십 있고 현실적인 ESTJ는 사람들을 잘 이끌어요. 조직을 정리하고 관리하는 걸 잘하죠!"
    },
    "ESFJ": {
        "career": "👩‍🍳 요리사, 🧑‍🏫 선생님, 👩‍💻 비서",
        "reason": "사람들을 잘 챙기고 정이 많은 ESFJ는 함께하는 걸 좋아해요. 섬세하고 따뜻한 직업이 잘 맞아요!"
    },
    "ENFJ": {
        "career": "🎓 교육자, 🧑‍🤝‍🧑 NGO 활동가, 🎙️ 아나운서",
        "reason": "타인을 돕고 감동을 주는 ENFJ는 리더십이 뛰어나요. 팀워크가 필요한 일에서 빛나요!"
    },
    "ENTJ": {
        "career": "🚀 CEO, 📈 기획자, 🧑‍💼 비즈니스 리더",
        "reason": "야망이 크고 추진력이 있는 ENTJ는 큰 목표를 향해 달리는 걸 좋아해요. 문제 해결 능력도 뛰어나요!"
    }
}

if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 유형 추천 진로")
    st.markdown(f"**추천 직업:** {career_recommendations[selected_mbti]['career']}")
    st.markdown(f"**추천 이유:** {career_recommendations[selected_mbti]['reason']}")

    st.success("진로는 앞으로 계속 바뀔 수도 있어요! 다양한 경험을 통해 자신을 알아가는 게 제일 중요하답니다! 😊")
