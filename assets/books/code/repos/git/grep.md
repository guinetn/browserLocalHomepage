## git grep

git grep author                         Print lines matching a pattern. 
git grep "foo()"                        Search in working directory for foo()

git rev-list –all | xargs git grep -F ‘font-size: 52 px;’     search for the string "font-size: 52 px;" in your repository: