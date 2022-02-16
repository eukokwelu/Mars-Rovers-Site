from behave import step


@step(u'the test starts')
def step_impl(context):
    print("hi")


@step(u'the test runs')
def step_impl(context):
    print("test running")


@step(u'the test passes')
def step_impl(context):
    assert (True == True)
