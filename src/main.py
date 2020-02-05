import time
import sys
from Report import Report


rpt = Report()

print("TODO: if sys.argv[1] is not given, print a usage message and exit")  # DELETE ME

print("Reading the databases...", file=sys.stderr)
before = time.time()

print("TODO: if opening the file 'sys.argv[1]/area_titles.csv' fails, let your program crash here")  # DELETE ME
print("TODO: Convert the file 'sys.argv[1]/area_titles.csv' into a dictionary")  # DELETE ME

print("TODO: if opening the file 'sys.argv[1]/2018.annual.singlefile.csv' fails, let your program crash here")  # DELETE ME
print("TODO: Collect information from 'sys.argv[1]/2018.annual.singlefile.csv', place into the Report object rpt")  # DELETE ME

after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)



print("TODO: Fill in the report for all industries")  # DELETE ME
rpt.all.num_areas           = 1337

rpt.all.gross_annual_wages  = 13333337
rpt.all.max_annual_wage     = ("Trantor", 123456)

rpt.all.total_estab         = 42
rpt.all.max_estab           = ("Terminus", 12)

rpt.all.total_empl          = 987654
rpt.all.max_empl            = ("Anacreon", 654)


print("TODO: Fill in the report for the software publishing industry")  # DELETE ME
rpt.soft.num_areas          = 1010

rpt.soft.gross_annual_wages = 101001110111
rpt.soft.max_annual_wage    = ("Helicon", 110010001)

rpt.soft.total_estab        = 1110111
rpt.soft.max_estab          = ("Solaria", 11000)

rpt.soft.total_empl         = 100010011
rpt.soft.max_empl           = ("Gaia", 10110010)


# Print the completed report
print(rpt)

print("\n\nTODO: did you delete all of these TODO messages?")  # DELETE ME
