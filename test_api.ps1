# Script para probar la API de Kids ABB

Write-Host "`n=== Probando API Kids ABB ===" -ForegroundColor Cyan

# 1. Health Check
Write-Host "`n1. Health Check:" -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:8000/health" -Method GET
Write-Host $response.Content -ForegroundColor Green

# 2. Agregar niño - Ana
Write-Host "`n2. Agregar niño - Ana (8 años):" -ForegroundColor Yellow
$body = @{
    name = "Ana"
    age = 8
} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/add" -Method POST -ContentType "application/json" -Body $body
Write-Host $response.Content -ForegroundColor Green

# 3. Agregar niño - Carlos
Write-Host "`n3. Agregar niño - Carlos (10 años):" -ForegroundColor Yellow
$body = @{
    name = "Carlos"
    age = 10
} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/add" -Method POST -ContentType "application/json" -Body $body
Write-Host $response.Content -ForegroundColor Green

# 4. Agregar niño - Beatriz
Write-Host "`n4. Agregar niño - Beatriz (7 años):" -ForegroundColor Yellow
$body = @{
    name = "Beatriz"
    age = 7
} | ConvertTo-Json
$response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/add" -Method POST -ContentType "application/json" -Body $body
Write-Host $response.Content -ForegroundColor Green

# 5. Listar todos los niños
Write-Host "`n5. Listar todos los niños:" -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/list" -Method GET
Write-Host $response.Content -ForegroundColor Green

# 6. Obtener estadísticas del árbol
Write-Host "`n6. Estadísticas del árbol:" -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/stats" -Method GET
Write-Host $response.Content -ForegroundColor Green

# 7. Obtener un niño específico por ID (usando ID 1)
Write-Host "`n7. Obtener niño con ID 1:" -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/1" -Method GET
    Write-Host $response.Content -ForegroundColor Green
} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}

# 8. Eliminar un niño (ID 2)
Write-Host "`n8. Eliminar niño con ID 2:" -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/2" -Method DELETE
    Write-Host $response.Content -ForegroundColor Green
} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}

# 9. Verificar que se eliminó
Write-Host "`n9. Listar niños después de eliminar:" -ForegroundColor Yellow
$response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/kids/list" -Method GET
Write-Host $response.Content -ForegroundColor Green

Write-Host "`n=== Pruebas completadas ===" -ForegroundColor Cyan
Write-Host "`nPara ver la documentación interactiva, abre: http://localhost:8000/docs" -ForegroundColor Magenta
Write-Host "Nota: Los IDs ahora son cortos y secuenciales (1, 2, 3, ...)" -ForegroundColor Yellow
