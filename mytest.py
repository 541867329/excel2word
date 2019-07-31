# coding=utf-8
import sys
from openpyxl import Workbook
from openpyxl import load_workbook
import os
from docx import Document
from docx.shared import Inches
from datetime import datetime
from xlrd import xldate_as_tuple
from docxtpl import DocxTemplate
#将excel导出到word的脚本

wb=load_workbook('./test.xlsx')#读取文件
ws=wb['MySheet'] #工作表
data=[ i for i in ws.values ]#获取工作表内的所有数据
#row1=data[0]#第一行的数组
#cell1=row1[0].value#第一行第一列数据
#date = xldate_as_tuple(cell1,0)#表格内的时间处理。改为直接将excel中的时间保存为文本
#time = datetime.datetime(*date)

listWord=["AA", "BB", "CC", "DD","EE"]#word模板中的关键字
listDict =[ dict(zip(listWord,data[i])) for i in range(0,len(data)) ]#形成字典列表

for i in range(0,len(listDict)):
	doc = DocxTemplate("项目日志-承建单位.docx")#导入模板
	doc.render(listDict[i])#替换模板中的关键字，listDict为列表，listDict[i]为字典
	doc.save(listDict[i]['AA']+"项目日志.docx")#按日期输出成word文档
	