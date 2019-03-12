class Color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class judge:
    def __init__(self, reference, tests):
        self.reference = reference
        self.tests = tests

    def __call__(self, func):
        ref_results = []
        results = []

        success_header = f"{Color.OKGREEN}SUCCESS{Color.ENDC}"
        failure_header = f"{Color.FAIL}FAILURE{Color.ENDC}"

        test_number = 0
        for test in self.tests:
            ref_result = self.reference(*test)
            result = func(*test)
            ref_results += [ref_result]
            results += [result]

            header = f"Test #{test_number} : {func.__name__}"
            if ref_result == result:
                print(
                    f"{header} : {success_header} - expected: {ref_result}, got: {result}"
                )
            else:
                print(
                    f"{header} : {failure_header} {test} - expected: {ref_result}, got: {result}"
                )
            test_number += 1

        return func
