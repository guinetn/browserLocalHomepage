# Switch/Case Statement (Python >= 3.10)

https://www.python.org/dev/peps/pep-3103/#basic-syntax

match x:
    case host, port:
        mode = "http"
    case host, port, mode:
        pass



http_code = "418"
match http_code:
    case "200":
        print("OK")
        do_something_good()
    case "404":
        print("Not Found")
        do_something_bad()
    case "418":
        print("I'm a teapot")
        make_coffee()
    case _:
        print("Code not found")

will replace (above we remove the repetition of http_code ==)

http_code = "418"
if http_code == "418":
    print("OK")
    do_something_good()
elif http_code == "404":
    print("Not Found")
    do_something_bad()
elif http_code == "418"
    print("I'm a teapot")
    make_coffee()
else:
    print("Code not found")        