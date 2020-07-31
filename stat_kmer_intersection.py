#!/usr/bin/env python
import os
import sys


def stat_inter(in_list, out_stat):
	print("Loading list")
	sample_db = {}
	with open(in_list, 'r') as fin:
		for line in fin:
			fn = line.strip()
			sample = fn.split('/')[-1].split('.')[0]
			sample_db[sample] = fn
	
	print("Loading kmers")
	kmer_db = {}
	for sample in sample_db:
		print("\tLoading %s"%sample)
		fn = sample_db[sample]
		kmer_db[sample] = set()
		with open(fn, 'r') as fin:
			for line in fin:
				kmer_db[sample].add(line.strip())
	print("Stat")
	stat_db = {}
	samples = sorted(sample_db.keys())
	for i in range(0, len(samples)-1):
		for j in range(i+1, len(samples)):
			sa = samples[i]
			sb = samples[j]
			print("\tIntersection %s %s"%(sa, sb))
			inter_set = kmer_db[sa].intersection(kmer_db[sb])
			key = sa+'-'+sb
			stat_db[key] = [len(inter_set)*1.0/len(kmer_db[sb]), "(%d/%d)"%(len(inter_set), len(kmer_db[sb]))]
			key = sb+'-'+sa
			stat_db[key] = [len(inter_set)*1.0/len(kmer_db[sa]), "(%d/%d)"%(len(inter_set), len(kmer_db[sa]))]
	
	print("Write result")
	with open(out_stat, 'w') as fout:
		fout.write("Sample\t%s\n"%('\t'.join(samples)))
		for i in range(0, len(samples)):
			info = [samples[i]]
			for j in range(0, len(samples)):
				if i != j:
					sa = samples[j]
					sb = samples[i]
					key = sa+'-'+sb
					info.append(','.join(map(str, stat_db[key])))
				else:
					info.append('\\')
			fout.write("%s\n"%('\t'.join(info)))

	print("Finished")


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: python %s <in_list> <out_stat>"%sys.argv[0])
	else:
		in_list, out_stat = sys.argv[1:]
		stat_inter(in_list, out_stat)

