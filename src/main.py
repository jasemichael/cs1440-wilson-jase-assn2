import time
import sys
from Report import Report


rpt = Report()

if len(sys.argv) < 1:
	print("Usage: src/main.py DATA_DIRECTORY")
	sys.exit(1)

#print("Reading the databases...", file=sys.stderr)
before = time.time()

f = open(sys.argv[1] + "/area_titles.csv", "r")

d = {}
for line in f:
	l = line.split(',')
	if len(l) >= 3:
		d[l[0]] = l[1] + ',' + l[2][:-1]
	else:
		d[l[0]] = l[1]
f.close()

f = open(sys.argv[1] + "/2018.annual.singlefile.csv", 'r')

all_num_areas = 0
all_gross_annual_wages = 0
all_max_annual_wage = ["", 0]
all_total_estab = 0
all_max_estab = ["", 0]
all_total_empl = 0
all_max_empl = ["", 0]

soft_num_areas = 0
soft_gross_annual_wages = 0
soft_max_annual_wage = ["", 0]
soft_total_estab = 0
soft_max_estab = ["", 0]
soft_total_empl = 0
soft_max_empl = ["", 0]

for line in f:
	l = line.split(',')
	if l[0].strip('"')[0] != 'C' and l[0].strip('"')[0] != 'U' and '000' != l[0].strip('"')[2:5] and len(l[0].strip('"')) == 5:
		if l[1].strip('"') == "0" and l[2].strip('"') == "10":
			all_num_areas += 1
			all_gross_annual_wages += int(l[10].strip('"'))
			if all_max_annual_wage[1] < int(l[10].strip('"')):
				all_max_annual_wage[0] = d[l[0]].strip('"')
				all_max_annual_wage[1] = int(l[10].strip('"'))
			all_total_estab += int(l[8].strip('"'))
			if all_max_estab[1] < int(l[8].strip('"')):
				all_max_estab[0] = d[l[0]].strip('"')
				all_max_estab[1] = int(l[8].strip('"'))
			all_total_empl += int(l[9].strip('"'))
			if all_max_empl[1] < int(l[9].strip('"')):
				all_max_empl[0] = d[l[0]].strip('"')
				all_max_empl[1] = int(l[9].strip('"'))

	if l[0].strip('"')[0] != 'C' and l[0].strip('"')[0] != 'U' and '000' != l[0].strip('"')[2:5] and len(l[0].strip('"')) == 5:
		if l[1].strip('"') == "5" and l[2].strip('"') == "5112":
			soft_num_areas += 1
			soft_gross_annual_wages += int(l[10].strip('"'))
			if soft_max_annual_wage[1] < int(l[10].strip('"')):
				soft_max_annual_wage[0] = d[l[0]].strip('"')
				soft_max_annual_wage[1] = int(l[10].strip('"'))
			soft_total_estab += int(l[8].strip('"'))
			if soft_max_estab[1] < int(l[8].strip('"')):
				soft_max_estab[0] = d[l[0]].strip('"')
				soft_max_estab[1] = int(l[8].strip('"'))
			soft_total_empl += int(l[9].strip('"'))
			if soft_max_empl[1] < int(l[9].strip('"')):
				soft_max_empl[0] = d[l[0]].strip('"')
				soft_max_empl[1] = int(l[9].strip('"'))

after = time.time()
#print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)



rpt.all.num_areas           = all_num_areas

rpt.all.gross_annual_wages  = all_gross_annual_wages
rpt.all.max_annual_wage     = all_max_annual_wage

rpt.all.total_estab         = all_total_estab
rpt.all.max_estab           = all_max_estab

rpt.all.total_empl          = all_total_empl
rpt.all.max_empl            = all_max_empl


rpt.soft.num_areas          = soft_num_areas

rpt.soft.gross_annual_wages = soft_gross_annual_wages
rpt.soft.max_annual_wage    = soft_max_annual_wage

rpt.soft.total_estab        = soft_total_estab
rpt.soft.max_estab          = soft_max_estab

rpt.soft.total_empl         = soft_total_empl
rpt.soft.max_empl           = soft_max_empl


# Print the completed report
print(rpt)
