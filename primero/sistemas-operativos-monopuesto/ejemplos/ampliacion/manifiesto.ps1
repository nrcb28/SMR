# Manifiesto de un árbol sintético de Windows: consulta origen, escribe sólo salida.
# Compatible con Windows PowerShell 5.1 y PowerShell 7 para este contrato.
param(
    [Parameter(Mandatory = $true)][string]$Origen,
    [Parameter(Mandatory = $true)][string]$Salida
)

$ErrorActionPreference = 'Stop'
$bloqueo = $null
$temporal = $null
$temporalCreado = $false

try {
    $origenObjeto = Get-Item -LiteralPath $Origen -Force
    $salidaObjeto = Get-Item -LiteralPath $Salida -Force
    if (-not $origenObjeto.PSIsContainer -or -not $salidaObjeto.PSIsContainer) {
        throw 'Origen y salida deben ser directorios existentes.'
    }
    if (($origenObjeto.Attributes -band [IO.FileAttributes]::ReparsePoint) -or
        ($salidaObjeto.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
        throw 'Las carpetas raíz no pueden ser enlaces ni puntos de análisis.'
    }

    $baseOrigen = $origenObjeto.FullName.TrimEnd([IO.Path]::DirectorySeparatorChar)
    $baseSalida = $salidaObjeto.FullName.TrimEnd([IO.Path]::DirectorySeparatorChar)
    $prefijoOrigen = $baseOrigen + [IO.Path]::DirectorySeparatorChar
    $prefijoSalida = $baseSalida + [IO.Path]::DirectorySeparatorChar
    if ($prefijoSalida.StartsWith($prefijoOrigen, [StringComparison]::OrdinalIgnoreCase)) {
        throw 'La salida no puede ser el origen ni estar dentro de él.'
    }

    $rutaBloqueo = Join-Path $baseSalida '.manifiesto.lock'
    $bloqueo = [IO.File]::Open($rutaBloqueo, [IO.FileMode]::OpenOrCreate,
        [IO.FileAccess]::ReadWrite, [IO.FileShare]::None)

    $pendientes = New-Object 'System.Collections.Generic.Queue[System.IO.DirectoryInfo]'
    $pendientes.Enqueue($origenObjeto)
    $filas = New-Object 'System.Collections.Generic.List[object]'
    while ($pendientes.Count -gt 0) {
        $directorio = $pendientes.Dequeue()
        foreach ($elemento in Get-ChildItem -LiteralPath $directorio.FullName -Force) {
            if ($elemento.Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw 'El árbol contiene un enlace o punto de análisis: revisar el alcance.'
            }
            if ($elemento.PSIsContainer) {
                $pendientes.Enqueue($elemento)
                continue
            }
            $hash = Get-FileHash -LiteralPath $elemento.FullName -Algorithm SHA256
            $filas.Add([PSCustomObject]@{
                Ruta = $elemento.FullName.Substring($prefijoOrigen.Length)
                Bytes = $elemento.Length
                SHA256 = $hash.Hash
            })
        }
    }
    if ($filas.Count -eq 0) {
        throw 'No hay archivos regulares; se conserva el manifiesto anterior.'
    }

    $temporal = Join-Path $baseSalida ('.manifiesto-' + [Guid]::NewGuid().ToString('N') + '.tmp')
    New-Item -ItemType File -Path $temporal | Out-Null
    $temporalCreado = $true
    $filas | Sort-Object Ruta | Export-Csv -LiteralPath $temporal -NoTypeInformation -Encoding UTF8
    $publicado = Join-Path $baseSalida 'manifiesto.csv'
    if ([IO.File]::Exists($publicado)) {
        [IO.File]::Replace($temporal, $publicado, $null)
    }
    else {
        [IO.File]::Move($temporal, $publicado)
    }
    $temporalCreado = $false
    Write-Output ('UTC={0} archivos={1} resultado=correcto' -f
        [DateTime]::UtcNow.ToString('o'), $filas.Count)
}
catch {
    Write-Error ('Manifiesto no publicado: ' + $_.Exception.Message) -ErrorAction Continue
    exit 1
}
finally {
    if ($temporalCreado -and $temporal -and [IO.File]::Exists($temporal)) {
        Remove-Item -LiteralPath $temporal -Force
    }
    if ($bloqueo) {
        $bloqueo.Dispose()
    }
}
