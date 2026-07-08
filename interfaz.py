import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modelos.smartgate import SmartGate
from analisis.prediccion import SimulacionPredictiva
from analisis.sustentabilidad import Sustentabilidad

class SmartGateGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("SmartGate IA - Sistema de Control de Acceso")
        self.ventana.geometry("650x450")
        self.ventana.resizable(False, False)

        self.gate = SmartGate()
        self.prediccion = SimulacionPredictiva()
        self.sustentabilidad = Sustentabilidad()
        self.crear_componentes()

    def crear_componentes(self):
        titulo = tk.Label(
            self.ventana, 
            text="SMARTGATE IA", 
            font=("Arial", 22, "bold"), 
            fg="#1a365d"
        )
        titulo.pack(pady=15)

        # 2. SECCIÓN: CONTROL DE ACCESO MANUAL (Fase 4)
        frame_acceso = tk.LabelFrame(self.ventana, text=" Módulo de Validación y Acceso ", font=("Arial", 11, "bold"), padx=15, pady=15)
        frame_acceso.pack(fill="x", padx=20, pady=10)

        tk.Label(frame_acceso, text="Ingresa Matrícula:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        
        self.entrada_matricula = tk.Entry(frame_acceso, font=("Arial", 12), width=20)
        self.entrada_matricula.grid(row=0, column=1, padx=10, pady=5)
        self.entrada_matricula.focus()

        btn_validar = tk.Button(
            frame_acceso, 
            text="Validar Acceso", 
            font=("Arial", 10, "bold"), 
            bg="#2b6cb0", 
            fg="black", 
            command=self.procesar_validacion
        )
        btn_validar.grid(row=0, column=2, padx=10, pady=5)

        # Caja de texto para mostrar el resultado en tiempo real
        self.lbl_resultado_acceso = tk.Label(
            frame_acceso, 
            text="Esperando matrícula...", 
            font=("Arial", 10, "italic"), 
            fg="gray",
            wraplength=550,
            justify="left"
        )
        self.lbl_resultado_acceso.grid(row=1, column=0, columnspan=3, sticky="w", pady=10)

        # 3. SECCIÓN: ANÁLISIS INTELIGENTE (Fases 7 y 8)
        frame_analisis = tk.LabelFrame(self.ventana, text=" Módulos Avanzados (IA & Sustentabilidad) ", font=("Arial", 11, "bold"), padx=15, pady=15)
        frame_analisis.pack(fill="x", padx=20, pady=10)

        # Botón Predicción (Fase 7)
        btn_predecir = tk.Button(
            frame_analisis, 
            text="🔮 Analizar Riesgo Tráfico", 
            font=("Arial", 10), 
            command=self.mostrar_prediccion
        )
        btn_predecir.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        # Botón Sustentabilidad (Fase 8)
        btn_sustentable = tk.Button(
            frame_analisis, 
            text="🌱 Evaluar Eco-Sustentabilidad", 
            font=("Arial", 10), 
            command=self.mostrar_sustentabilidad
        )
        btn_sustentable.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Área de resultados del análisis
        self.txt_reporte_avanzado = tk.Text(frame_analisis, height=6, width=65, font=("Courier", 10), state="disabled", bg="#f7fafc")
        self.txt_reporte_avanzado.grid(row=1, column=0, columnspan=2, pady=10)

        # Pie de página
        lbl_footer = tk.Label(self.ventana, text="Universidad Politécnica de Guanajuato", font=("Arial", 8), fg="gray")
        lbl_footer.pack(side="bottom", pady=10)

    # LÓGICA DE INTERACCIÓN
    def procesar_validacion(self):
        matricula = self.entrada_matricula.get().strip().upper()
        
        if not matricula:
            messagebox.showwarning("Campo Vacío", "Por favor, ingresa una matrícula válida.")
            return

        # Procesamos en el cerebro de SmartGate
        registro = self.gate.procesar_acceso(matricula)
        
        # Cambiamos colores según el veredicto
        if registro.autorizado:
            self.lbl_resultado_acceso.config(text=f"✅ {registro.motivo}", fg="green", font=("Arial", 10, "bold"))
        else:
            self.lbl_resultado_acceso.config(text=f"❌ {registro.motivo}", fg="red", font=("Arial", 10, "bold"))
        
        # Limpiamos la caja para una nueva entrada
        self.entrada_matricula.delete(0, tk.END)

    def mostrar_prediccion(self):
        res = self.prediccion.analizar()
        
        self.txt_reporte_avanzado.config(state="normal")
        self.txt_reporte_avanzado.delete("1.0", tk.END)
        
        if isinstance(res, str):
            self.txt_reporte_avanzado.insert(tk.END, res)
        else:
            reporte_texto = (
                f"REPORTE PREDICTIVO DE TRÁFICO\n"
                f"• Hora pico estimada   : {res['hora_pico']}\n"
                f"• Volumen de Vehiculos : {res['vehiculos']} accesos detectados\n"
                f"• Nivel de riesgo      : {res['riesgo']}\n"
                f"====================================="
            )
            self.txt_reporte_avanzado.insert(tk.END, reporte_texto)
            
        self.txt_reporte_avanzado.config(state="disabled")

    def mostrar_sustentabilidad(self):
        res = self.sustentabilidad.evaluar()
        
        self.txt_reporte_avanzado.config(state="normal")
        self.txt_reporte_avanzado.delete("1.0", tk.END)
        
        reporte_texto = (
            f"EVALUACIÓN ECO-SUSTENTABLE\n"
            f"• Tiempo promedio en barrera : {res['tiempo']} segundos\n"
            f"• Diagnostico ambiental   : {res['estado']}\n"
            f"• Objetivo del sistema    : Minimizar el CO2\n"
            f"=================================="
        )
        self.txt_reporte_avanzado.insert(tk.END, reporte_texto)
        self.txt_reporte_avanzado.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartGateGUI(root)
    root.mainloop()