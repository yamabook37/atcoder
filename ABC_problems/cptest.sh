#!/bin/bash

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

oj test -c "python3 ${problem_name}.py" -d test/${problem_name}
# ABC_problems に移動して実行
#oj test -c "python3 Atcoder/ABC_problems/${problem_name}.py" -d test/${problem_name}
