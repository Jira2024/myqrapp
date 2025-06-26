import streamlit as st
import qrcode
from datetime import datetime

st.title('QR Code Generator')

# Input field for URL or text
# if 'input_data' not in st.session_state:
#     st.session_state.input_data = ''
#     st.session_state.focus_input = True
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False
if 'qr_generated' not in st.session_state:
    st.session_state.qr_generated = False


input_key = "input_data_cleared" if st.session_state.clear_input else "input_data"
data = st.text_input(
    'Enter URL or text', key=input_key)

# Generate QR code
if st.button('Generate QR Code'):
    if data:
        img = qrcode.make(data)
        img_path = f'qrcodeimg/qr_{datetime.now().strftime("%Y%m%d%H%M%S")}{data}.png'

        img.save(img_path)
        st.image(img_path, width=300)
        st.success('QR code generated successfully')

        st.session_state.clear_input = ''
        st.session_state.focus_input = True
    else:
        st.warning('Please enter some data to generate a QR code.')


# Set focus back to the input field
if st.session_state.clear_input:
    st.session_state.focus_input = True
# if st.session_state.focus_input:
#     st.write(f"""<script>
#              document.querySelector('input[type="text"]').focus();
#              </script>""",
#              unsafe_allow_html=True
#              )
#     st.session_state.focus_input = False
