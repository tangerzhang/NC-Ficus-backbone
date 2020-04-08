# NC-Ficus-backbone
Codes for Ficus backbone review

### System requirment
- **Dependencies: PERL verion 5**
- **Operating system: CentOS 6.2**
- **Software version: release-date-20201124**
- **No non-stardand software required**

### Installation guide
- **Install command lines**
```
git clone https://github.com/tangerzhang/NC-Ficus-backbone.git
chmod +x *.pl
```
- **Install time**
```
Time: 5 seconds
```


### convert VCF to fasta
- **Parameter description**
> This script was used to extract tandem SNPs and converted it into fasta format. Each sample will have a single sequence in fasta format.
```
perl vcf2fasta.pl 
****************************************************************
    Usage: perl vcf2fasta.pl -v snp.vcf -o snp.fasta 
      -h : help and usage.
      -v : snp.vcf, input
      -o : snp.fasta, output
      -s:  sample included
      -e : sample excluded
      -m : missing rate, default 0.4
****************************************************************
```
- **demo data tesing**
>The demo VCF data contains 1000 lines and 17 individuals.
```
perl ~/software/script/faSize.pl snp.demo.fasta 
```
> Running this script on demo data needs only 1 second.  
After running the script, we will get a snp.demo.fasta file, containing 17 sequences with each having 881 SNPs. The parameter -m 0.4 will allow a mininum missing rate of 40% within each SNP site.

### Extract subset of samples from VCF
- **Parameter description**
> If we have dozons of samples in a VCF and only focus on a subset, this script subVCF.pl can be used for this purpose.
```
perl subVCF.pl 
************************************************************************
    Usage: perl subVCF.pl -v file.vcf -s sample.included.txt -o out.vcf
      -h : help and usage.
      -v : file.vcf, support .gz
      -s : included sample name
      -o : output vcf
      -m : missing rate (default 0.4)
************************************************************************
```
- **Demo data testing**
> Running this script on demo data requires only 1 second.   
The parameter -s will allow us to provide a list of sample names of interest, which will be further extracted by the script subVCF.pl
```
perl subVCF.pl -v demo.vcf -s sample.list -o subset.vcf
```
> The file 'sample.list' contains three samples:
```
FhiFhF3C
FmiFmU
FadWG105P
```
> After running the script 'subVCF.pl', we wil get a subset of VCF, containg only the listed 3 samples.

