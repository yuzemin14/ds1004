
/usr/bin/hadoop fs -get /user/ecc290/HW1data/parking-violations.csv
/usr/bin/hadoop fs -get /user/ecc290/HW1data/open-violations.csv

rm -r -f results
mkdir results

./testtask_hadoop.sh 1 /user/ecc290/HW1data/parking-violations.csv,/user/ecc290/HW1data/open-violations.csv $1
./testtask_local.sh 2 parking-violations.csv $1
./testtask_local.sh 3 open-violations.csv $1
./testtask_local.sh 4 parking-violations.csv $1
./testtask_local.sh 5 parking-violations.csv $1
./testtask_local.sh 6 parking-violations.csv $1
./testtask_local.sh 7 parking-violations.csv $1

rm parking-violations.csv
rm open-violations.csv
