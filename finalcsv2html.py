import csv
import cgi, cgitb
# import sys

# if len(sys.argv) < 2:
#   print "Usage: ./csv-html.py <your CSV file> <your HTML File.html>"
#   print
#   print
#   exit(0)

# Open the CSV file for reading
# reader = csv.reader(open(sys.argv[1]))
datadict_path = 'C:\Users\USER\Downloads\RIT\Deliverables\\'
reader = csv.reader(open(datadict_path + 'Data Dictionary_Inv.csv'))

# Create the HTML file
# f_html = open(sys.argv[2],"w");
f_html = open('Inventory_new.html',"w")

f_html.write('<title>Inventory Data Dictionary</title>')
f_html.write('<script src="submit_javascript.js"></script>')
f_html.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
f_html.write('<style>body {background-color: white;text-align: center;   color: black;}table, th, td {    border: 1px solid black;    border-collapse: collapse;}</style>')
f_html.write('<form method = "post" action = "processinput.cgi" id = "form_id">')
f_html.write('<table>')
for row in reader: # Read a single row from the CSV file
  f_html.write('<tr>')# Create a new row in the table
  for column in row: # For each column..
    if column == 'INPUT':
        f_html.write('<td>' + '<INPUT TYPE="TEXT" NAME="name" id = "inout" SIZE="20">' + '</td>')
    else:
        f_html.write('<td>' + column + '</td>')
  f_html.write('</tr>')


f_html.write('</table>')
f_html.write('<input type="submit" name = "submitbutton" value="Submit" />')
f_html.write('</form>')

