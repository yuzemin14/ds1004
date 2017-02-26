MAPPER="$3/task$1/map.py"
REDUCER="$3/task$1/reduce.py"
DIFFFILE="results/task$1.diff"
TMPFILE="$3/task$1/task$1tmp.out"
if [ -e "$DIFFFILE" ]; then
	rm "$DIFFFILE" 
fi
cat "$2" | python "$MAPPER" | sort -n | python "$REDUCER" | sort -n > "$TMPFILE"

if [ -e "$TMPFILE" ]
then
	DIFF=$(diff -w "keys/task$1.out" "$TMPFILE")
	DIFFC=$(diff -w -y "keys/task$1.out" "$TMPFILE")
	if [ "$DIFF" ]
	then 
		echo "$DIFFC" > "results/task$1.diff"
		echo "Task $1: Failed. See errors in results/task$1.diff"
	else
		echo "Task $1: Passed."
	fi
else
	echo "Task $1: Failed; no output generated."
fi
rm -f "$TMPFILE"  


