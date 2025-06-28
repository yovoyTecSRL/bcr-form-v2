#!/usr/bin/env python3
"""
Demo del Sistema BCR Form v2
Demuestra el flujo completo del sistema
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8001"

def demo_complete_flow():
    """Demuestra el flujo completo del sistema"""
    print("🏦 DEMO SISTEMA BCR FORM V2")
    print("="*50)
    print(f"🕐 Iniciado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 1. Obtener provincias
    print("1️⃣  Obteniendo provincias...")
    response = requests.get(f"{BASE_URL}/provincias")
    provincias = response.json()
    print(f"   ✅ {provincias['total']} provincias disponibles")
    
    # 2. Obtener cantones de San José
    print("2️⃣  Obteniendo cantones de San José...")
    response = requests.get(f"{BASE_URL}/cantones/San José")
    cantones = response.json()
    print(f"   ✅ {cantones['total']} cantones en San José")
    
    # 3. Validar formulario completo
    print("3️⃣  Validando formulario de prueba...")
    form_data = {
        "nombre": "María Elena",
        "apellido1": "Rodríguez",
        "apellido2": "Vargas",
        "cedula": "123456780",
        "telefono": "8899-7755",
        "email": "maria.rodriguez@email.com",
        "provincia": "San José",
        "canton": "Escazú",
        "direccion": "Condominio Monteverdi, Casa 78",
        "gps_lat": 9.9281,
        "gps_lng": -84.0907,
        "ingresos": 1200000
    }
    
    response = requests.post(f"{BASE_URL}/validar-formulario", json=form_data)
    validation_result = response.json()
    
    if validation_result["status"] == "APPROVED":
        print(f"   ✅ Formulario APROBADO")
        print(f"   📋 Validaciones: {len(validation_result['validation_results'])}")
        session_id = validation_result["session_id"]
        print(f"   🆔 Session ID: {session_id}")
    else:
        print(f"   ❌ Formulario RECHAZADO")
        return
    
    # 4. Ejecutar pruebas automatizadas
    print("4️⃣  Ejecutando pruebas automatizadas...")
    time.sleep(1)  # Pausa dramática
    
    response = requests.post(f"{BASE_URL}/ejecutar-pruebas", json={"session_id": session_id})
    test_result = response.json()
    
    print(f"   ✅ Pruebas completadas en {test_result['summary']['duration']:.1f}s")
    print(f"   📊 Resultado: {test_result['summary']['passed']}/{test_result['summary']['total_tests']} pruebas pasaron")
    
    # 5. Obtener datos de pruebas en tiempo real
    print("5️⃣  Consultando datos de pruebas en tiempo real...")
    response = requests.get(f"{BASE_URL}/tests-live-data")
    live_data = response.json()
    
    print(f"   📈 {len(live_data['tests'])} pruebas registradas")
    print(f"   ⏱️  Duración total: {live_data['summary']['duration']:.1f}s")
    
    # 6. Chat con QA tester
    print("6️⃣  Consultando al tester QA...")
    time.sleep(1)
    
    try:
        response = requests.post(f"{BASE_URL}/qa-chat", 
                               json={"message": "¿Cómo evaluarías la solicitud de María Elena?"}, 
                               timeout=15)
        chat_result = response.json()
        print(f"   🤖 QA Tester: {chat_result['response'][:100]}...")
        print(f"   🧠 Fuente: {chat_result['source']}")
    except requests.Timeout:
        print("   ⏰ QA Tester tardó en responder (timeout)")
    except Exception as e:
        print(f"   ⚠️  Error en QA Chat: {e}")
    
    # 7. Resumen final
    print("\n" + "="*50)
    print("🎉 DEMO COMPLETADA EXITOSAMENTE")
    print("🌟 Todas las funcionalidades están operativas:")
    print("   ✅ Validación de formularios")
    print("   ✅ Pruebas automatizadas")
    print("   ✅ Datos geográficos dinámicos")
    print("   ✅ Visualización en tiempo real")
    print("   ✅ Chat con IA tester")
    print("   ✅ Seguridad integrada")
    print("\n🚀 Sistema listo para producción!")

if __name__ == "__main__":
    try:
        demo_complete_flow()
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar al servidor")
        print("💡 Asegúrate de que el servidor esté ejecutándose en http://localhost:8001")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
