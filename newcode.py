import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from pathlib import Path
import os
st.title('Ecaps Reconciliation')
uploaded_razorpay_file = st.file_uploader("Upload razorpay Files ",type=['xlsx'])
uploaded_ecaps_file = st.file_uploader("Upload ecaps Files",type=['xlsx'])
# if uploaded_file is not None:
#     file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#     st.write(file_details)
df1=pd.read_excel(uploaded_razorpay_file,engine='openpyxl')
df2=pd.read_excel(uploaded_ecaps_file,engine='openpyxl')
A=df1['SettlementAmount'].count()
B=df2['amount'].count()
C=df2['amount'].sum()
D =df1['SettlementAmount'].sum()
result=[] 
if A==B and C==D:

    
    dic={'No of txns as per razorpayX':A,'No_of txn as per Ecaps':B,'Total Amount as per RazorpayX ' :C,'Total Amount as Ecaps': D
          ,'Summary':'matched'}
    result.append(dic)
else:
    dic1={'No of txns as per razorpayX':A,'No_of txn as per Ecaps':B,'Total Amount as per RazorpayX ' :C,'Total Amount as Ecaps': D
         ,'Summary':'Not matched'}
    result.append(dic1)
    print(result)
df3=pd.DataFrame(result)
st.write('Your Result is below',df3.T)



