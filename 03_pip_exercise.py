import camelcase

c = camelcase.CamelCase()

txt = "hello world. what if i told you that this is the last day of your development journey"

print(c.hump(txt))

