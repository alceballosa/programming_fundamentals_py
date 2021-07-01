persona = {
    "nombre":"Julio",
    "apellido":"Florez",
    "edad":30,
    "notas": [1,2,3]
}

print(persona)

persona2 = {}
persona2["nombre"] = "María"
persona2["apellido"] = "López"
print(persona2)


js = {"users": []}
js["users"].append(persona)
js["users"].append(persona2)

print(js)
