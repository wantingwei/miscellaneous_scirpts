fileprefix="gene_"
seqs=$(cat test.fasta | awk '/>.*\|NP/')
for seq in $seqs
do
	suffix="|NP*"
	name=${seq/%$suffix}
	prefix=">"
	name=${name/#$prefix}
	name=$(echo $name | sed "s+\/+\\\/+g")
	echo $name
	cmd="/>${name}\|/"
	names=$(cat test.fasta | awk $cmd)
	for fn in $names
	do
		rename=$(echo $fn | sed "s+\/+\\\/+g")
		rename=$(echo $rename | sed "s+\>+\\\>+g")
		rename=$(echo $rename | sed "s+\|+\\\|+g")
		cmd="/${rename}/{flag=1;next}/\>/{flag=0}flag"
		segment=$(cat test.fasta | awk $cmd)
		ext=$(echo $fn | grep -o '|[A-Z][A-Z]')
		ext=${ext##*|}
		fname="${fileprefix}${ext}"
		echo $fn >> $fname
		echo $segment >> $fname
	done
done
# />A\/North_Carolina\/04\/2016/,/>/p
# />A\/North_Carolina\/04\/2016/,/>/p
	#name=$(echo $name | sed "s+\/+\\\/+g")
	#names=$(sed '/>$name/p' test.fasta)
	#echo $names
	#cmd="/>${name}/,/>/p"
	#echo $cmd
	#cat test.fasta | sed $cmd