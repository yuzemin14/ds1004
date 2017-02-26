rm -f "results/task$1.diff" 

cdir=$(pwd)

cd "$3" 
/usr/bin/hadoop fs -rm -r -f "task$1tmp.out"
/usr/bin/hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar -files "task$1/" -mapper "task$1/map.py" -reducer "task$1/reduce.py" -input "$2" -output "task$1tmp.out"
/usr/bin/hadoop fs -getmerge "task$1tmp.out" "task$1/task$1tmp.out"
cat "task$1/task$1tmp.out" | sort -n > "task$1/task$1tmp2.out"


if [ -e "task$1/task$1tmp2.out" ]
then
	DIFF=$(diff -w "$cdir/keys/task$1.out" "task$1/task$1tmp2.out")
	DIFFC=$(diff -w -y --suppress-common-lines "$cdir/keys/task$1.out" "task$1/task$1tmp2.out")
	if [ "$DIFF" ]
	then 
		echo "$DIFFC" > "$cdir/results/task$1.diff"
		echo "Task $1: Failed. See errors in results/task$1.diff"
	else
		echo "Task $1: Passed."
	fi
else
	echo "Task $1: Failed; no output generated."
fi
rm -f "task$1/task$1tmp2.out"
rm -f "task$1/task$1tmp.out"
/usr/bin/hadoop fs -rm -r -f "task$1tmp.out"

cd "$cdir"
