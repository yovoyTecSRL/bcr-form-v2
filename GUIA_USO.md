# 🚀 GUÍA DE USO - SISTEMA BCR FORM V2

## 📋 INICIO RÁPIDO

### 1. Iniciar el Sistema
```bash
cd /workspaces/bcr-form-v2
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### 2. Acceder a la Aplicación
- **URL Principal**: http://localhost:8001
- **Visor de Pruebas**: http://localhost:8001/tests-live

## 🎯 FUNCIONALIDADES PRINCIPALES

### 📝 Formulario de Solicitud
1. **Datos Personales**
   - Nombre completo (mínimo 2 palabras)
   - Cédula costarricense (formato 123456789)
   - Teléfono (8888-7777 o 88887777)
   - Email válido

2. **Información de Dirección**
   - Provincia (dropdown dinámico)
   - Cantón (dropdown dinámico basado en provincia)
   - Dirección específica

3. **Ubicación GPS** (Opcional)
   - Coordenadas de Costa Rica
   - Latitud: 8-11 grados Norte
   - Longitud: -87 a -82 grados Oeste

4. **Información Financiera**
   - Ingresos mensuales en colones

### 🧪 Pruebas Automatizadas
- **Pruebas de Formulario**: Validación de campos
- **Pruebas de Seguridad**: XSS, SQL Injection
- **Pruebas de Rendimiento**: Tiempo de respuesta
- **Total**: 9 casos de prueba automatizados

### 🤖 Chat QA con IA
- Análisis inteligente de solicitudes
- Respuestas contextuales basadas en pruebas
- Historial de conversaciones
- Integración con GPT-4

### 📊 Visualización en Tiempo Real
- Monitor de pruebas ejecutándose
- Resultados en tiempo real
- Estadísticas de rendimiento

## 🔧 ENDPOINTS DE API

### GET Endpoints
```bash
GET /                    # Página principal
GET /provincias          # Lista de provincias CR
GET /cantones/{provincia} # Cantones por provincia
GET /tests-live          # Página visor de pruebas
GET /tests-live-data     # Datos de pruebas (JSON)
GET /qa-chat-history     # Historial del chat
```

### POST Endpoints
```bash
POST /validar-formulario # Validar formulario completo
POST /ejecutar-pruebas   # Ejecutar suite de pruebas
POST /qa-chat           # Chat con tester QA
```

## 📝 EJEMPLOS DE USO

### Validar Formulario
```bash
curl -X POST "http://localhost:8001/validar-formulario" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Ana María",
    "apellido1": "González",
    "apellido2": "López",
    "cedula": "123456780",
    "telefono": "8888-7777",
    "email": "ana@example.com",
    "provincia": "San José",
    "canton": "Central",
    "direccion": "Calle 1, Casa 123",
    "gps_lat": 9.9281,
    "gps_lng": -84.0907,
    "ingresos": 850000
  }'
```

### Ejecutar Pruebas
```bash
curl -X POST "http://localhost:8001/ejecutar-pruebas" \
  -H "Content-Type: application/json" \
  -d '{"session_id": "SESSION_ID_AQUÍ"}'
```

### Chat con QA
```bash
curl -X POST "http://localhost:8001/qa-chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "¿Cómo están las pruebas?"}'
```

## 🛠️ COMANDOS ÚTILES

### Pruebas del Sistema
```bash
# Prueba integral completa
python demo_system.py

# Pruebas automatizadas
python test_integration.py

# Verificar endpoints
curl "http://localhost:8001/provincias"
curl "http://localhost:8001/tests-live-data"
```

### Monitoreo
```bash
# Ver logs del servidor
tail -f logs/app.log  # (si está configurado)

# Verificar estado del servidor
curl -s "http://localhost:8001/" | head -5

# Estadísticas de pruebas
curl -s "http://localhost:8001/tests-live-data" | jq '.summary'
```

## 🎨 INTERFAZ DE USUARIO

### Flujo del Formulario
1. **Paso 1**: Datos Personales
   - Validación en tiempo real
   - Mensajes de error claros

2. **Paso 2**: Dirección
   - Dropdowns dinámicos
   - Validación de provincia/cantón

3. **Paso 3**: GPS (Opcional)
   - Coordenadas automáticas o manuales
   - Validación de rango para Costa Rica

4. **Paso 4**: Revisión
   - Resumen de todos los datos
   - Botón de envío final

### Botones Especiales
- **"Ver pruebas IA en tiempo real"**: Abre visor de pruebas
- **"Conversar con el tester QA"**: Abre chat modal

## 🔒 SEGURIDAD

### Protecciones Implementadas
- **XSS Prevention**: Sanitización de HTML
- **SQL Injection**: Escape de caracteres
- **Rate Limiting**: 50 requests/minuto por IP
- **Input Validation**: Validación estricta de tipos
- **CORS**: Headers de seguridad

### Validaciones de Datos
- **Nombres**: Solo letras y espacios, mínimo 2 palabras
- **Cédula**: Formato CR con dígito verificador
- **Teléfono**: Formatos CR válidos
- **Email**: RFC compliant
- **GPS**: Coordenadas válidas para Costa Rica

## 🚨 SOLUCIÓN DE PROBLEMAS

### Error: Servidor no responde
```bash
# Verificar que el servidor esté ejecutándose
ps aux | grep uvicorn

# Reiniciar servidor
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### Error: Cédula no válida
- Usar formato: 123456789 (9 dígitos)
- O con guiones: 1-2345-6789
- Verificar dígito verificador

### Error: Chat QA no responde
- Verificar que .env tiene OPENAI_API_KEY
- El chat puede tardar 10-15 segundos con GPT-4
- Fallback automático si API no disponible

### Error: Formulario rechazado
- Verificar todos los campos requeridos
- Comprobar formato de datos (teléfono, email)
- Revisar que provincia y cantón sean válidos

## 📈 MÉTRICAS Y MONITOREO

### Indicadores Clave
- **Tasa de aprobación**: % de formularios aprobados
- **Tiempo de respuesta**: Promedio < 2 segundos
- **Pruebas pasadas**: 8/9 típicamente (88.9%)
- **Disponibilidad**: 99.9% uptime esperado

### Logs Importantes
- Validaciones fallidas
- Errores de cédula
- Intentos de inyección detectados
- Límites de rate exceeded

---

**📞 SOPORTE**: Para dudas técnicas, revisar logs del servidor o contactar al equipo de desarrollo.
