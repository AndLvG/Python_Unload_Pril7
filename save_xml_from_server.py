import pyodbc
import pandas as pd

CONN_STR = """Driver={SQL Server Native Client 11.0};
                                Server=dpx\mssqlserver2012;
                                Database=my_base;
                                uid=srz_admin;
                                pwd=srz_admin"""

conn = pyodbc.connect(CONN_STR)
df = pd.read_sql("""SELECT iesdb.dbo.lv_GetXML() AS x""", conn)
xml_file = df.iloc[0]['x']
with open("D:\\1\\test.xml", "w", encoding="UTF-8") as xml_writer:
    xml_writer.write(xml_file)
print('Готово')

