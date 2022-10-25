#open and read file as list
from asyncore import read
import imp
import re
import xlsxwriter
from datetime import datetime

workbook = xlsxwriter.Workbook('write_list.xlsx')
worksheet = workbook.add_worksheet()



with open('en.vtt','r') as f:
    lie=f.read()
ne=lie.split('\n'+'\n')
ce=[i.split('\n') for i in ne ]
de=[ce[i][1].split('-->') for  i in range(1,len(ne)-1)]
fe=[de[i][1].split(' p') for i in range(1,len(ne)-2)  ]
for raw,raw_data in enumerate(fe):
    for col,col_data in enumerate(raw_data):
         worksheet.write(raw,col,col_data)
workbook.close()  

  
#print(ce[1][1]) 
#print(de[0][0])
print(len(fe))
with open('de.vtt','r') as f:
    lig=f.read()
ng=lig.split('\n'+'\n')
cg=[i.split('\n') for i in ng ]
dg=[cg[i][1].split('-->') for  i in range(1,len(ng)-1)]
fg=[dg[i][1].split(' p') for i in range(1,len(ng)-800)  ]

workbook1 = xlsxwriter.Workbook('write_list1.xlsx')
worksheet1 = workbook1.add_worksheet()
for j,(en,ge) in enumerate(zip(de,dg)):
    tse=datetime.strptime(en[0].strip(),"%H:%M:%S.%f").strftime("%H:%M:%S")
    tsg=datetime.strptime(ge[0].strip(),'%H:%M:%S.%f').strftime("%H:%M:%S")
    tfg=datetime.strptime(fg[j][0].strip(),'%H:%M:%S.%f').strftime("%H:%M:%S")
    tfe=datetime.strptime(fe[j][0].strip(),'%H:%M:%S.%f').strftime("%H:%M:%S")
    if tse==tsg and tfg==tfe:
       continue
    elif tse==tsg  and tfe != tfg:
       fe[j][0]=fe[j+1][0]
       fe.pop(j+1)
       if fg[j][0]==fe[j][0]:
          continue
       else: 
         fe[j][0]=fe[j+1][0] 
         fe.pop(j+1)
    else : 
        continue    

    for raw,raw_data in enumerate(fe):
        for col,col_data in enumerate(raw_data):
            worksheet1.write(raw,col,col_data)
    workbook1.close()    