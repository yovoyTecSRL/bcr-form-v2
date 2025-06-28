#!/usr/bin/env python3
"""
Script de prueba integral del sistema BCR Form v2
Prueba todos los endpoints y funcionalidades principales
"""

import requests
import json
import time
from typing import Dict, Any, Optional

BASE_URL = "http://localhost:8001"

def test_endpoint(endpoint: str, method: str = "GET", data: Optional[Dict[Any, Any]] = None) -> bool:
    """Prueba un endpoint específico"""
    try:
        url = f"{BASE_URL}{endpoint}"
        print(f"🧪 Probando {method} {endpoint}...")
        
        if method == "GET":
            response = requests.get(url, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=10)
        else:
            print(f"❌ Método {method} no soportado")
            return False
            
        if response.status_code == 200:
            print(f"✅ {endpoint} - OK")
            return True
        else:
            print(f"❌ {endpoint} - Error {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ {endpoint} - Excepción: {e}")
        return False

def main():
    """Ejecuta todas las pruebas"""
    print("🚀 Iniciando pruebas integrales del sistema BCR Form v2\n")
    
    tests_passed = 0
    tests_total = 0
    
    # Prueba 1: Página principal
    tests_total += 1
    if test_endpoint("/"):
        tests_passed += 1
    
    # Prueba 2: Provincias
    tests_total += 1
    if test_endpoint("/provincias"):
        tests_passed += 1
    
    # Prueba 3: Cantones
    tests_total += 1
    if test_endpoint("/cantones/San José"):
        tests_passed += 1
    
    # Prueba 4: Validar formulario
    tests_total += 1
    form_data = {
        "nombre": "Ana María",
        "apellido1": "López",
        "apellido2": "Herrera",
        "cedula": "123456780",
        "telefono": "8777-6666",
        "email": "ana@example.com",
        "provincia": "San José",
        "canton": "Escazú",
        "direccion": "Residencial Los Laureles, Casa 45",
        "gps_lat": 9.9281,
        "gps_lng": -84.0907,
        "ingresos": 950000
    }
    
    if test_endpoint("/validar-formulario", "POST", form_data):
        tests_passed += 1
        session_id = "test_session"  # En una implementación real, extraeríamos del response
        
        # Prueba 5: Ejecutar pruebas
        tests_total += 1
        if test_endpoint("/ejecutar-pruebas", "POST", {"session_id": session_id}):
            tests_passed += 1
    else:
        tests_total += 1  # Cuenta la prueba de ejecutar-pruebas como fallida
    
    # Prueba 6: Datos de pruebas en tiempo real
    tests_total += 1
    if test_endpoint("/tests-live-data"):
        tests_passed += 1
    
    # Prueba 7: Chat QA
    tests_total += 1
    chat_data = {
        "message": "¿Cómo van las pruebas del sistema?"
    }
    if test_endpoint("/qa-chat", "POST", chat_data):
        tests_passed += 1
    
    # Prueba 8: Historial del chat
    tests_total += 1
    if test_endpoint("/qa-chat-history"):
        tests_passed += 1
    
    # Prueba 9: Página de pruebas en tiempo real
    tests_total += 1
    if test_endpoint("/tests-live"):
        tests_passed += 1
    
    # Resultados finales
    print(f"\n📊 RESULTADOS FINALES:")
    print(f"✅ Pruebas exitosas: {tests_passed}/{tests_total}")
    print(f"❌ Pruebas fallidas: {tests_total - tests_passed}/{tests_total}")
    
    success_rate = (tests_passed / tests_total) * 100
    print(f"📈 Tasa de éxito: {success_rate:.1f}%")
    
    if success_rate >= 90:
        print("🎉 ¡Sistema funcionando correctamente!")
    elif success_rate >= 70:
        print("⚠️  Sistema funcional con algunos problemas menores")
    else:
        print("🚨 Sistema tiene problemas significativos")
    
    return success_rate >= 70

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
