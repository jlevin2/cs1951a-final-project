import csv

data_dir = "./CollegeScorecard_Raw_Data/"
years = ["1996_97", "1997_98", "1998_99", "1999_00", "2000_01", "2001_02","2002_03","2003_04", "2004_05", "2005_06", "2006_07", "2007_08", "2008_09", "2009_10", "2010_11", "2011_12", "2012_13", "2013_14", "2014_15", "2015_16", "2016_17"]

output = "only_relevant_data.csv"

with open(output, "w+") as out_csv_file:
    field_names = ["YEAR", "INSTNM", "DEBT_MDN", "LO_INC_DEBT_MDN", "MD_INC_DEBT_MDN", "HI_INC_DEBT_MDN"]
    out = csv.DictWriter(out_csv_file, fieldnames=field_names)
    out.writeheader()
    for year in years:
        with open(data_dir + "MERGED" + year + "_PP.csv", "r") as year_csv:
            year_data = csv.DictReader(year_csv)
            for college in year_data:
                out_dict = dict()
                row_corrupted = False
                for field in field_names:
                    if field == "YEAR":
                        continue
                    val = college[field]
                    if val != "PrivacySuppressed" and val.lower() != "null":
                        out_dict[field] = val
                    else:
                        row_corrupted = True
                if not row_corrupted:
                    out_dict["YEAR"] = year
                    out.writerow(out_dict)
