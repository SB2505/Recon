import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from pathlib import Path
import os 
#img = Image.open(r"C:\Users\shahw\Downloads\Ecaps Final Logo corrected-01.png")
#st.sidebar.image(img, height=100,width=300) 
st.title('Ecaps Reconcilaition')
option=st.selectbox('Please Select Recon Name',('RazorpayX','Bankit','Paytm',"AEPS"))
if option=='RazorpayX':
    home = str(Path.home())
    path = home + "/Desktop/"
    

    

    def file_selector(folder_path=path):

        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Please upload a vendor file', filenames)
        return os.path.join(folder_path, selected_filename)

    filenamer = file_selector()
    print(filenamer)
    st.write('You selected `%s`' % filenamer)
    def file_selector123(path):
        filenames1 = os.listdir(folder_path) 
        selected_filename = st.selectbox('Please upload a user file', filenames1)
        return os.path.join(folder_path, selected_filename)
        


    filenamep = file_selector123()
    st.write('You selected `%s`' % filenamep) 
    b=filenamep.replace(chr(92),'/')
    a=filenamer.replace(chr(92),'/')
    #a=r"C:\Users\shahw\Desktop\RazorPayX_10_1_2021.xlsx"
    #b=r"C:\Users\shahw\Desktop\payouts - 10 Jan 21.xlsx"
    df1=pd.read_excel(a)
    df2=pd.read_excel(b)
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
elif option=='Bankit':
    def file_selector(folder_path=r"C:\Users\shahw\Desktop"):
        filenames10=os.listdir(folder_path)
        selected_filename=st.selectbox('Please upload a user file',filenames10)
        return os.path.join(folder_path, selected_filename)
    filenamea = file_selector()
    st.write('You selected `%s`' % filenamea) 
    def file_selector123(folder_path=r"C:\Users\shahw\Desktop"):

        filenames11=os.listdir(folder_path)
        selected_filename=st.selectbox('Please upload a vendore file',filenames11)
        return os.path.join(folder_path,selected_filename) 
    filenameb=file_selector123() 
    st.write('You selected `%s`' % filenameb) 
    b=filenameb.replace(chr(92),'/')
    a=filenamea.replace(chr(92),'/')
    dfbankit3=pd.read_excel(a)
    dfbankit3.head()
    dfbankit1=dfbankit3[(dfbankit3['Particulars']=='DMR-AREMIT')  & (dfbankit3['Transaction Status'] == "Success")]
    dfbankit4=pd.read_excel(b)
    dfbankit2= dfbankit4[(dfbankit4['Status']=='SUCCESS') & (dfbankit4['ProdName']=='IMPS')]
    dfbankit4.head()
    A=dfbankit1['Txn. Amount'].sum()
    B=dfbankit1['Txn. Amount'].count()
    C=dfbankit2['Amount'].sum()
    D=dfbankit2['Amount'].count()
    dic2={'No of txns success as per Ecaps':D,'No of Sucess txns as per Bankit':B,'Sum of txns amount as per Ecaps':A,'Sum of txns as per bankit':C,
     'Difference': D-B}
    df2=pd.DataFrame(dic2,index=['Value'])
    st.write('Your Result is below',df2.T)
elif option=='AEPS':
    def file_selector(folder_path=r"C:\Users\shahw\Desktop"):
        filenames10=os.listdir(folder_path)
        selected_filename=st.selectbox('Please upload a user file',filenames10)
        return os.path.join(folder_path, selected_filename) 
    filenamea = file_selector()
    st.write('You selected `%s`' % filenamea)

    def file_selector123(folder_path=r"C:\Users\shahw\Desktop"):

        filenames11=os.listdir(folder_path)
        selected_filename=st.selectbox('Please upload a vendore file',filenames11)
        return os.path.join(folder_path,selected_filename) 
    filenameb=file_selector123()
    st.write('You selected `%s`' % filenameb)
    def file_selector13(folder_path=r"C:\Users\shahw\Desktop"):

        filenames12=os.listdir(folder_path)
        selected_filename=st.selectbox('Please upload a vendore file',filenames12,key=" ")
        return os.path.join(folder_path,selected_filename) 
    filenamec=file_selector13()
    st.write('You selected `%s`' % filenamec)
    b=filenameb.replace(chr(92),'/')
    a=filenamea.replace(chr(92),'/')
    c=filenamec.replace(chr(92),'/')

    df_aeps=pd.read_excel(a)
    df_ecaps1=pd.read_excel(b)
    df_ecaps2=pd.read_excel(c)
    df_merged=df_ecaps=pd.concat([df_ecaps1, df_ecaps2],axis=0,
    join="outer",
    ignore_index=False,
    keys=None,
    levels=None,
    names=None,
    verify_integrity=False,
    copy=True)
    #print(df_ecaps)
    df22 = df_aeps[(df_aeps['Service'] == "Cash Withdrawl") & (df_aeps['Transaction Status'] == "Success")] 
    P=df22[ 'Txn. Amount'].sum()
    Q=df22[ 'Txn. Amount'].count()
    df33=df_ecaps[df_ecaps['ProductMajor']=='AEPS']
    R=df33['RechargeAmount'].sum()
    S=df33['RechargeAmount'].count() 
    dic3={'No of txns success as per AEPS':Q,'No of Sucess txns as per Ecaps':S,'Sum of txns amount as per AEPS':P,'Sum of txns as per Ecaps':R,
     'Difference': Q-S}
    df44=pd.DataFrame(dic3,index=['Value'])
    st.write('Your Result is below',df44.T) 
    
    



    
    
    

    









    
        

     
        
















 





    















    
     
    
    








 

 




 





    



