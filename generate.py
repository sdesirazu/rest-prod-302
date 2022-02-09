from datetime import datetime

import sys, re

print("<html><head>List of redirect URLs</head>")
print("<style>")
print("table, th, td {")
print("  border: 1px solid black;")
print("  border-collapse: collapse;")
print("</style>")
print("<body>")
# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("<hr/>Generated on date and time:", dt_string)
print("<hr/><table>")
print("<tr><th>Line number</th><th>Code</th><th>Redirect To</th><th>Redirect From</th></tr>\n")

lineno = 1

for line in sys.stdin:

    pattern301 = 'Redirecting \(301\)'
    pattern302 = 'Redirecting \(302\)'
    match301 = re.search(pattern301, line)
    match302 = re.search(pattern302, line)
 
    if (match301 or match302):
        patternRedir = '.*Redirecting \((.*)\) to <GET (.*)> from <GET (.*)>'
        matchRedir = re.search(patternRedir, line)
        print("<tr><td>", lineno, "</td><td>",matchRedir.group(1),"</td><td>",matchRedir.group(2), "</td><td>", matchRedir.group(3), "</td></tr>")
        lineno = lineno + 1

