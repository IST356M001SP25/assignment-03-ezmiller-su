'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''

import streamlit as st
import json
import packaging

if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'file_count' not in st.session_state:
    st.session_state.file_count = 0
if 'line_count' not in st.session_state:
    st.session_state.line_count = 0

st.title("Process Package Files")
uploadedfile = st.file_uploader("Upload package file:")

if uploadedfile:
    file = uploadedfile.read().decode('utf-8')

    pkg = []
    line_count = 0

    for line in file.split('\n'):
        parsed = packaging.parse_packaging(line)
        pkg.append(parsed)
        unit = packaging.get_unit(parsed)
        total_units = packaging.calc_total_units(parsed)
        st.session_state.line_count += 1
        line_count += 1
    
    new_json_name = uploadedfile.name.split('.')[0]
    
    with open(f'data/{new_json_name}.json','w') as jsonfile:
        json.dump(pkg, jsonfile, indent=4)
        st.session_state.file_count += 1

    st.session_state.summaries.append(f"{line_count} packages written to {new_json_name}.json")

    for x in st.session_state.summaries:
        st.info(f"{x}", icon='💾')

    st.success(f"{st.session_state.file_count} files processed, {st.session_state.line_count} total lines processed", icon='✅')