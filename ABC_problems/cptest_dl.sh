#!/bin/zsh

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}
echo ${test_dir}

#oj-prepare https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
#https://github.com/online-judge-tools/template-generator/blob/master/README.ja.md
#code "/Users/yuki/Library/Application Support/online-judge-tools/prepare.config.toml"

cd /Users/yuki/Develop/pythonProject/python3/Atcoder/ABC_problems
#mkdir -p ${test_dir}
rm -rf ${test_dir} && oj download -d ${test_dir} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}

# make test directory by -d
# if [[ ! -e ${test_dir} ]] then
#     oj download -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
# fi