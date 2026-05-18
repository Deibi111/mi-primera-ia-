# Clasificador de Sentimientos Automatizado para Soporte al Cliente 🤖📊

Este proyecto utiliza Procesamiento de Lenguaje Natural (NLP) para analizar de forma automática los comentarios de clientes, clasificar su sentimiento (Positivo, Negativo o Neutral) y detectar alertas urgentes para el equipo de soporte técnico o comercial.

## 🚀 Características del Proyecto
- **Modelo de IA:** Utiliza `BETO` (`finiteautomata/beto-sentiment-analysis`), un modelo basado en la arquitectura BERT entrenado específicamente con español americano.
- **Lógica de Negocio Inteligente:** Identifica automáticamente comentarios críticos (sentimiento negativo con alta confianza de la IA) y los marca con una etiqueta de prioridad urgente (`SÍ 🚨`).
- **Análisis de Datos:** Estructura los resultados en un DataFrame usando `Pandas` y exporta de forma automática un reporte listo para el negocio en formato `.csv`.

## 🛠️ Tecnologías Utilizadas
- **Python 3.11+**
- **Hugging Face Transformers** (Para la integración de modelos LLM/NLP)
- **PyTorch** (Como motor de Deep Learning subyacente)
- **Pandas** (Para la manipulación y estructuración de datos)

## 📦 Estructura del Resultado en Consola
Cuando el script se ejecuta, procesa los textos y genera una salida estructurada como la siguiente:
```text
Comentario                                                     Sentimiento   Confianza IA   Prioridad Urgente
El servicio al cliente fue pésimo...                            Negativo       99.93%              SÍ 🚨
¡Me encantó el producto! Llegó super rápido...                  Positivo       99.84%                No