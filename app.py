import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="Kerala Utility Hub", page_icon="🌴", layout="centered")

st.title("🌴 Kerala Daily Utility Hub")
st.caption("മലയാളികൾക്കായുള്ള ദൈനംദിന കാൽക്കുലേറ്ററുകളും ടൂളുകളും")

tab1, tab2, tab3 = st.tabs(["📐 ഭൂമി അളവ്", "🪙 സ്വർണ്ണം & GST", "🔊 മലയാളം Voice"])

with tab1:
    st.subheader("ഭൂമി അളവ് കൺവെർട്ടർ")
    cents = st.number_input("സെന്റ് (Cents) നൽകുക:", min_value=0.0, value=10.0, step=0.5)
    sqft = cents * 435.6
    acres = cents / 100.0
    st.success(f"**{cents} സെന്റ് =**")
    st.write(f"- 📏 **{sqft:,.2f}** ചതുരശ്ര അടി (Sq. Ft)")
    st.write(f"- 🌾 **{acres:.3f}** ഏക്കർ (Acres)")

with tab2:
    st.subheader("സ്വർണ്ണവില & പണിക്കൂലി കാൽക്കുലേറ്റർ")
    pavan_rate = st.number_input("ഒരു പവൻ സ്വർണ്ണവില (₹):", min_value=0.0, value=58000.0, step=100.0)
    grams = st.number_input("ആവശ്യമായ ഗ്രാം:", min_value=0.0, value=8.0, step=0.5)
    making_percent = st.number_input("പണിക്കൂലി (%):", min_value=0.0, value=5.0, step=0.5)
    
    gram_rate = pavan_rate / 8.0
    gold_cost = gram_rate * grams
    making_charge = gold_cost * (making_percent / 100.0)
    subtotal = gold_cost + making_charge
    gst = subtotal * 0.03
    total_cost = subtotal + gst
    
    st.info(f"**ആകെ തുക: ₹ {total_cost:,.2f}**")
    st.write(f"- സ്വർണ്ണവില: ₹ {gold_cost:,.2f}")
    st.write(f"- പണിക്കൂലി ({making_percent}%): ₹ {making_charge:,.2f}")
    st.write(f"- GST (3%): ₹ {gst:,.2f}")

with tab3:
    st.subheader("മലയാളം Voice Player")
    user_text = st.text_area("മലയാളത്തിൽ എന്തെങ്കിലും ടൈപ്പ് ചെയ്യുക:", "നമസ്കാരം, സുഖമാണോ?")
    if st.button("ശബ്ദം കേൾക്കുക 🔊"):
        if user_text.strip():
            with st.spinner("ശബ്ദം തയ്യാറാക്കുന്നു..."):
                tts = gTTS(text=user_text, lang='ml')
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                st.audio(fp, format="audio/mp3")
        else:
            st.warning("ദയവായി എന്തെങ്കിലും എഴുതുക.")
