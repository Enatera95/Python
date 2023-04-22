import pandas as pd
import base64
import argparse
import imghdr
from mimetypes import guess_extension, guess_type
from PIL import Image


parser = argparse.ArgumentParser(description='CSV_Excel Converter by Datec (PNG) Software Team 2023')

parser.add_argument("--csv", help="Name of the csv.", default="Specify the CSV File.", required=True)
parser.add_argument("--base64", help="Name of the base64 column.", default="Specify the base64 column.", required=True)
parser.add_argument("--column", help="Name of the column to write the images to. For example A, B, C and so on.", default="Specify column", required=True)

args = parser.parse_args()


#df = pd.read_csv("Countries (2).csv")
df = pd.read_csv(args.csv)
a = 1;

#for i in df["Cflag"]:
for i in df[args.base64]:
  imgdata = base64.b64decode(i.replace("_x000D_", "")+'==')
  ext = guess_extension(guess_type("data:image/png;base64,"+i.replace("_x000D_", ""))[0])
  filename = 'flag'+str(a)+ext
  #filename = 'flag'+str(a)
  a = a+1 
  with open(filename, 'wb') as f:
    f.write(imgdata)
  #print(i)
  
# Create a new Pandas dataframe from df.
df2 = df;
  
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('out.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='countries')
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['countries']
  
for i in range(len(df.index)):
  img = Image.open('flag'+str(i+1)+ext)
  #worksheet.insert_image('E'+str(i+2), 'flag'+ str(i+1) +'.gif')
  #worksheet.insert_image(args.column+str(i+2), 'flag'+ str(i+1) +'.gif')
  worksheet.insert_image(args.column+str(i+2), 'flag'+ str(i+1)+ext)
  worksheet.set_column_pixels(4, 4, img.width)
  worksheet.set_row_pixels(i+1, img.height)

# Close the Pandas Excel writer and output the Excel file.
writer._save()
print('CSV_Excel Converter by Datec (PNG) Software Team 2023')
print('Base64 rows converted: '+str(len(df.index)))
print('Excel output file: out.xlsx')

