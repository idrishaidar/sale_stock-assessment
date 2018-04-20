import csv
import sys
import time
import math
import collections

# pre-calculate the effective score of product
def initialize(file1, file2):
    eff_score = collections.defaultdict(dict)
    recommend_score = collections.defaultdict(dict)
    with open(file1) as inputfile1:
        reader1 = csv.reader(inputfile1, delimiter = '\t')

        for row in reader1:
                uid = row[0]
                pid = row[1]
                score = float(row[2])
                if (time.time() - float(row[3]) / 86400) < 1:
                    last_calc = 0
                else:
                    last_calc = math.ceil((time.time() - float(row[3])) / 86400)
                eff_score[uid][pid] =  round(score * math.pow(0.95, last_calc), 3)
    # show top 5 recommended products for a user (uid)
    def top_5_product(uid):
        print("Top 5 recommended products for user " + uid + ":")
        with open(file2) as inputfile2:
            reader2 = csv.reader(inputfile2, delimiter = '\t')
            for row2 in reader2:
                pid = row2[0]
                pscore = row2[1]
                if pid in eff_score[uid]:
                    recommend_score[pid] = float(pscore) * eff_score[uid][pid] + float(pscore)
                else:
                    recommend_score[pid] = float(pscore)       
        sorted_score = sorted(recommend_score.items(), key=lambda k_v: k_v[1], reverse=True)
        top5 = [k[0] for k in sorted_score[:5]]
        for p in top5:
            print(p)
        inputfile2.close()
    top_5_product(sys.argv[1])
    inputfile1.close()

input1 = 'user_preference.txt'
input2 = 'product_score.txt'
initialize(input1, input2)