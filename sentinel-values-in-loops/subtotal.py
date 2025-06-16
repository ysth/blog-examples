
data = (
    { 'foo': 'Foo 1', 'value': 1 },
    { 'foo': 'Foo 1', 'value': 3 },
    { 'foo': 'Foo 2', 'value': 2 },
)

def show_row(foo="", value="", subtotal=False):
    if subtotal:
        show_row('====================','==========')
    print(f'{foo:20} {value:>10}')
    if subtotal:
        print()

show_row('Foo','Value')
previous_foo = None
subtotal = 0
for row in data:
    if previous_foo is not None:
        if previous_foo != row['foo']:
            show_row(previous_foo, value=subtotal, subtotal=True)
            subtotal = 0
    previous_foo = row['foo']
    subtotal += row['value']
        
    show_row(**row)

if previous_foo is not None:
    show_row(previous_foo, value=subtotal, subtotal=True)
