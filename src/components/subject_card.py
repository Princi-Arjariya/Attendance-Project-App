import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""<div style="
        background: white;
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    ">
        <h3 style="margin: 0; color: #1e293b; font-size: 1.3rem;">{name}</h3>
        <p style="margin: 10px 0; color: #64748b;">
            Code: 
            <span style="background: #E0E3FF; color: #5865F2; padding: 2px 8px; border-radius: 5px;">
                {code}
            </span> 
            | Section: {section}
        </p>"""

    if stats:
        html += '<div style="display: flex; gap: 8px; flex-wrap: wrap;">'
        for icon, label, value in stats:
            html += f"""
            <div style="background: #EB459E10; padding: 5px 12px; border-radius: 12px; font-size: 0.9rem;">
                {icon} <b>{value}</b> {label}
            </div>"""
        html += "</div>"

    html += "</div>"

    # HTML Render karne ke liye
    st.markdown(html, unsafe_allow_html=True)

    # Agar koi Streamlit button ya action callback hai
    if footer_callback:
        footer_callback()