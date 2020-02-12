"""
 Compary a DNA kit (23andMe, AncestryDNA, 

vcf line:

1       865628  789256  G       A       .       .       ALLELEID=707587;CLNDISDB=MedGen:CN517202
;CLNDN=not_provided;CLNHGVS=NC_000001.10:g.865628G>A;CLNREVSTAT=criteria_provided,_single_submit
ter;CLNSIG=Likely_benign;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=SAMD11:1483
98;MC=SO:0001583|missense_variant;ORIGIN=1
"""

import csv


class dnadata(object):
    dna_providers = ['myheritage', 'livingdna', 'ancestry', '23andme']

    def __init__(self, name, provider=None):
        """read specified dna file"""
        pass


class vcf(object):
    def __init__(self, name):
        with open(name) as f:
            for line in f.readlines():
                line_a = line.split()

    def download(self, name=None):
        """download current or specified version of clinvar database"""
        import requests
        pass
                
## EOF ##
