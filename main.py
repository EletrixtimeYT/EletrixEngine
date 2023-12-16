from eletrixengine import engine

engine.logs.error("Ceci est une erreur de test")
engine.logs.warn("Ceci est un warn de test")
engine.logs.info("Ceci est info de test")

print(engine.window_property.init(height=500,width=500))
