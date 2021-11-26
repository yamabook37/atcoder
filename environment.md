python環境について整理

基本は
pyenvでバージョン管理

### 用途
# pyenv versions
# pyenv local or global xxxx
・system

・pyenv local 3.8.2   # set to Python3.8
競プロ基本


・anaconda
(・pyenv local pypy3.6-7.3.0  # set to PyPy3 )
競プロPyPy使いたいとき
  # pypy3 xxx.py
機械学習
画像処理などライブラリが必要な場合
# pyenv local anaconda
# conda install xxx
で整える

# https://qiita.com/shimajiroxyz/items/788811730c152b18c997
LDFLAGS="-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --patch 3.8.2 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)
  成功!
LDFLAGS="-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --patch pypy3.6-7.3.0 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)


LDFLAGS="-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install 3.8.2
  できるらしいけど試さず終わった
LDFLAGS="-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install pypy3.6-7.3.0
  失敗