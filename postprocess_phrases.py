def post_process(f1,f2,f3,f4):
    """
    f1: Input Hindi phrases
    f2: Output Hindi Phrases (New File)
    f3: Input Marathi phrases
    f4: Output Marathi Phrases (New File)
    """
    with open(f1,"r") as f:
        inp = f.readlines()
    with open(f3,"r") as f:
        mr_inp = f.readlines()
    output = []
    mr_output=[]
    output_ind=[]
    remove_ind=[]
    start_time = time.time()
    for i in range(len(inp)):
        #print(i)
        
        x = inp[i].strip()
        if len(x) <= 1:
            continue
        x = x.replace(" ","0")
        y = inp[i]
        delete=[]
        out=[]
        mr_out=[]
        #print("striping decimals")
        if not x.isdecimal():
            flag=0
            j=0
            #print(f'len of output : {len(output)}')
            while j< len(output):

                str1 = re.sub(r'\d',"",output[j]).strip()
                #print(str1)
                str2 = re.sub(r'\d',"",y).strip()
                #print(str2)
                if str2 in str1:
                    flag=1
                    break
                elif str1 in str2:
                    delete.append(j)
                j+=1
            if flag==0:
                output.append(y)
                mr_output.append(mr_inp[i])
        #print("decimal stripped")
        if len(delete)>0:
            for x in range(len(output)):
                if x not in delete:
                    out.append(output[x])
                    mr_out.append(mr_output[x])
            mr_output = mr_out
            output=out
        #print("deleted req sent")
        if i%10000 == 0:
            a = round(time.time() - start_time,2)
            if a>60:
                min = round(a/60,2)
                print(f'iteration: {i}, time = {min} , current size of output : {len(output)}  sample of output: {output[-1]} : {mr_output[-1]}')
            else:
                print(f'iteration: {i}, time = {a} , current size of output : {len(output)}  sample of output: {output[-1]} : {mr_output[-1]}')
            start_time = time.time()
            print(f"len en: {len(output)}   len mr: {len(mr_output)} ")
            if(len(output) > 0 and len(mr_output)>0):
                with open(f2,"w") as fm:
                    fm.writelines(output)
                with open(f4,"w") as fw:
                    fw.writelines(mr_output)
    
    print(f"len en: {len(output)}   len mr: {len(mr_output)} ")
    if len(output) > 0 and len(mr_output)>0 :
        with open(f2,"w") as fm:
            fm.writelines(output)
        with open(f4,"w") as fw:
            fw.writelines(mr_output)
import sys
import re
import numpy as np
import time
f1=sys.argv[1]
f2=sys.argv[2]
f3=sys.argv[3]
f4=sys.argv[4]
post_process(f1,f2,f3,f4)
