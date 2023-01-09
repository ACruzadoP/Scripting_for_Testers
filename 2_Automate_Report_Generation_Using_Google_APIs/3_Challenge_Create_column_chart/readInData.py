import csv

#final desired data formats:
# - Charts:         [["Test Name",<NumberOfAsserts>,<NumberOfFailedAsserts>],...]


data_list = []
with open('TestAnalysisData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        data_list.append(row)

chart_data = [data_list[0]]

for row in data_list[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    number_of_asserts = int(row[1])
    number_of_failed_asserts = int(row[2])
    chart_data.append([row[0],number_of_asserts,number_of_failed_asserts])



from string import Template
#first substitution is the header, the rest is the data
htmlString = Template("""<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  
  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
    <div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")


chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s,\n'%row
completed_html = htmlString.substitute(labels=chart_data[0],
data=chart_data_str)
    

with open('Chart.html','w') as f:
    f.write(completed_html)