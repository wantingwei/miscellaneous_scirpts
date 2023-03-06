fileprefix="gene_"
filename="complied-All.fa" #your file name
seqs=$(cat ${filename} | awk '/>.*\|NP/')
for seq in $seqs
do
	suffix="|NP*"
	name=${seq/%$suffix}
	prefix=">"
	name=${name/#$prefix}
	name=$(echo $name | sed "s+\/+\\\/+g")
	echo $name
	cmd="/>${name}\|/"
	names=$(cat ${filename} | awk $cmd)
	for fn in $names
	do
		rename=$(echo $fn | sed "s+\/+\\\/+g")
		rename=$(echo $rename | sed "s+\>+\\\>+g")
		rename=$(echo $rename | sed "s+\|+\\\|+g")
		cmd="/${rename}/{flag=1;next}/\>/{flag=0}flag"
		segment=$(cat ${filename} | awk $cmd)
		ext=$(echo $fn | grep -o '|[A-Z][A-Z]')
		ext=${ext##*|}
		fname="${fileprefix}${ext}"
		echo $fn >> $fname.fasta
		echo $segment >> $fname.fasta
	done
done
