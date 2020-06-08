#!/bin/sh
sub_name=${1}
python ../1-FSO_localizer/make_matrix.py ${sub_name} 1
python ../1-FSO_localizer/make_matrix.py ${sub_name} 2
python ../2-SO_connectivity/make_matrix.py ${sub_name} 1
python ../2-SO_connectivity/make_matrix.py ${sub_name} 2
python ../2-SO_connectivity/make_matrix.py ${sub_name} 3
python ../2-SO_connectivity/make_matrix.py ${sub_name} 4
python ../2-SO_connectivity/ordering.py ${sub_name} 
