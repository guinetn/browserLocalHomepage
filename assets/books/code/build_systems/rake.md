## RAKE 

A make-like build utility for Ruby.

a build tool for automating tasks in Ruby. It provides a simple syntax to generate tasks and resolve tasks’ dependencies.
a simple ruby build program with capabilities similar to make
https://github.com/ruby/rake
gem install rake

Rakefile
```rake
task "third_task", %w[first_task second_task] do
    puts "third task"
end

task "first_task", %w[before_task] do
    puts "first task"
end

task "second_task", %w[before_task] do
    puts "second task"
end

task "before_task" do
    puts "before"
end
```

$> rake third_task
before
first task
second task
third task