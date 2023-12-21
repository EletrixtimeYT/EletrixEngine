from eletrixengine import engine

logs = engine.Logs()
logs.error("Ceci est une erreur de test")
logs.warn("Ceci est un warn de test")
logs.info("Ceci est info de test")

print(engine.WindowProperty().init(height=500,width=500))
