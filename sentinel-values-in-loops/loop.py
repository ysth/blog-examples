
data = (
    { 'foo': 'Foo 1', 'value': 1 },
    { 'foo': 'Foo 1', 'value': 3 },
    { 'foo': 'Foo 2', 'value': 2 },
)

def show_row(foo="", value=""):
    print(f'{foo:20} {value:>10}')

show_row('Foo','Value')

for row in data:
    show_row(**row)
