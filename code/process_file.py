'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''

import streamlit as st
import json
import packaging

pkg = []

uploadedfile = st.file_uploader("Upload package file:")
file = uploadedfile.read().decode('utf-8')

pkg_count = 0

for line in file.split('\n'):
    parsed = packaging.parse_packaging(line)
    pkg.append(parsed)
    unit = packaging.get_unit(parsed)
    total_units = packaging.calc_total_units(parsed)
    pkg_count += 1
    st.info(f"{line} ➡️ Total 📦 Size: {total_units} {unit}")

new_json_name = uploadedfile.name.split('.')[0]

with open(f'data/{new_json_name}.json','w') as jsonfile:
    json.dump(pkg, jsonfile, indent=4)
    st.success(f"💾 {pkg_count} packages written to {new_json_name}.json")