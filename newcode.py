import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from pathlib import Path
import os
st.title('Ecaps Reconciliation')
option=st.selectbox('Please Select Recon Name',('RazorpayX','Bankit','Paytm',"AEPS"))
if option=='RazorpayX':
    uploaded_razorpay_file = st.file_uploader("Upload razorpay Files ",type=['xlsx'])
    uploaded_ecaps_file = st.file_uploader("Upload ecaps Files",type=['xlsx'])
    if uploaded_razorpay_file is None:

        #file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write('No file selected,please select files')
    df1=pd.read_excel(uploaded_razorpay_file)
    df2=pd.read_excel(uploaded_ecaps_file)
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
    df11=pd.DataFrame(result)
    st.write('Your Result is below',d11.T)
elif option=='Bankit':
    uploaded_razorpay_file = st.file_uploader("Upload Bankit file ",type=['xlsx'])
    uploaded_ecaps_file = st.file_uploader("Upload ecaps Files",type=['xlsx'])
    if uploaded_razorpay_file is None:

        #file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write('No file selected,please select files')
    df3=pd.read_excel(uploaded_razorpay_file)
    df4=pd.read_excel(uploaded_ecaps_file)
    df5=df3[(df3['Particulars']=='DMR-AREMIT')  & (df3['Transaction Status'] == "Success")]
    
    df6= df4[(df4['Status']=='SUCCESS') & (df4['ProdName']=='IMPS')]
    
    A=df5['Txn. Amount'].sum()
    B=df5['Txn. Amount'].count()
    C=df6['Amount'].sum()
    D=df6['Amount'].count()
    dic2={'No of txns success as per Ecaps':D,'No of Sucess txns as per Bankit':B,'Sum of txns amount as per Ecaps':A,'Sum of txns as per bankit':C,
     'Difference': D-B}
    df22=pd.DataFrame(dic2,index=['Value'])
    st.write('Your Result is below',df22.T)
elif option=='AEPS':
    uploaded_razorpay_file = st.file_uploader("Upload AEPS file ",type=['xlsx'])
    uploaded_ecaps_file = st.file_uploader("Upload ecaps Files 1st",type=['xlsx'])
    uploaded_ecaps_file2 = st.file_uploader("Upload ecaps file 2nd ",type=['xlsx'])
    if uploaded_razorpay_file is None:

        #file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write('No file selected,please select files')
    df7=pd.read_excel(uploaded_razorpay_file)
    df8=pd.read_excel(uploaded_ecaps_file)
    df9=pd.read_excel(uploaded_ecaps_file2)
    df_merged=pd.concat([df8, df9],axis=0,
    join="outer",
    ignore_index=False,
    keys=None,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)
    #print(df_ecaps)
    df77= df7[(df7['Service'] == "Cash Withdrawl") & (df7['Transaction Status'] == "Success")] 
    P=df77[ 'Txn. Amount'].sum()
    Q=df77[ 'Txn. Amount'].count()
    df88=df_merged[df_merged['ProductMajor']=='AEPS']
    R=df88['RechargeAmount'].sum()
    S=df88['RechargeAmount'].count() 
    dic3={'No of txns success as per AEPS':Q,'No of Sucess txns as per Ecaps':S,'Sum of txns amount as per AEPS':P,'Sum of txns as per Ecaps':R,
     'Difference': Q-S}
    df44=pd.DataFrame(dic3,index=['Value'])
    st.write('Your Result is below',df44.T) 
    

    


    
