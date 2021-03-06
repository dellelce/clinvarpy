"""
 Compare a DNA kit (23andMe, AncestryDNA, etc) with the Clinvar database.

example vcf line:

1       865628  789256  G       A       .       .

  ALLELEID=707587
  CLNDISDB=MedGen:CN517202
  CLNDN=not_provided
  CLNHGVS=NC_000001.10:g.865628G>A
  CLNREVSTAT=criteria_provided,_single_submitter
  CLNSIG=Likely_benign
  CLNVC=single_nucleotide_variant
  CLNVCSO=SO:0001483
  GENEINFO=SAMD11:148398;
  MC=SO:0001583|missense_variant
  ORIGIN=1
"""


class dnadata(object):
    """Reader to personal DNA Data."""

    dna_providers = ['myheritage', 'livingdna', 'ancestry', '23andme']

    def __init__(self, name, provider=None):
        """Read specified dna file."""
        pass


class vcf(object):
    """Wrapper class to the Clinvar database in VCF format."""

    base_url = 'ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37'

    def process_file(self, name):
        """Process file in vcf format."""
        with open(name) as fh:
            vcf = self.process(fh.read())

        return vcf

    def process(self, stream=None):
        """Process stream in vcf format."""
        vcf = []

        if stream is None:
            if self.rawdata is None:
                self.rawdata = self.latest()
                stream = self.rawdata
            else:
                stream = self.rawdata

        vcf_raw = stream.splitlines()

        for line in vcf_raw:
            line_a = line.split()
            if '#' in line[0]: continue

            vcf_line = []
            for i in [i.split(';') for i in line_a]:
                vcf_line += i

            vcf.append(vcf_line)

        return vcf

    def simple_dict(self, vcf=None):
        """Return a dictionary using chromosome and position in chromosome as keys."""
        vcf_dict = {}

        for line in vcf:
            chrm = line.pop(0)
            position = line.pop(0)

            #remove ORIGIN=1, we consider it the default
            line_pos = 0
            for item in line:
                if item == 'ORIGIN=1':
                    line.pop(line_pos)

                line_pos += 1

            if vcf_dict.get(chrm) is None:
                vcf_dict[chrm] = {}

            vcf_dict[chrm][position] = line

        return vcf_dict

    def __init__(self, name=None):
        """Set-up object."""
        self.rawdata = None
        self.simple = None

    def latest(self):
        """Download latest available copy of clinvar database in vcf format."""
        import requests
        import requests_ftp
        import gzip

        requests_ftp.monkeypatch_session()
        with requests.Session() as sess:
            resp = sess.get('{}/clinvar.vcf.gz'.format(self.base_url))

        self.rawdata = gzip.decompress(resp.content)

        return self.rawdata

    def download(self, name=None, workdir=None):
        """Download current or specified version of clinvar database."""
        pass


## EOF ##
