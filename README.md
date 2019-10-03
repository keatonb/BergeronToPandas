# BergeronToPandas
Python function to read Bergeron et al. synthetic color outputs into Pandas dataframes.

The synthetic white dwarf colors available at http://www.astro.umontreal.ca/~bergeron/CoolingModels/ are super useful, but not super convenient to read into Python.  Import this function to read those files into a Pandas dataframe format. Takes a filename as the argument and returns an ordered dictionary of Pandas dataframes, in case the file contains multiple tables (i.e., for hydrogen and helium atmospheres).

This was not written to read in their "Evolutionary Sequences" files, but only the "Synthetic Colors."

If you use those models in your work, please acknowledge them as described on [their website](http://www.astro.umontreal.ca/~bergeron/CoolingModels/). Shoutouts to this script are appreciated but not required. 
