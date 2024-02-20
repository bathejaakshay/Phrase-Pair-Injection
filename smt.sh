# source language
src=$1

# target language
tgt=$2

# path to the corpus directory (where train and test files resides)
# The train files in the corpus should be of name: $corpus/train.<src> and $corpus/train.<tgt>
corpus=$3


langmod="${src}${tgt}_${tgt}_5"
mkdir -p $corpus/lang_models
mkdir -p $corpus/$src/$tgt

# path to the SRILM bin directory
LM=$4

# path to mosesdecoder
moses=$5
$moses/scripts/training/clean-corpus-n.perl $corpus/train $src $tgt $corpus/train.clean 1 80

$LM/i686-m64/ngram-count -order 5 -interpolate -kndiscount -unk -text $corpus/train.clean.$tgt -lm $corpus/lang_models/$langmod.lm
echo "lm done"

#cd $moses/scripts/training
#echo "changed directory"

# path to the external-bin-dir that contains GIZA++, mkcls, snt2cooc.out files.
giza=$6
$moses/scripts/training/train-model.perl -root-dir $corpus/$src/$tgt/trained_model -external-bin-dir $6 -alignment grow-diag-final-and -reordering msd-bidirectional-fe --corpus $corpus/train.clean --f $src --e $tgt --lm 0:5:$corpus/lang_models/$langmod.lm:0
echo "model trained"


