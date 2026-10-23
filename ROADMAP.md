# Roadmap: Cybersecurity AI Engineer

**Perfil** Ethical Hacker en transicion a AI Security Engineer / Red Teamer de IA

**Base Actual** Python intermedio, Bash, Kali Linux, CTF's, redes, JS/React basico 



**Objetivo:** Convertirte en un profesional capaz de construir sistemas de IA y romperlos éticamente. Perfil híbrido de alta demanda: **AI Security Engineer / Red Teamer de IA**.


🛡️

La seguridad debe practicarse únicamente en sistemas propios o con autorización explícita. Documenta siempre la divulgación responsable.


## 🧭 Plan de avance práctico

### Tu punto de partida

Tu Python intermedio y la experiencia en CTFs son una buena base. El objetivo es conectar esas fortalezas con fundamentos de datos y ML, seguridad de LLMs y prácticas de ingeniería defensiva. No necesitas dominar toda la ciencia de datos antes de comenzar con seguridad de IA.

### Cómo usar esta ruta

En cada ciclo de estudio, avanza con cuatro pasos: aprende un concepto, construye un experimento pequeño, evalúa los resultados y documenta lo aprendido. Empieza con seguridad de LLMs en paralelo con los fundamentos de ML; aumenta la dificultad conforme entiendas cómo se entrenan y despliegan los modelos.


🛡️

Practica únicamente en sistemas propios, laboratorios diseñados para ello o entornos con autorización explícita. Usa datos sintéticos o sanitizados; no pruebes herramientas contra servicios de terceros. Mantén las pruebas de red team acotadas y documenta mitigaciones, límites y autorización.



### Primer ciclo sugerido

1. **Datos:** repasa NumPy y Pandas; carga un dataset pequeño, limpia campos y documenta qué representa cada columna.
2. **ML clásico:** entrena un clasificador o detector de anomalías sencillo; separa entrenamiento y evaluación, y registra precision, recall y falsos positivos.
3. **Redes neuronales:** reproduce un ejemplo pequeño en PyTorch y observa cómo cambian las métricas al ajustar el entrenamiento.
4. **Seguridad de LLM:** dibuja el flujo de una aplicación RAG mínima y sus límites de confianza. Diseña pruebas seguras para tu propio prototipo y registra resultado, riesgo y mitigación.

Ajusta la duración de cada paso a tu disponibilidad; el entregable importa más que cumplir un calendario rígido.

### Proyectos prioritarios para tu portafolio

#### 1. LLM Red Team Lab

Construye un banco de evaluación en Python para una aplicación de LLM local o propia. Agrupa escenarios de prueba por riesgo (por ejemplo, instrucciones conflictivas, contenido recuperado no confiable y exposición accidental de información de prueba), sin dirigirlos a servicios ajenos. Registra versión del modelo, comportamiento esperado y observado, severidad, mitigación y resultado de la nueva prueba. Puedes evaluar con herramientas como Garak o promptfoo dentro de un entorno controlado y autorizado.

**Entregable:** README con alcance y límites, arquitectura del laboratorio, casos de prueba no sensibles, resultados antes/después y controles recomendados.

#### 2. AI-Powered Log Analyzer

Crea un analizador defensivo que use logs sintéticos o sanitizados de un entorno propio. Combina reglas transparentes para patrones como intentos repetidos de autenticación con un modelo local que resuma por qué un evento merece revisión. Compara sus resultados con una línea base, mide falsos positivos y evita que el prototipo ejecute acciones automáticas sobre sistemas.

**Entregable:** script o aplicación pequeña, conjunto de datos de prueba, métricas, ejemplos de explicación y sección sobre privacidad y limitaciones.

#### 3. Threat Model ATLAS para una aplicación RAG

Documenta el flujo de datos, activos, componentes, límites de confianza y posibles impactos. Mapea a MITRE ATLAS las técnicas pertinentes a alto nivel y, para cada riesgo, anota controles preventivos/detectivos y cómo comprobarlos de forma segura en tu laboratorio.

**Entregable:** threat model en Markdown, diagrama de arquitectura, tabla riesgo–control–evidencia y supuestos del análisis.

### Criterios para considerar un ciclo terminado

- Puedes explicar cómo se entrenó y evaluó tu modelo, y qué limitaciones tienen sus métricas.
- Tienes una aplicación de prueba propia con límites de confianza y controles documentados.
- Cada hallazgo incluye evidencia reproducible en el laboratorio, impacto, mitigación y retest.
- El repositorio incluye instrucciones de ejecución, datos de prueba permitidos y límites de uso.

## 🧭 FASE 0 — Fundamentos (Meses 1–2)

Antes de asegurar IA, necesitas dominar sus cimientos técnicos.

### 🐍 Python para IA y Seguridad

- **Lenguaje base:** Python 3.11+
- **Librerías esenciales:**
    - NumPy → operaciones matriciales y vectores
    - Pandas → manipulación de datos
    - requests + BeautifulSoup → automatización y scraping
    - asyncio → scripts concurrentes para pentesting
- **Práctica:** Reescribe 3 scripts viejos de pentesting en Python moderno con type hints.

### 📐 Matemáticas Mínimas Viables

- Álgebra lineal: matrices, vectores, producto punto y descomposición
- Cálculo: derivadas parciales y gradiente descendente
- Estadística: distribuciones, media, varianza y métricas de evaluación
- **Recurso clave:** *Mathematics for Machine Learning* (Deisenroth), disponible gratuitamente en el PDF oficial

### 🐧 Base Hacker (Reforzamiento)

- Linux avanzado: bash, systemd, permisos y strace
- Redes: TCP/IP, DNS, HTTP/S y TLS
- Herramientas: Burp Suite, Nmap, Wireshark y Metasploit
- Extra: OWASP Top 10 Web clásico, como analogía para LLMs

## 🤖 FASE 1 — Construir IA (Meses 2–5)

Un hacker ético de IA debe saber construir lo que rompe.

### 📊 Machine Learning Clásico

- **Framework:** scikit-learn
- **Temas:**
    - Clasificación: Logistic Regression, Random Forest y SVM
    - Regresión: Linear, Ridge y Lasso
    - Clustering: K-Means y DBSCAN
    - Detección de anomalías: Isolation Forest y One-Class SVM
- **Aplicación de seguridad:** Entrenar un IDS con CICIDS2017

### 🧠 Deep Learning

- **Frameworks:** PyTorch (recomendado) o TensorFlow
- **Temas:**
    - Redes densas (MLP)
    - CNNs (visión)
    - RNNs / LSTMs (secuencias)
    - Transfer learning
- **Práctica:** Crear un clasificador de malware basado en imágenes binarias

### 🔤 Arquitectura Transformer (Crítico)

- Mecanismo de self-attention
- Multi-head attention
- Positional encoding
- Encoder-Decoder, arquitectura original
- Variantes: BERT (encoder), GPT (decoder) y T5 (encoder-decoder)
- **Recurso obligatorio:** *Attention Is All You Need*, paper original
- **Práctica:** Implementar un Transformer pequeño desde cero en PyTorch

## ⚔️ FASE 2 — Núcleo de Seguridad en IA (desde el mes 3, en paralelo con Fase 1)

Aquí tu perfil se vuelve el de un auditor: dejas de ser únicamente usuario de IA.

### 🎯 Adversarial Machine Learning

- Ataques de evasión: FGSM, PGD y C&W
- Data poisoning: envenenamiento de datasets de entrenamiento
- Model inversion: extracción de datos de entrenamiento del modelo
- Model extraction: extracción de un modelo mediante consultas a una API
- Membership inference: determinar si un dato estuvo en el entrenamiento
- **Herramientas:** CleverHans y Adversarial Robustness Toolbox (ART) de IBM

### 💬 Seguridad en LLMs y GenAI

- **Prompt Injection:**
    - Directa, realizada por una persona usuaria maliciosa
    - Indirecta, mediante RAG, emails o webs
- Jailbreaking: DAN, role-play y técnicas de codificación
- **Seguridad en RAG:**
    - Envenenamiento de bases vectoriales
    - Exfiltración mediante documentos maliciosos
    - Cross-tenant leakage
- Fuga de datos: system prompt leaking y extracción de PII

### OWASP Top 10 for LLM Applications

1. LLM01: Prompt Injection
2. LLM02: Insecure Output Handling
3. LLM03: Training Data Poisoning
4. LLM04: Model DoS
5. LLM05: Supply Chain Vulnerabilities
6. LLM06: Sensitive Information Disclosure
7. LLM07: Insecure Plugin Design
8. LLM08: Excessive Agency
9. LLM09: Overreliance
10. LLM10: Model Theft

### 🛠️ Herramientas de Red Teaming de IA

- **Garak (NVIDIA):** escáner de vulnerabilidades para LLMs
- **PyRIT (Microsoft):** framework de red teaming automatizado
- **promptfoo:** testing de prompts y evaluaciones
- **Rebuff:** detección de prompt injection
- **LLM Guard:** suite de protección
- **Gandalf (Lakera):** CTF de prompt injection

## 🛡️ FASE 3 — Defensa, MLOps y Despliegue (Meses 10–12)

Convertir el conocimiento en producción real.

### 🔐 MLSecOps

- **Supply chain de modelos:**
    - Riesgos de archivos `.pickle` maliciosos y ejecución arbitraria de código
    - Formato seguro: `safetensors`
    - Verificación de hashes de pesos
- CI/CD para modelos: pipelines seguros con firmas
- Monitoring: drift detection y alertas de anomalías

### 🚧 Guardrails y Defensa

- NeMo Guardrails (NVIDIA)
- Llama Guard (Meta)
- Filtros personalizados: regex y clasificadores auxiliares
- **Arquitectura defensiva:**
    - Validación de entradas
    - Sanitización de salidas
    - Sandboxing de agentes
    - Least privilege para herramientas

### ☁️ Cloud y Despliegue

- Contenedores: Docker y Podman
- APIs: FastAPI y Flask
- Cloud IA: AWS Bedrock, Azure OpenAI y GCP Vertex AI
- Orquestación: Kubernetes básico
- Seguridad cloud: IAM y gestión de secretos con Vault

## 🎯 Proyectos de Portafolio

### Proyecto 1: LLM Firewall

- **Objetivo:** Proxy que analice prompts entrantes y bloquee inyecciones
- **Stack:** FastAPI + Rebuff + clasificador personalizado
- **Funciones:** logging, rate limiting y dashboard
- **Entregable:** repositorio en GitHub con demo en video

### Proyecto 2: Red Team de Chatbot Local

- **Objetivo:** Auditar un LLM open source con Garak
- **Stack:** Ollama + Llama 3 + Garak + PyRIT
- **Entregable:** reporte de vulnerabilidades y parches propuestos

### Proyecto 3: IDS con IA

- **Objetivo:** Detectar tráfico malicioso con ML
- **Stack:** scikit-learn + CICIDS2017 + FastAPI
- **Entregable:** modelo + API + métricas de F1, precision y recall

### Proyecto 4 (Bonus): Adversarial Attack Demo

- **Objetivo:** Evaluar la robustez de un clasificador de imágenes con FGSM
- **Stack:** PyTorch + ART
- **Entregable:** notebook con visualizaciones de antes y después

## 📚 Certificaciones y Recursos

### Certificaciones

- CAISP — Certified AI Security Professional
- GIAC GMLS — GIAC Machine Learning for Security
- AI Security Fundamentals (Cloud Security Alliance)
- CompTIA SecurityAI (emergente)

### Comunidades

- AI Village (DEF CON)
- MLSecOps Community
- OWASP GenAI Security Project
- Hack The Box AI Challenges
- Gandalf (Lakera) — CTF de prompt injection

### Libros y Papers

- *Adversarial Machine Learning* (Joseph et al.)
- *AI Security and Privacy* (varios autores)
- Paper: *Attention Is All You Need*
- Paper: *Universal and Transferable Adversarial Attacks on Aligned LLMs*
- OWASP Top 10 for LLM (PDF oficial)

### Canales y Cursos

- DeepLearning.AI — cursos de seguridad de IA
- Lakera Blog — investigación sobre prompt injection
- Simon Willison's Blog — seguridad de LLMs
- Trail of Bits Blog — seguridad de IA y ML

## 🗓️ Cronograma Resumido

| Mes | Foco | Entregable |
| --- | --- | --- |
| 1–2 | Fundamentos | Scripts Python + repaso de redes |
| 3–5 | Construir IA | Modelo ML + Transformer propio |
| 6–9 | Seguridad IA | Red team report + herramientas |
| 10–12 | Defensa/MLOps | Proyecto de producción + portafolio |

---

## 🎯 Progress Tracker (Current Cycle)

*Marca las casillas a medida que completas los entregables. ¡Este es mi compromiso público!*

### Fase 0 — Fundamentos (Meses 1–2)
- [x] Configurar mi portafolio en GitHub (Landing Page y Roadmap)
- [x] Reescribir script 1 de pentesting con Python moderno (type hints)
- [ ] Reescribir script 2 de pentesting con Python moderno
- [ ] Reescribir script 3 de pentesting con Python moderno
- [ ] Repasar NumPy y Pandas con un dataset de logs

### Fase 1 — Construir IA (Meses 2–5)
- [ ] Entrenar mi primer modelo de Machine Learning clásico (scikit-learn)
- [ ] Implementar un Transformer pequeño desde cero en PyTorch

### Fase 2 — Seguridad de IA (En paralelo)
- [ ] Completar los 7 niveles de Gandalf (Lakera)
- [ ] Instalar y ejecutar mi primer escaneo con Garak en un modelo local

### Fase 3 — Defensa y Despliegue (Meses 10–12)
- [ ] Crear un LLM Firewall básico con FastAPI


## 💡 Consejos Finales

1. Documenta todo en un blog o GitHub. El portafolio pesa más que el CV.
2. Participa en CTFs de IA desde el mes 6: Gandalf y HTB AI.
3. Contribuye a open source: Garak, PyRIT y Rebuff aceptan PRs.
4. No esperes a saberlo todo para aplicar a trabajos. El campo es nuevo y todo el mundo está aprendiendo.
5. Ética primero: tu rol es defender, no atacar sin permiso. Documenta la divulgación responsable.

## 🔗 Recursos Rápidos

- OWASP LLM Top 10
- Garak
- PyRIT
- promptfoo
- Gandalf
- Adversarial Robustness Toolbox (ART)
- AI Village
- arXiv — buscar “adversarial LLM”
