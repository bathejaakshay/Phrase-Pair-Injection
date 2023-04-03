import statistics
import sys
#bn-hi 0.5 0.3 -1 0.2
#-0.0175885 0.0547269 0.23071 0.0235061
#0.00486439 0.0519429 0.166653 -0.0122001 HiMr ILCI BPE
#0.00869246 -0.00177925 0.0232645 0.00181537 ILCI1+2 bpe~
#0.0283145 0.0136206 0.260442 0.0294723 ILCI1+2 word level
# ml-ta 0.0435498 0.00716548 0.0660262 0.0411338
# bn-gu 0.0824832 0.0404014 0.0175244 0.00150509
# bn-hi 0.131781 0.0309374 0.00798419 0.0169979
# bn-mr 0.13106 0.0275451 -0.0379368 0.0355809
# pa-hi 0.0837709 0.0252701 0.00161317 -0.00190149
# pa-bn 0.0770937 0.038154 0.00695106 -0.00497429
# pa-gu 0.161303 0.0526818 -0.0175882 0.0176084
# pa-mr 0.0421559 0.0548517 0.0113851 0.0188543
# hi-pa 0.0816048 0.0237733 0.0424097 -0.0275249
# en-mr 0.108696 0.065217 -0.217391 0.04347

# Probabilities
#Language model, reordering model, word penalty, translation model

def weighted_average(probs):
	p0 = 0.5
	p1 = 0.3
	p2 = -1
	p3 = 0.2
	s=p0+p1+p2+p3
	return (p0*float(probs[0])+p1*float(probs[1])+p2*float(probs[2])+p3*float(probs[3]))/s

if __name__ == "__main__":
    line=[]
    entries=[]
    main=[]
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    f3 = sys.argv[3]
    f4 = sys.argv[4]
    lm = sys.argv[5]
    dist = sys.argv[6]
    wp = sys.argv[7]
    tm = sys.argv[8]

    '''
    f1: phrase table
    f2: hindi new
    f3: marathi new
    f4: stats new
    find following values in moses.ini
    lm = language model val
    dist = distortion val
    wp = word penalty
    tm = translation prob val
    '''
    fp=open(f1,"r")
    fh=open(f2,"w")
    fm=open(f3,"w")
    fs=open(f4,"w")
    count = 0
    for line in fp:
        if count%10000 == 0:
            print(count)
        count+=1
        line=line.split("|||")
        probs=line[2].strip().split()
        wa=weighted_average(probs)
        entries.append(wa)
        main.append(line)
    fs.write("max: "+str(max(entries))+"\n")
    fs.write("min: "+str(min(entries))+"\n")
    fs.write("mean: "+str(statistics.mean(entries))+"\n")
    fs.write("sd: "+str(statistics.stdev(entries))+"\n")
    #threshold=statistics.mean(entries)+0.5*statistics.stdev(entries)
    threshold = 0.98
    for itr in main:
        probs=itr[2].strip().split()
        wa=weighted_average(probs)
        if(wa>=threshold):
            fh.write(itr[0].strip()+'\n')
            fm.write(itr[1].strip()+'\n')
    fp.close()
    fh.close()
    fm.close()
    fs.close()

