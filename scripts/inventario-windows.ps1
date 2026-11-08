# Consultas locales; no cambia configuración ni política de ejecución.
$ErrorActionPreference = 'Stop'

try {
    $sistema = Get-CimInstance Win32_OperatingSystem
    $equipo = Get-CimInstance Win32_ComputerSystem
    $procesadores = @(Get-CimInstance Win32_Processor | ForEach-Object {
        [PSCustomObject]@{
            Modelo = $_.Name
            Nucleos = $_.NumberOfCores
            ProcesadoresLogicos = $_.NumberOfLogicalProcessors
        }
    })
    $discos = @(Get-CimInstance Win32_DiskDrive | ForEach-Object {
        [PSCustomObject]@{
            Indice = $_.Index
            Modelo = $_.Model
            TamanoGiB = [Math]::Round($_.Size / 1GB, 2)
        }
    })

    [PSCustomObject]@{
        Sistema = $sistema.Caption
        Version = $sistema.Version
        Compilacion = $sistema.BuildNumber
        MemoriaGiB = [Math]::Round($equipo.TotalPhysicalMemory / 1GB, 2)
        CPU = $procesadores
        Discos = $discos
        Nota = 'Consultas sin números de serie, cuentas ni direcciones de red. Revisa antes de compartir.'
    } | ConvertTo-Json -Depth 5
}
catch {
    Write-Error ('No se pudo completar el inventario CIM: ' + $_.Exception.Message) -ErrorAction Continue
    exit 1
}
