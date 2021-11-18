#!/bin/bash

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

oj test -c "python3 ABC_problems/${problem_name}.py" -d test/${problem_name}

"""
AtCoder
├── cptest.sh #今回メインとなるシェルスクリプト
│
├── input.txt #ゴール2の手入力の値を入れるファイル
│
├── ABC_problems #コンテストの問題を格納するディレクトリ 
│
├── test #コンテストのサンプルケースを格納するディレクトリ
│
└── .vscode #VS Codeの設定ファイルを格納するディレクトリ
    ├── launch.json #ゴール2の設定ファイル
    └── tasks.json #ゴール1の設定ファイル
"""
