import streamlit as st
from datetime import date
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Kerala Viral Utilities", page_icon="🌴", layout="centered")

st.title("🌴 Kerala Super 4-in-1 Hub")
st.caption("മലയാളികൾക്കായി ഏറ്റവും കൂടുതൽ ആവശ്യമുള്ള 4 കാര്യങ്ങൾ ഒരൊറ്റ ആപ്പിൽ!")

tab1, tab2, tab3, tab4 = st.tabs([
    "🍚 1. റേഷൻ കാൽക്കുലേറ്റർ", 
    "🚌 2. KSRTC മിന്നൽ & സ്വിഫ്റ്റ്", 
    "🎭 3. മീം മേക്കർ", 
    "🎯 4. PSC & സർവീസ് പ്രായം"
])

# ----------------- 1. റേഷൻ കാൽക്കുലേറ്റർ -----------------
with tab1:
    st.subheader("🍚 പച്ചരിയും മണ്ണെണ്ണയും (റേഷൻ വിഹിതം)")
    st.write("നിങ്ങളുടെ കാർഡിലെ ആളുകളുടെ എണ്ണം അനുസരിച്ച് ഈ മാസം എന്ത് കിട്ടും എന്ന് നോക്കൂ:")
    
    card_type = st.selectbox("റേഷൻ കാർഡിന്റെ നിറം:", [
        "മഞ്ഞ കാർഡ് (AAY - അന്ത്യോദയ അന്നയോജന)", 
        "പിങ്ക് കാർഡ് (PHH - മുൻഗണനാ വിഭാഗം)", 
        "നീല കാർഡ് (NPS - സബ്സിഡി വിഭാഗം)", 
        "വെള്ള കാർഡ് (NPNS - പൊതുവിഭാഗം)"
    ])
    members = st.number_input("കാർഡിലെ അംഗങ്ങളുടെ എണ്ണം:", min_value=1, max_value=25, value=4, step=1)
    
    st.markdown("---")
    st.write("### 🛒 നിങ്ങൾക്ക് അർഹതപ്പെട്ട റേഷൻ വിഹിതം:")
    
    if "മഞ്ഞ" in card_type:
        st.success("✨ **മഞ്ഞ കാർഡ് വിഹിതം (സൗജന്യം):**")
        st.write("- 🌾 അരി: **30 കിലോഗ്രാം** (പൂർണ്ണമായും സൗജന്യം)")
        st.write("- 🌾 ഗോതമ്പ്: **5 കിലോഗ്രാം** (സൗജന്യം)")
        st.write("- 🪔 മണ്ണെണ്ണ: **1 ലിറ്റർ** (സർക്കാർ സബ്സിഡി നിരക്കിൽ)")
    elif "പിങ്ക്" in card_type:
        st.info("✨ **പിങ്ക് കാർഡ് വിഹിതം (ഒരംഗത്തിന് 5 കിലോ വീതം സൗജന്യം):**")
        rice = members * 4
        wheat = members * 1
        st.write(f"- 🌾 അരി: **{rice} കിലോഗ്രാം** (സൗജന്യം)")
        st.write(f"- 🌾 ആട്ട / ഗോതമ്പ്: **{wheat} കിലോഗ്രാം** (സൗജന്യം)")
        st.write("- 🪔 മണ്ണെണ്ണ: **0.5 ലിറ്റർ**")
    elif "നീല" in card_type:
        st.warning("✨ **നീല കാർഡ് വിഹിതം (സബ്സിഡി നിരക്കിൽ):**")
        rice = members * 2
        st.write(f"- 🌾 അരി: **{rice} കിലോഗ്രാം** (കിലോയ്ക്ക് ₹4 നിരക്കിൽ)")
        st.write("- 🌾 ആട്ട: **2 പാക്കറ്റ്** (ലഭ്യതയനുസരിച്ച് സബ്സിഡി നിരക്കിൽ)")
        st.write("- 🪔 മണ്ണെണ്ണ: **0.5 ലിറ്റർ** (ലഭ്യതയനുസരിച്ച്)")
    else:
        st.write("✨ **വെള്ള കാർഡ് വിഹിതം (നോൺ സബ്സിഡി):**")
        st.write("- 🌾 അരി: കാർഡിന് **10 കിലോഗ്രാം** വരെ (സ്റ്റോക്ക് അനുസരിച്ച്, കിലോയ്ക്ക് ₹10.90)")
        st.write("- 🌾 ആട്ട: **2 പാക്കറ്റ്** (ലഭ്യതയനുസരിച്ച്)")

# ----------------- 2. KSRTC മിന്നൽ & സ്വിഫ്റ്റ് -----------------
with tab2:
    st.subheader("🚌 KSRTC യാത്രാ കാൽക്കുലേറ്റർ")
    st.write("പ്രധാന റൂട്ടുകളിലെ മിന്നൽ, സൂപ്പർഫാസ്റ്റ്, സ്വിഫ്റ്റ് നിരക്കും സമയവും:")
    
    routes = {
        "തിരുവനന്തപുരം ↔ എറണാകുളം": {"distance": 210, "minnal_fare": 360, "sf_fare": 250, "time": "4.5 മണിക്കൂർ"},
        "എറണാകുളം ↔ കോഴിക്കോട്": {"distance": 180, "minnal_fare": 320, "sf_fare": 220, "time": "4.0 മണിക്കൂർ"},
        "തിരുവനന്തപുരം ↔ കോഴിക്കോട്": {"distance": 390, "minnal_fare": 650, "sf_fare": 460, "time": "8.5 മണിക്കൂർ"},
        "കോഴിക്കോട് ↔ കണ്ണൂർ": {"distance": 90, "minnal_fare": 180, "sf_fare": 120, "time": "2.0 മണിക്കൂർ"},
        "പാലക്കാട് ↔ എറണാകുളം": {"distance": 135, "minnal_fare": 240, "sf_fare": 170, "time": "3.0 മണിക്കൂർ"}
    }
    
    selected_route = st.selectbox("റൂട്ട് തിരഞ്ഞെടുക്കുക:", list(routes.keys()))
    info = routes[selected_route]
    
    st.markdown("---")
    st.write(f"📍 **ദൂരം:** ഏകദേശം {info['distance']} കി.മീ | ⏱️ **യാത്രാസമയം:** {info['time']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("⚡ **മിന്നൽ / സ്വിഫ്റ്റ് ഡീലക്സ്**")
        st.write(f"ടിക്കറ്റ് നിരക്ക്: **₹ {info['minnal_fare']}**")
        st.caption("പരിമിതമായ സ്റ്റോപ്പുകൾ, വേഗതയേറിയ യാത്ര")
    with col2:
        st.success("🚍 **സൂപ്പർ ഫാസ്റ്റ് (SF)**")
        st.write(f"ടിക്കറ്റ് നിരക്ക്: **₹ {info['sf_fare']}**")
        st.caption("എല്ലാ പ്രധാന ടൗണുകളിലും സ്റ്റോപ്പ്")

# ----------------- 3. മീം മേക്കർ -----------------
with tab3:
    st.subheader("🎭 മലയാളം മീം ജനറേറ്റർ")
    st.write("നിങ്ങളുടെ ഫേസ്ബുക്ക്/റെഡ്ഡിറ്റ് പോസ്റ്റുകൾക്കായി മീം ഉണ്ടാക്കൂ:")
    
    char_style = st.selectbox("മീം പശ്ചാത്തലം:", [
        "സലിം കുമാർ (മണവാളൻ എക്സ്പ്രഷൻ)",
        "ജഗതി (ദാസൻ & വിജയൻ സ്റ്റൈൽ)",
        "ഇന്നസെന്റ് (കിളിച്ചുണ്ടൻ സ്റ്റൈൽ)",
        "ഹരിശ്രീ അശോകൻ (രമണൻ ഡയലോഗ്)"
    ])
    
    top_text = st.text_input("മുകളിലെ വാചകം (സാഹചര്യം):", "ഞാൻ ജോലി കഴിഞ്ഞു വീട്ടിലെത്തുമ്പോൾ...")
    bottom_text = st.text_input("താഴത്തെ വാചകം (പഞ്ച് ഡയലോഗ്):", "എന്നെക്കണ്ടതും അമ്മ: 'ആ ചോറ് തിന്ന് പാത്രം കഴുകി വെക്ക്'")
    
    if st.button("മീം തയ്യാറാക്കുക 🎨"):
        # Create image card
        img = Image.new('RGB', (600, 320), color=(30, 41, 59))
        draw = ImageDraw.Draw(img)
        
        # Border
        draw.rectangle([10, 10, 590, 310], outline=(56, 189, 248), width=3)
        
        # Draw texts
        draw.text((30, 40), f"[{char_style}]", fill=(250, 204, 21))
        draw.text((30, 100), top_text, fill=(255, 255, 255))
        draw.text((30, 190), bottom_text, fill=(56, 189, 248))
        draw.text((30, 260), "🌴 Created via Kerala Viral Hub", fill=(148, 163, 184))
        
        st.image(img, caption="നിങ്ങളുടെ മീം റെഡി!")
        
        # Download button
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(label="മീം ഡൗൺലോഡ് ചെയ്യുക 📥", data=byte_im, file_name="kerala_meme.png", mime="image/png")

# ----------------- 4. PSC & സർവീസ് പ്രായം -----------------
with tab4:
    st.subheader("🎯 PSC പ്രായപരിധി & സർവീസ് ടൂൾ")
    dob = st.date_input("നിങ്ങളുടെ ജനനത്തീയതി (Date of Birth):", min_value=date(1965, 1, 1), max_value=date.today())
    today = date.today()
    
    years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.info(f"📅 **ഇന്നത്തെ നിങ്ങളുടെ പ്രായം: {years} വയസ്സ്**")
    
    st.write("#### 📋 PSC അർഹത പരിശോധന:")
    cat = st.selectbox("വിഭാഗം / സംവരണം:", [
        "ജനറൽ (General - 36 വയസ്സ്)", 
        "ഒ.ബി.സി (OBC - 39 വയസ്സ്)", 
        "എസ്.സി / എസ്.ടി (SC/ST - 41 വയസ്സ്)",
        "വിമുക്തഭടന്മാർ / ഭിന്നശേഷി (46 വയസ്സ്)"
    ])
    
    limit = 36 if "ജനറൽ" in cat else (39 if "ഒ.ബി.സി" in cat else (41 if "എസ്.സി" in cat else 46))
    
    if years <= limit:
        st.success(f"✅ നിങ്ങൾക്ക് പരീക്ഷയ്ക്ക് അപേക്ഷിക്കാം! പരമാവധി പ്രായം: {limit} വയസ്സ്.")
    else:
        st.error(f"❌ പ്രായപരിധി ({limit} വയസ്സ്) കഴിഞ്ഞിരിക്കുന്നു.")
        
    st.markdown("---")
    st.write("#### ⏳ പെൻഷൻ റിട്ടയർമെന്റ് കൗണ്ടർ (56 വയസ്സ്):")
    retirement_years = 56 - years
    if retirement_years > 0:
        st.write(f"സർക്കാർ സർവീസിൽ വിരമിക്കാൻ ഇനിയുള്ളത് ഏകദേശം: **{retirement_years} വർഷം**")
    else:
        st.write("വിരമിക്കൽ പ്രായപരിധി (56 വയസ്സ്) പിന്നിട്ടിരിക്കുന്നു.")
