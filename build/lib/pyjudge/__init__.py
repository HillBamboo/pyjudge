import time

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
    def __init__(self, reference_solution=None, tests=None, verbose=False):
        self.reference_solution = reference_solution
        if tests is None:
            raise ValueError("tests must be provided!")
        self.tests = tests
        self.verbose = verbose
        self.success_header = f'{Color.OKGREEN}SUCCESS{Color.ENDC}'
        self.failure_header = f'{Color.FAIL}FAILURE{Color.ENDC}'

    def __call__(self, func):
        print(f'\n=== Run {Color.HEADER}{func.__name__}{Color.ENDC}')
        if self.reference_solution is None: return self.test_single(func)
        else : return self.compare(func)

    def test_single(self, func):
        cnt_ok = 0
        total_time = 0
        for i, (*data, expected) in enumerate(self.tests):
            start = time.time()
            out = func(None, *data)
            end = time.time()
            total_time += (end - start)
            header = f" Test #{i}"
            if expected == out:
                if self.verbose:
                    print(
                        f"{header} : {self.success_header} - expected: {expected}, got: {out}"
                    )
                cnt_ok += 1
            else:
                print(
                    f"{header} : {self.failure_header} {data} - expected: {expected}, got: {out}"
                )
        avg_time = 1000 * total_time / len(self.tests)
        # mask_result = f'{Color.OKBLUE}OK{Color.ENDC}' if cnt_ok == len(self.tests) else f'{Color.FAIL}FAIL{Color.ENDC}'
        print(f'--- {Color.OKGREEN}PASS {cnt_ok}/{len(self.tests)}{Color.ENDC} ({avg_time:.0f}ms)')
        return func

    def compare(self, func):
        cnt_ok = 0
        total_time = 0
        for i, test in enumerate(self.tests):
            ref = self.reference_solution(*test)
            start = time.time()
            out = func(None, *test) # TODO: self = None
            end = time.time()
            total_time += (end - start)
            header = f"\tTest #{i}"
            if ref == out:
                if self.verbose:
                    print(
                        f"{header} : {self.success_header} - expected: {ref}, got: {out}"
                    )
                cnt_ok += 1
            else:
                print(
                    f"{header} : {self.failure_header} {test} - expected: {ref}, got: {out}"
                )
        avg_time = 1000 * total_time / len(self.tests)
        # mask_result = f'{Color.OKBLUE}OK{Color.ENDC}' if cnt_ok == len(self.tests) else f'{Color.FAIL}FAIL{Color.ENDC}'
        print(f'--- {Color.OKGREEN}PASS {cnt_ok}/{len(self.tests)}{Color.ENDC} ({avg_time:.0f}ms)')
        return func