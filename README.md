# Phrase-Pair-Injection  
## Prerequisites

1. [Moses Decoder](http://www2.statmt.org/moses/?n=Development.GetStarted)
2. SRILM


## USAGE

### Training PBSMT
```
./smt.sh <src language code> <target language code> <path to the corpus directory> <path to the SRILM bin directory> <path to mosesdecoder tool> <path to the external-bin-dir that contains GIZA++, mkcls, snt2cooc.out files>
```

### Extracting Phrase Pairs from the Phrase Table

```
python ./capture.py <path to the phrase table> <path to save source file> <path to save target file> <path to save output statistics> <Language Model value> <distortion model value> <word penalty value> <translation model value> 
```
