from transformers import pipeline
import pandas as pd
print("Cargando modelo de Inteligencia Artificial...")
analizador = pipeline("sentiment-analysis", model="finiteautomata/beto-sentiment-analysis")
comentarios = [
    "El servicio al cliente fue pésimo, nadie me ayudó con mi reembolso.",
    "¡Me encantó el producto! Llegó super rápido y funciona de maravilla.",
    "El sistema se cayó a mitad de la compra y me cobraron doble. Urgente ayuda.",
    "Es un producto decente, cumple con lo que promete pero el empaque llegó roto.",
    "La atención de la asesora Maria fue excelente, muy amable."
]
print("\n--- Analizando comentarios con IA ---")
resultados_finales = []

for comentario in comentarios:
    prediccion = analizador(comentario)[0]
    label = prediccion['label']
    score = prediccion['score']
    es_urgente = "SÍ 🚨" if label == "NEG" and score > 0.8 else "No"
    resultados_finales.append({
        "Comentario": comentario,
        "Sentimiento": "Positivo" if label == "POS" else ("Negativo" if label == "NEG" else "Neutral"),
        "Confianza IA": f"{score:.2%}",
        "Prioridad Urgente": es_urgente
    })
    df = pd.DataFrame(resultados_finales)
print("\n", df.to_string(index=False))
df.to_csv("reporte_sentimientos.csv", index=False, encoding="utf-8-sig")
print("\n¡Proyecto ejecutado! Se ha generado el archivo 'reporte_sentimientos.csv' con el análisis.")
