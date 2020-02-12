"""
 Compare a DNA kit (23andMe, AncestryDNA, etc) with the Clinvar database

vcf line:

1       865628  789256  G       A       .       .       ALLELEID=707587;CLNDISDB=MedGen:CN517202
;CLNDN=not_provided;CLNHGVS=NC_000001.10:g.865628G>A;CLNREVSTAT=criteria_provided,_single_submit
ter;CLNSIG=Likely_benign;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=SAMD11:1483
98;MC=SO:0001583|missense_variant;ORIGIN=1
"""


class dnadata(object):
    dna_providers = ['myheritage', 'livingdna', 'ancestry', '23andme']

    def __init__(self, name, provider=None):
        """read specified dna file"""
        pass


class vcf(object):
    base_url = 'ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37'

    def process_file(self, name):
        """process file in vcf format"""
        pass

    def process(self, stream):
        """process stream in vcf format"""
        pass

    def __init__(self, name=None):
        pass

    def latest(self):
        """download latest available copy of clinvar database in vcf format"""
        import requests
        import requests_ftp
        import gzip

        requests_ftp.monkeypatch_session()
        with requests.Session() as sess:
            resp = sess.get('{}/clinvar.vcf.gz'.format(self.base_url))

        return gzip.decompress(resp.content)

    def download(self, name=None, workdir=None):
        """download current or specified version of clinvar database"""
        pass


## EOF ##
