import os
import tarfile
import glob

import plio
import libpysat

# from datasketch import MinHashLSH, WeightedMinHashGenerator
# %pylab inline

import os
files = glob.glob('*.sl2')
for f in files:
    tar = tarfile.open(f)
    # Extract the spc and the ctg files
    list(map(tar.extract, [m for m in tar.getmembers() if '.spc' in m.name]))
files = glob.glob('*.spc')

files = glob.glob('*.spc')
d = {}
for f in files:
    s = libpysat.data.spectra.Spectra.from_file(f)
    ref1s = s.xs('REF1', level=1, axis=1)
#     res, denom = ref1s.continuum_correct(nodes=[512.6, 1547.7, 2404.2],correction_nodes=[512.6, 1547.7, 2587.9], func=libpysat.transform.continuum.regression)
#     d[s.loc['PRODUCT_ID'].iloc[0]] = res
    break
# res
