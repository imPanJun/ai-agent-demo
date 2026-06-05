import streamlit as st

st.set_page_config(page_title="AI 總協調官 Demo", layout="wide")

st.title("🚀 AI 總協調官 (Prompt Coach Agent)")
st.markdown("---")

# 使用者輸入
task = st.radio("1. 您的任務是？", ["做簡報", "寫企劃", "查資料"])
tone = st.radio("2. 您的語氣風格？", ["自然口語", "專業嚴肅"])
keyword = st.text_input("3. 請輸入關鍵字：", "新進員工培訓")

# 啟動按鈕
if st.button("開始執行 AI 代理", type="primary"):
    missing_info = []

    # 簡單檢查缺失
    if task == "做簡報" and "簡報" not in keyword:
        missing_info.append("請問簡報需要幾頁？")

    if task == "寫企劃" and "企劃" not in keyword:
        missing_info.append("企劃的對象是誰？")

    if task == "查資料" and len(keyword) < 5:
        missing_info.append("請提供更具體的查詢主題。")

    # 如果有缺失 → 反問使用者
    if missing_info:
        st.warning("⚠️ 需要更多資訊：")
        for q in missing_info:
            st.write("👉 " + q)
    else:
        # 如果資訊完整 → 生成 Prompt
        prompt_text = f"""
Act as an AI assistant.
Task: {task}
Tone: {tone}
Topic: {keyword}

Please provide a structured output that matches the task type.
"""
        st.success("🎉 資訊完整，已生成 Prompt！")
        st.code(prompt_text, language="markdown")
