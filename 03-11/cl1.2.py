data = "string"

print(hasattr(data,"reverse"))
print(hasattr(data,"index"))
print(f'!!!{data.startswith("st")}!!!')
print(getattr(data,"startswith"))
starts = getattr(data ,"startswith")
print(f'!!!{starts()}!!!')
print(type(starts))
