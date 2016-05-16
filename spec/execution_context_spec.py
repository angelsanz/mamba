from expects import *
from doublex import *
from doublex_expects import *

from mamba.reporter import Reporter
from mamba.example import Example
from mamba.example_group import ExampleGroup


with description('the execution context'):
    with it('is not shared across examples'):
        dummy_reporter = Stub(Reporter)
        a_test_function = Spy().whatever
        another_test_function = Spy().whatever

        group = ExampleGroup('irrelevant subject')
        group.append(Example(a_test_function))
        group.append(Example(another_test_function))


        group.run(dummy_reporter)


        first_execution_context = a_test_function.calls[0].args[0]
        second_execution_context = another_test_function.calls[0].args[0]

        expect(first_execution_context).not_to(be(second_execution_context))
