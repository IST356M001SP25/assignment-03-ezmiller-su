'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''

import streamlit as st
import packaging

st.title('Process One Package')
packagingtxt = st.text_input('Enter package data:') # 12 eggs in 1 carton / 3 cartons in 1 box
if packagingtxt:
    parsed = packaging.parse_packaging(packagingtxt)
    unit = packaging.get_unit(parsed)
    total_units = packaging.calc_total_units(parsed)
    st.text(parsed)
    for x in parsed:
        item = list(x.keys())[0]
        quantity = list(x.values())[0]
        st.info(f"{item} ➡️ {quantity}")
    st.success(f"Total 📦 Size: {total_units} {unit}")