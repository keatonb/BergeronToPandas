# BergeronToPandas
Python function to read Bergeron et al. synthetic color outputs into Pandas dataframes.

The synthetic white dwarf colors available at http://www.astro.umontreal.ca/~bergeron/CoolingModels/ are super useful, but not super convenient to read into Python.  Import this function to read those files into a Pandas dataframe format. Takes a filename as the argument and returns an ordered dictionary of Pandas dataframes, in case the file contains multiple tables (i.e., for hydrogen and helium atmospheres).

This was not written to read in their "Evolutionary Sequences" files, but only the "Synthetic Colors."

Use as:
```
from BergeronToPandas import BergeronToPandas
tables = BergeronToPandas('Table_Mass_0.6') #OrderedDict of Pandas DataFrames
print(tables.keys()) #"['0.6 Mo Pure hydrogen grid; thick H models', '0.6 Mo Pure helium grid']"
print(tables.values()[0]) #Pandas DataFrame of synthetic colors for the hydrogen models
```

If you use those models in your work, please acknowledge them as described on [their website](http://www.astro.umontreal.ca/~bergeron/CoolingModels/). Shoutouts to this script are appreciated but optional.
