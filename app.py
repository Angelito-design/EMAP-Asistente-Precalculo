# ============================================================
# EMAP - El Mejor Asistente de Precálculo
# Universidad Mariano Gálvez de Guatemala
# Integrantes:
#   - Ángel Luis Flores Urizar   2990-26-2483
#   - Elmer Daniel Juárez Aju    2990-26-2481
# Asignatura: Precálculo - Sección A
# ============================================================

import streamlit as st
import sympy as sp
from sympy import symbols, Eq, solve, factor, expand, simplify, diff, integrate, limit, latex, N
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import numpy as np
import matplotlib.pyplot as plt
import random

# -------------------- CONFIGURACIÓN DE PÁGINA --------------------
st.set_page_config(
    page_title="EMAP - El Mejor Asistente de Precálculo",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- ESTILOS CÁLIDOS Y MATES --------------------
st.markdown("""
<style>
    /* Fondo general cálido */
    .stApp {
        background-color: #FDF6F0;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F5E6D3;
        border-right: 2px solid #E8D5C4;
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: #5C4033 !important;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Botones */
    .stButton > button {
        background-color: #C4784A;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1.2rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #A65F35;
        color: white;
    }
    
    /* Cajas de resultado */
    .resultado-box {
        background-color: #FFF8F0;
        border-left: 5px solid #C4784A;
        padding: 1rem 1.2rem;
        border-radius: 0 10px 10px 0;
        margin: 1rem 0;
        color: #4A3728;
    }
    
    .paso-box {
        background-color: #F8EDE3;
        border-left: 4px solid #D4A373;
        padding: 0.8rem 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.6rem 0;
        color: #4A3728;
    }
    
    .error-box {
        background-color: #FDECEA;
        border-left: 5px solid #E07A5F;
        padding: 1rem;
        border-radius: 0 10px 10px 0;
        color: #5C2E2E;
    }
    
    .info-box {
        background-color: #E8F0E9;
        border-left: 5px solid #81B29A;
        padding: 1rem;
        border-radius: 0 10px 10px 0;
        color: #2F4F3A;
    }
    
    /* Inputs */
    .stTextInput > div > div > input {
        background-color: #FFFBF7;
        border: 1px solid #E8D5C4;
        border-radius: 6px;
    }
    
    /* Radio y select */
    .stRadio > label, .stSelectbox > label {
        color: #5C4033;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- UTILIDADES --------------------
x = symbols('x')
transformations = standard_transformations + (implicit_multiplication_application,)

def parsear(expr_str):
    """Intenta parsear una expresión matemática de forma amigable."""
    try:
        expr_str = expr_str.replace('^', '**').replace('sen', 'sin').replace('tg', 'tan')
        return parse_expr(expr_str, transformations=transformations)
    except Exception as e:
        raise ValueError(f"No pude entender la expresión: {expr_str}")

def mostrar_latex(expr):
    return f"${latex(expr)}$"

def caja_resultado(titulo, contenido):
    st.markdown(f"""
    <div class="resultado-box">
        <strong>{titulo}</strong><br>
        {contenido}
    </div>
    """, unsafe_allow_html=True)

def caja_paso(numero, texto):
    st.markdown(f"""
    <div class="paso-box">
        <strong>Paso {numero}:</strong> {texto}
    </div>
    """, unsafe_allow_html=True)

def caja_error(mensaje):
    st.markdown(f"""
    <div class="error-box">
        ⚠️ <strong>Error:</strong> {mensaje}
    </div>
    """, unsafe_allow_html=True)

def caja_info(mensaje):
    st.markdown(f"""
    <div class="info-box">
        ℹ️ {mensaje}
    </div>
    """, unsafe_allow_html=True)

# -------------------- ENCABEZADO --------------------
st.title("📐 EMAP")
st.markdown("### El Mejor Asistente de Precálculo")
st.caption("Universidad Mariano Gálvez de Guatemala  •  Precálculo Sección A")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Ángel Luis Flores Urizar**  \n2990-26-2483")
with col2:
    st.markdown("**Elmer Daniel Juárez Aju**  \n2990-26-2481")

st.markdown("---")

# -------------------- SIDEBAR --------------------
st.sidebar.title("📚 Módulos")
modulo = st.sidebar.radio(
    "Selecciona lo que quieres resolver:",
    [
        "🏠 Inicio",
        "🔢 Álgebra y Ecuaciones",
        "📈 Funciones (Dominio, Rango, Composición)",
        "📊 Graficar Funciones",
        "♾️ Límites",
        "📉 Derivadas",
        "∫ Integrales",
        "🎯 Máximos y Mínimos",
        "📝 Ejercicios de Práctica",
        "ℹ️ Acerca de EMAP"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Escribe las expresiones usando **x** como variable.\nEjemplos:\n- x**2 + 3*x - 4\n- (x+1)/(x-2)\n- sin(x) + cos(x)")

# ============================================================
# MÓDULO: INICIO
# ============================================================
if modulo == "🏠 Inicio":
    st.header("Bienvenido a EMAP")
    st.markdown("""
    Soy **El Mejor Asistente de Precálculo**. Estoy aquí para ayudarte a:
    
    - Resolver ecuaciones y factorizar
    - Analizar funciones (dominio, rango, composición)
    - Graficar funciones
    - Calcular límites
    - Derivar e integrar
    - Encontrar máximos y mínimos
    - Practicar con ejercicios
    
    **Cómo usarme:**
    1. Elige un módulo en el menú de la izquierda
    2. Escribe la expresión o los datos que te piden
    3. Observa el procedimiento paso a paso y la respuesta final
    
    ¡Empecemos!
    """)
    
    st.subheader("Ejemplo de prueba del proyecto")
    st.markdown("Analiza $f(x) = x^3 - 6x^2 + 9x + 1$ y determina sus puntos críticos.")
    
    if st.button("Resolver el ejemplo de prueba"):
        f = x**3 - 6*x**2 + 9*x + 1
        f_diff = diff(f, x)
        criticos = solve(f_diff, x)
        
        caja_paso(1, f"Función: {mostrar_latex(f)}")
        caja_paso(2, f"Derivada: $f'(x) = {latex(f_diff)}$")
        caja_paso(3, f"Igualamos a cero: ${latex(f_diff)} = 0$")
        caja_paso(4, f"Puntos críticos: $x = {latex(criticos)}$")
        
        for c in criticos:
            segunda = diff(f_diff, x).subs(x, c)
            tipo = "Mínimo relativo" if segunda > 0 else "Máximo relativo" if segunda < 0 else "Punto de inflexión"
            y_val = f.subs(x, c)
            caja_resultado(f"En x = {c}", f"f({c}) = {y_val}  →  **{tipo}**")

# ============================================================
# MÓDULO: ÁLGEBRA Y ECUACIONES
# ============================================================
elif modulo == "🔢 Álgebra y Ecuaciones":
    st.header("Álgebra y Ecuaciones")
    
    opcion = st.selectbox("¿Qué deseas hacer?", [
        "Resolver ecuación",
        "Factorizar expresión",
        "Expandir expresión",
        "Simplificar expresión"
    ])
    
    expr_input = st.text_input("Escribe la expresión o ecuación (usa = para ecuaciones):", 
                               placeholder="Ej: x**2 - 5*x + 6 = 0   o   x**2 - 9")
    
    if st.button("Resolver"):
        if not expr_input.strip():
            caja_error("Debes escribir una expresión o ecuación.")
        else:
            try:
                if opcion == "Resolver ecuación":
                    if "=" not in expr_input:
                        caja_error("Para resolver una ecuación debes incluir el signo =")
                    else:
                        izquierda, derecha = expr_input.split("=")
                        eq = Eq(parsear(izquierda.strip()), parsear(derecha.strip()))
                        solucion = solve(eq, x)
                        
                        caja_paso(1, f"Ecuación: ${latex(eq)}$")
                        caja_paso(2, "Despejamos la variable x")
                        if solucion:
                            caja_resultado("Solución", f"$x = {latex(solucion)}$")
                        else:
                            caja_resultado("Solución", "No se encontraron soluciones reales.")
                
                elif opcion == "Factorizar expresión":
                    expr = parsear(expr_input)
                    fact = factor(expr)
                    caja_paso(1, f"Expresión original: ${latex(expr)}$")
                    caja_paso(2, "Aplicamos factorización")
                    caja_resultado("Expresión factorizada", mostrar_latex(fact))
                
                elif opcion == "Expandir expresión":
                    expr = parsear(expr_input)
                    exp = expand(expr)
                    caja_paso(1, f"Expresión original: ${latex(expr)}$")
                    caja_paso(2, "Desarrollamos / expandimos")
                    caja_resultado("Expresión expandida", mostrar_latex(exp))
                
                elif opcion == "Simplificar expresión":
                    expr = parsear(expr_input)
                    simp = simplify(expr)
                    caja_paso(1, f"Expresión original: ${latex(expr)}$")
                    caja_paso(2, "Simplificamos")
                    caja_resultado("Expresión simplificada", mostrar_latex(simp))
            
            except Exception as e:
                caja_error(str(e))

# ============================================================
# MÓDULO: FUNCIONES
# ============================================================
elif modulo == "📈 Funciones (Dominio, Rango, Composición)":
    st.header("Análisis de Funciones")
    
    sub = st.radio("Elige una opción:", ["Dominio de una función", "Composición de funciones", "Evaluar función"])
    
    if sub == "Dominio de una función":
        f_str = st.text_input("Función f(x):", placeholder="Ej: 1/(x-2)   o   sqrt(x+3)")
        if st.button("Calcular dominio"):
            if not f_str:
                caja_error("Escribe una función.")
            else:
                try:
                    f = parsear(f_str)
                    caja_paso(1, f"Función: $f(x) = {latex(f)}$")
                    
                    from sympy import fraction
                    num, den = fraction(f)
                    if den != 1:
                        dens = solve(den, x)
                        caja_paso(2, f"El denominador no puede ser cero: ${latex(den)} \\neq 0$")
                        if dens:
                            caja_resultado("Dominio", f"$\\mathbb{{R}} - \\{{{latex(dens)}\\}}$")
                        else:
                            caja_resultado("Dominio", "$\\mathbb{R}$ (todos los reales)")
                    else:
                        caja_paso(2, "No hay denominadores que restrinjan el dominio de forma evidente.")
                        caja_resultado("Dominio", "En la mayoría de casos: $\\mathbb{R}$ (todos los reales). Verifica raíces pares manualmente si las hay.")
                except Exception as e:
                    caja_error(str(e))
    
    elif sub == "Composición de funciones":
        f_str = st.text_input("f(x) =", placeholder="x**2 + 1")
        g_str = st.text_input("g(x) =", placeholder="x - 3")
        if st.button("Calcular composición"):
            try:
                f = parsear(f_str)
                g = parsear(g_str)
                fog = f.subs(x, g)
                gof = g.subs(x, f)
                
                caja_paso(1, f"$f(x) = {latex(f)}$")
                caja_paso(2, f"$g(x) = {latex(g)}$")
                caja_resultado("(f ∘ g)(x)", mostrar_latex(simplify(fog)))
                caja_resultado("(g ∘ f)(x)", mostrar_latex(simplify(gof)))
            except Exception as e:
                caja_error(str(e))
    
    elif sub == "Evaluar función":
        f_str = st.text_input("f(x) =", placeholder="x**2 - 4*x + 3")
        valor = st.text_input("Valor de x:", placeholder="2")
        if st.button("Evaluar"):
            try:
                f = parsear(f_str)
                val = parsear(valor)
                resultado = f.subs(x, val)
                caja_paso(1, f"$f(x) = {latex(f)}$")
                caja_paso(2, f"Sustituimos $x = {latex(val)}$")
                caja_resultado(f"f({valor})", mostrar_latex(resultado))
            except Exception as e:
                caja_error(str(e))

# ============================================================
# MÓDULO: GRAFICAR
# ============================================================
elif modulo == "📊 Graficar Funciones":
    st.header("Graficar Funciones")
    
    f_str = st.text_input("Función a graficar f(x):", placeholder="x**3 - 6*x**2 + 9*x + 1")
    col_a, col_b = st.columns(2)
    with col_a:
        xmin = st.number_input("x mínimo", value=-5.0)
    with col_b:
        xmax = st.number_input("x máximo", value=5.0)
    
    if st.button("Graficar"):
        if not f_str:
            caja_error("Escribe una función.")
        else:
            try:
                f = parsear(f_str)
                f_lamb = sp.lambdify(x, f, modules=["numpy"])
                
                xs = np.linspace(xmin, xmax, 400)
                ys = f_lamb(xs)
                
                ys = np.array(ys, dtype=float)
                mask = np.isfinite(ys)
                xs, ys = xs[mask], ys[mask]
                
                fig, ax = plt.subplots(figsize=(9, 5))
                ax.plot(xs, ys, color="#C4784A", linewidth=2.5, label=f"f(x) = {f_str}")
                ax.axhline(0, color="#8B7355", linewidth=0.8)
                ax.axvline(0, color="#8B7355", linewidth=0.8)
                ax.grid(True, alpha=0.3, color="#D4A373")
                ax.set_facecolor("#FFF8F0")
                fig.patch.set_facecolor("#FDF6F0")
                ax.set_xlabel("x", color="#5C4033")
                ax.set_ylabel("f(x)", color="#5C4033")
                ax.set_title(f"Gráfica de f(x) = {f_str}", color="#5C4033", fontsize=13)
                ax.legend()
                st.pyplot(fig)
                
                caja_info("La gráfica se generó correctamente. Observa intersecciones, crecimiento y comportamiento.")
            except Exception as e:
                caja_error(f"No se pudo graficar: {e}")

# ============================================================
# MÓDULO: LÍMITES
# ============================================================
elif modulo == "♾️ Límites":
    st.header("Límites")
    
    f_str = st.text_input("Función f(x):", placeholder="(x**2 - 1)/(x - 1)")
    punto = st.text_input("x tiende a:", placeholder="1   o   oo (infinito)")
    
    if st.button("Calcular límite"):
        if not f_str or not punto:
            caja_error("Completa la función y el punto.")
        else:
            try:
                f = parsear(f_str)
                if punto.lower() in ["oo", "inf", "infinito", "+oo"]:
                    p = sp.oo
                    p_latex = "\\infty"
                elif punto.lower() in ["-oo", "-inf", "-infinito"]:
                    p = -sp.oo
                    p_latex = "-\\infty"
                else:
                    p = parsear(punto)
                    p_latex = latex(p)
                
                lim = limit(f, x, p)
                
                caja_paso(1, f"Función: $f(x) = {latex(f)}$")
                caja_paso(2, f"Calculamos $\\displaystyle\\lim_{{x \\to {p_latex}}} f(x)$")
                caja_paso(3, "Aplicamos propiedades de límites / sustitución / racionalización según corresponda")
                caja_resultado("Resultado del límite", mostrar_latex(lim))
                
            except Exception as e:
                caja_error(str(e))

# ============================================================
# MÓDULO: DERIVADAS
# ============================================================
elif modulo == "📉 Derivadas":
    st.header("Derivadas")
    
    f_str = st.text_input("Función f(x):", placeholder="x**3 - 6*x**2 + 9*x + 1")
    orden = st.selectbox("Orden de la derivada:", [1, 2, 3])
    
    if st.button("Derivar"):
        if not f_str:
            caja_error("Escribe una función.")
        else:
            try:
                f = parsear(f_str)
                derivada = f
                for i in range(orden):
                    derivada = diff(derivada, x)
                
                caja_paso(1, f"Función original: $f(x) = {latex(f)}$")
                caja_paso(2, f"Aplicamos reglas de derivación ({orden} vez/veces)")
                
                caja_info("Reglas utilizadas: regla de la potencia, regla de la suma/resta, regla del producto/cociente y regla de la cadena según corresponda.")
                
                caja_resultado(f"Derivada de orden {orden}", f"$f^{{({orden})}}(x) = {latex(derivada)}$")
                
            except Exception as e:
                caja_error(str(e))

# ============================================================
# MÓDULO: INTEGRALES
# ============================================================
elif modulo == "∫ Integrales":
    st.header("Integrales")
    
    tipo = st.radio("Tipo de integral:", ["Indefinida", "Definida"])
    f_str = st.text_input("Función f(x):", placeholder="x**2 + 3*x")
    
    a = b = None
    if tipo == "Definida":
        col1, col2 = st.columns(2)
        with col1:
            a = st.text_input("Límite inferior a:", value="0")
        with col2:
            b = st.text_input("Límite superior b:", value="2")
    
    if st.button("Integrar"):
        if not f_str:
            caja_error("Escribe una función.")
        else:
            try:
                f = parsear(f_str)
                
                if tipo == "Indefinida":
                    F = integrate(f, x)
                    caja_paso(1, f"Integral indefinida: $\\displaystyle\\int {latex(f)} \\, dx$")
                    caja_paso(2, "Aplicamos reglas de integración (potencia, suma, etc.)")
                    caja_resultado("Resultado", f"${latex(F)} + C$")
                
                else:
                    a_val = parsear(a)
                    b_val = parsear(b)
                    F = integrate(f, (x, a_val, b_val))
                    caja_paso(1, f"$\\displaystyle\\int_{{{latex(a_val)}}}^{{{latex(b_val)}}} {latex(f)} \\, dx$")
                    caja_paso(2, "Encontramos la antiderivada y evaluamos en los límites")
                    caja_resultado("Resultado", mostrar_latex(F))
            
            except Exception as e:
                caja_error(str(e))

# ============================================================
# MÓDULO: MÁXIMOS Y MÍNIMOS
# ============================================================
elif modulo == "🎯 Máximos y Mínimos":
    st.header("Máximos y Mínimos Relativos")
    
    f_str = st.text_input("Función f(x):", placeholder="x**3 - 6*x**2 + 9*x + 1")
    
    if st.button("Analizar extremos"):
        if not f_str:
            caja_error("Escribe una función.")
        else:
            try:
                f = parsear(f_str)
                f1 = diff(f, x)
                f2 = diff(f1, x)
                
                criticos = solve(f1, x)
                
                caja_paso(1, f"Función: $f(x) = {latex(f)}$")
                caja_paso(2, f"Primera derivada: $f'(x) = {latex(f1)}$")
                caja_paso(3, f"Segunda derivada: $f''(x) = {latex(f2)}$")
                caja_paso(4, f"Resolvemos $f'(x) = 0$ → puntos críticos: ${latex(criticos)}$")
                
                if not criticos:
                    caja_info("No se encontraron puntos críticos.")
                else:
                    for c in criticos:
                        try:
                            y = f.subs(x, c)
                            seg = f2.subs(x, c)
                            
                            if seg > 0:
                                tipo = "Mínimo relativo"
                            elif seg < 0:
                                tipo = "Máximo relativo"
                            else:
                                tipo = "Concavidad no determinada (posible punto de inflexión)"
                            
                            caja_resultado(
                                f"Punto crítico x = {c}",
                                f"$f({c}) = {latex(y)}$  →  **{tipo}**  \n(Prueba de la segunda derivada: $f''({c}) = {latex(seg)}$)"
                            )
                        except:
                            caja_resultado(f"Punto x = {c}", "No se pudo clasificar automáticamente.")
            
            except Exception as e:
                caja_error(str(e))

# ============================================================
# MÓDULO: EJERCICIOS DE PRÁCTICA
# ============================================================
elif modulo == "📝 Ejercicios de Práctica":
    st.header("Ejercicios de Práctica con Retroalimentación")
    
    ejercicios = [
        {
            "pregunta": "Resuelve: x² - 5x + 6 = 0",
            "respuesta": [2, 3],
            "explicacion": "Factorizamos (x-2)(x-3)=0 → x=2 o x=3"
        },
        {
            "pregunta": "Factoriza: x² - 9",
            "respuesta": "(x-3)(x+3)",
            "explicacion": "Diferencia de cuadrados: a²-b² = (a-b)(a+b)"
        },
        {
            "pregunta": "Calcula el límite: lim (x→2) (x²-4)/(x-2)",
            "respuesta": 4,
            "explicacion": "Factorizamos numerador: (x-2)(x+2)/(x-2) = x+2 → cuando x→2 da 4"
        },
        {
            "pregunta": "Deriva: f(x) = 3x⁴ - 2x² + 5",
            "respuesta": "12x³ - 4x",
            "explicacion": "Regla de la potencia: n·x^(n-1)"
        },
        {
            "pregunta": "Integra: ∫ (2x + 3) dx",
            "respuesta": "x² + 3x + C",
            "explicacion": "Integral de x^n es x^(n+1)/(n+1)"
        },
        {
            "pregunta": "Encuentra f'(x) si f(x) = (x²+1)(x-3)",
            "respuesta": "3x² - 6x + 1",
            "explicacion": "Regla del producto: u'v + uv'"
        },
        {
            "pregunta": "¿Cuál es el dominio de f(x) = 1/(x-5)?",
            "respuesta": "Todos los reales excepto 5",
            "explicacion": "El denominador no puede ser cero"
        },
        {
            "pregunta": "Evalúa f(2) si f(x) = x³ - 4x",
            "respuesta": 0,
            "explicacion": "2³ - 4·2 = 8 - 8 = 0"
        },
        {
            "pregunta": "Simplifica: (x² - 4)/(x+2)",
            "respuesta": "x-2",
            "explicacion": "Factorizamos y cancelamos (x+2)"
        },
        {
            "pregunta": "Punto crítico de f(x) = x² - 4x + 1",
            "respuesta": 2,
            "explicacion": "f'(x)=2x-4=0 → x=2 (mínimo)"
        }
    ]
    
    if "ejercicio_actual" not in st.session_state:
        st.session_state.ejercicio_actual = random.choice(ejercicios)
    
    ej = st.session_state.ejercicio_actual
    
    st.subheader("Ejercicio actual")
    st.markdown(f"**{ej['pregunta']}**")
    
    respuesta_usuario = st.text_input("Tu respuesta:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Verificar respuesta"):
            if not respuesta_usuario.strip():
                caja_error("Escribe una respuesta.")
            else:
                correcta = False
                resp = respuesta_usuario.strip().lower().replace(" ", "")
                if isinstance(ej["respuesta"], list):
                    for r in ej["respuesta"]:
                        if str(r) in resp:
                            correcta = True
                else:
                    if str(ej["respuesta"]).lower().replace(" ", "") in resp or resp in str(ej["respuesta"]).lower().replace(" ", ""):
                        correcta = True
                
                if correcta:
                    st.success("✅ ¡Correcto! Muy bien.")
                    caja_info(ej["explicacion"])
                else:
                    st.error("❌ Incorrecto. Revisa la explicación.")
                    caja_info(f"Respuesta esperada: {ej['respuesta']}\n\n{ej['explicacion']}")
    
    with col2:
        if st.button("Nuevo ejercicio"):
            st.session_state.ejercicio_actual = random.choice(ejercicios)
            st.rerun()
    
    st.markdown("---")
    st.subheader("Lista de ejercicios de ejemplo disponibles")
    for i, e in enumerate(ejercicios, 1):
        st.markdown(f"{i}. {e['pregunta']}")

# ============================================================
# MÓDULO: ACERCA DE
# ============================================================
elif modulo == "ℹ️ Acerca de EMAP":
    st.header("Acerca de EMAP")
    st.markdown("""
    ### El Mejor Asistente de Precálculo (EMAP)
    
    **Universidad Mariano Gálvez de Guatemala**  
    Facultad de Ingeniería  
    Asignatura: Precálculo – Sección A  
    
    **Integrantes:**
    - Ángel Luis Flores Urizar (2990-26-2483)
    - Elmer Daniel Juárez Aju (2990-26-2481)
    
    **Herramientas utilizadas:**
    - Python
    - Streamlit (interfaz)
    - SymPy (cálculo simbólico)
    - Matplotlib (gráficas)
    
    **Características:**
    - Resolución real de problemas (no respuestas memorizadas)
    - Explicaciones paso a paso
    - Manejo de errores de entrada
    - Generador de prácticas con retroalimentación
    - Interfaz cálida y agradable
    - 100% gratuito y público
    
    **Fecha de entrega:** 25 de octubre de 2026
    """)

# Footer
st.markdown("---")
st.caption("EMAP © 2026 • Universidad Mariano Gálvez de Guatemala • Precálculo Sección A")
