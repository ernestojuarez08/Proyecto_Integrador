import json
import os
from datetime import datetime
from config import REGISTROS_JSON

# Importaciones de ReportLab para armar el PDF estructurado
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

class GeneradorReportes:
    def __init__(self, archivo_json=REGISTROS_JSON):
        self.archivo_json = archivo_json

    def cargar_datos(self):
        try:
            with open(self.archivo_json, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def generar_pdf(self, nombre_salida="Reporte_Accesos_SmartGate.pdf"):
        registros = self.cargar_datos()
        
        if not registros:
            return False, "No hay registros disponibles para exportar."

        # 1. Configuración del documento básico
        doc = SimpleDocTemplate(
            nombre_salida,
            pagesize=letter,
            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
        )
        
        story = []
        styles = getSampleStyleSheet()

        # Estilos personalizados
        style_title = ParagraphStyle(
            'TituloReporte',
            parent=styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=24,
            leading=28,
            textColor=colors.HexColor('#1A365D'),
            spaceAfter=6
        )
        
        style_subtitle = ParagraphStyle(
            'SubTituloReporte',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            textColor=colors.HexColor('#4A5568'),
            spaceAfter=20
        )

        style_cell = ParagraphStyle(
            'CeldaTabla',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=9,
            leading=11
        )

        style_cell_header = ParagraphStyle(
            'HeaderTabla',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=12,
            textColor=colors.white
        )

        # 2. Encabezado del PDF
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        story.append(Paragraph("SMARTGATE IA — REPORTE DE ACCESOS", style_title))
        story.append(Paragraph(f"Historial consolidado de accesos vehiculares | Generado el: {fecha_actual}", style_subtitle))
        story.append(Spacer(1, 10))

        # 3. Diseño y construcción de la Tabla
        # Encabezados de las columnas
        data_tabla = [[
            Paragraph("Fecha y Hora", style_cell_header),
            Paragraph("Matrícula", style_cell_header),
            Paragraph("Estado", style_cell_header),
            Paragraph("Motivo / Detalles", style_cell_header)
        ]]

        # Llenamos la tabla con el historial (últimos 50 registros para no saturar el PDF si es masivo)
        for r in registros[-50:]:  
            estado_texto = "AUTORIZADO" if r.get("autorizado") else "RECHAZADO"
            
            data_tabla.append([
                Paragraph(r.get("fecha_hora", "N/A"), style_cell),
                Paragraph(r.get("matricula", "N/A"), style_cell),
                Paragraph(estado_texto, style_cell),
                Paragraph(r.get("motivo", "N/A"), style_cell)
            ])

        # Anchos de columna fijos para tamaño Carta (Total 530 puntos disponibles)
        tabla_reporte = Table(data_tabla, colWidths=[120, 80, 80, 250])

        # Estilos visuales de la tabla (Colores institucionales UPG)
        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1A365D')), # Azul obscuro arriba
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')), # Bordes grises finos
        ])

        # Alternar colores en las filas para mejorar la lectura
        for i in range(1, len(data_tabla)):
            if i % 2 == 0:
                estilo_tabla.add('BACKGROUND', (0, i), (-1, i), colors.HexColor('#F7FAFC'))
            
            # Si fue rechazado, poner el texto de la celda de estado en un tono rojo sutil
            if data_tabla[i][2].text == "RECHAZADO":
                estilo_tabla.add('TEXTCOLOR', (2, i), (2, i), colors.HexColor('#C53030'))

        tabla_reporte.setStyle(estilo_tabla)
        story.append(tabla_reporte)

        # 4. Construcción final
        doc.build(story)
        return True, f"Reporte exportado exitosamente como: {nombre_salida}"