#coding=utf8
import xlwt,datetime
#创建一个Excel表格
wbk = xlwt.Workbook(encoding='utf-8',style_compression=0)
#为创建的Excel表格添加一个工作表
'''
#第一个为一个sheet名字，第二个确定同一个cell单元是否可以重置
否则重写时，会报Exception: Attempt to overwrite cell: sheetname=u'etsy_sheet' rowx=0 colx=0

'''
sheet = wbk.add_sheet("etsy_sheet",cell_overwrite_ok=True)
sheet.write(0,0,"title")
# sheet.write(0,0,"new_title")##重新设置，需要cell_overwrite_ok=True
sheet.write(0,1,"time")
sheet.write(1,0,"aaaa")

font =xlwt.Font()
font.name="Times New Roman"
font.colour_index=12#11为银绿色  12为蓝色
font.height = 0x00C8 # C8 in Hex (in decimal) = 10 points in height.
#加黑
font.bold = True
#下划线
font.underline = True
#中划线
font.struck_out=True
font.escapement = xlwt.Font.ESCAPEMENT_SUBSCRIPT # May be: ESCAPEMENT_NONE, ESCAPEMENT_SUPERSCRIPT, ESCAPEMENT_SUBSCRIPT
style=xlwt.XFStyle()
style.font = font
sheet.write(1,1,"likai",style)
sheet.write(2,0,label = "Unformatted")
sheet.write(2,1,label = "Formateedsdfsdsdf",style=style)
# Setting the Width of a Cell
sheet.col(0).width =3333# 3333 = 1

# Entering a Date into a Cell
style.num_format_str = 'M/D/YY' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
sheet.write(3, 0, datetime.datetime.now(), style)

# Adding a Hyperlink to a Cell
#添加链接
sheet.write(4, 0, xlwt.Formula('HYPERLINK("http://www.google.com";"Google")')) # Outputs the text "Google" linking to http://www.google.com

#Merging Columns and Rows
'''
如：wirte_memrge(6,7,0,3,"second",style)
6,7.指要合并的行数，0.3指要合并的列数，’second‘是输入的文本，style是你设置的风格，可以不写
'''
sheet.write_merge(5, 5, 0, 3, 'First Merge') # Merges row 5's columns 0 through 3.
sheet.write_merge(6, 7, 0, 3, 'Second Merge', style) # Merges row 1 through 2's columns 0 through 3.

#Setting the Alignment for the Contents of a Cell
alignment = xlwt.Alignment() # Create Alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style1=xlwt.XFStyle()
style1.alignment=alignment
sheet.write(8,0,"cell center",style1)

# Adding Borders to a Cell
#增加边框
borders = xlwt.Borders() # Create Borders
borders.left = xlwt.Borders.DASHED # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40
style = xlwt.XFStyle() # Create Style
style.borders = borders # Add Borders to Style
sheet.write(9, 0, 'Cell Contents', style)

# Setting the Background Color of a Cell
#增加背景颜色
pattern = xlwt.Pattern() # Create the Pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
style2 = xlwt.XFStyle() # Create the Pattern
style2.pattern = pattern # Add Pattern to Style
sheet.write(10, 0, 'aaaa', style2)

# Adding a Formula to a Cell
# 添加运算
sheet.write(0, 2, 5) # Outputs 5
sheet.write(0, 3, 2) # Outputs 2
sheet.write(0, 4, xlwt.Formula('c1*d1')) # Should output "10"
sheet.write(0, 5, xlwt.Formula('SUM(c1,d1)')) # Should output "7"
sheet.write(13, 4, "[[u'RNS36 Good Nail Match Non Hot Fix Rhinestones Good Glass Material Strass SS3-SS30 Jet Black AB 12 Facets Machine Cut 288-1440pcs', u'12.50', '1', 'ss20 4.6-4.8m1440pcs'], [u'RNS36 Good Nail Match Non Hot Fix Rhinestones Good Glass Material Strass SS3-SS30 Jet Black AB 12 Facets Machine Cut 288-1440pcs', u'8.33', '1', 'ss30 6.3-6.5mm288pcs']]") # Should output "7"
wbk.save('d:/TestData.xlsx')##保存的文件路径和文件名，必须存在