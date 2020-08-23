import flag


env = flag.string("env", "production", "The environment to use")
workers = flag.int("workers", 4, "The number of workers")
isTrue = flag.bool("isTrue", True, "Is this true")

if __name__ == '__main__':
    flag.parse()

    print(env.upper())
    print(workers.value + 3)
    print(isTrue)
