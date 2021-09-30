#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:05:46 2020

@author: qiuhouyuan
"""
import streamlit as st
 
 
st.write('你好，世界')

if __name__ == "__main__":
    st.markdown('# streamDemo')
    st.markdown('---')
    sidebar = st.sidebar
    alo_type = sidebar.selectbox("可视化算法",('pca', 'tsne', 'lle'))
    data_type = sidebar.selectbox("数据集", ('iris', 'digits'))
    data, label = load_data(data_type)
    st.dataframe(data)
    st.markdown('---')
    if sidebar.button('run'):
        df = process(alo_type, data, label)
        vega_scatter(df)