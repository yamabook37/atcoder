#!/bin/zsh

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}
echo ${test_dir}

# run test by -c
oj test -c "python3 /Users/yuki/Develop/pythonProject/python3/Atcoder/ABC_problems/${problem_name}.py" -d test/${problem_name}