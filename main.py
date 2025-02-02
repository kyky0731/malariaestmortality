import pandas
cols = ["SpatialDimensionValueCode", "TimeDim", "NumericValue", "Value", "Low", "High"]
csvfile = pandas.read_csv("malaria.csv", usecols=cols)

filtered = csvfile[csvfile["SpatialDimensionValueCode"] == "NGA"]
with open("file.txt", 'w') as f:
    f.write(filtered.to_string(header=True, index=False))
