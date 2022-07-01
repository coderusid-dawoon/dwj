import pandas as pd

raw_data = {'col0' : [1,2,3,4],
'col1' : [10,20,30,40],
'col2' : [100, 200, 300, 400]
}

raw_data1 = pd.DataFrame(raw_data)
print(raw_data1)
raw_data1.to_excel(excel_writer=r'C:\Users\정다운\Desktop\Pythonwork\dwj\vmware\sample.xlsx') # 유니코드 인식에러 r, \\

df = pd.read_csv(r"C:\Users\정다운\Desktop\Pythonwork\dwj\txt\test.txt", sep="\t", encoding='utf-8')
print(df)
df.to_excel(r'C:\Users\정다운\Desktop\Pythonwork\dwj\vmware\test2.xlsx', index=True)