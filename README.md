# Linux kernel evolution (showcase)

A showcase to compute/plot kernel evolution (size), see this issue: https://github.com/TuxML/ProjetIrma/issues/131

 * evokernelversions.py: execute TUXML using different versions 
 * kernel_options.csv: CSV file of number of options for different versions of the Linux kernel/architectures, thanks to Kconfiglib 
 * evo-query.ipynb: a Jupyter notebook to query the database (and get the size results of evokernelversions), merge data, and plot

We assume kernel_generator.py is present in the folder (eg wget https://raw.githubusercontent.com/TuxML/ProjetIrma/dev/kernel_generator.py)

Results: we plot evolution from 4.9.1 to 4.20.1 (below 4.9 requires gcc fixes: https://github.com/TuxML/ProjetIrma/issues/136)