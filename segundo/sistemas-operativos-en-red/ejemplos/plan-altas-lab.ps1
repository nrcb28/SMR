# Genera un plan de altas sintéticas. Nunca crea, borra ni modifica objetos.
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateScript({ Test-Path -LiteralPath $_ -PathType Leaf })]
    [string]$Csv,
    [switch]$ConsultarDirectorio
)

$ErrorActionPreference = 'Stop'
$filas = @(Import-Csv -LiteralPath $Csv -Delimiter ';' -Encoding UTF8)
if ($filas.Count -eq 0) { throw 'El CSV no contiene filas.' }
$vistos = @{}
$plan = @()

if ($ConsultarDirectorio) {
    Import-Module ActiveDirectory -ErrorAction Stop
    $dominio = Get-ADDomain -Server 'dc01.ad.aula.test'
    if ($dominio.DNSRoot -ne 'ad.aula.test') {
        throw 'La consulta no corresponde al dominio ficticio esperado.'
    }
}

foreach ($fila in $filas) {
    if ($null -eq $fila.Alias -or $null -eq $fila.Nombre -or $null -eq $fila.Grupo) {
        throw 'Faltan columnas Alias, Nombre o Grupo.'
    }
    $aliasLab = $fila.Alias.Trim().ToLowerInvariant()
    $nombreLab = $fila.Nombre.Trim()
    $grupoLab = $fila.Grupo.Trim()
    if ($aliasLab -notmatch '^[a-z][a-z0-9._-]{2,19}$') {
        throw ('Alias no admitido: ' + $aliasLab)
    }
    if ([string]::IsNullOrWhiteSpace($nombreLab) -or $nombreLab.Length -gt 80) {
        throw ('Nombre vacío o excesivo para: ' + $aliasLab)
    }
    if ($grupoLab -notmatch '^GG_LAB_[A-Za-z0-9_-]+$') {
        throw ('Grupo fuera del prefijo de laboratorio: ' + $grupoLab)
    }
    if ($vistos.ContainsKey($aliasLab)) {
        throw ('Alias duplicado: ' + $aliasLab)
    }
    $vistos[$aliasLab] = $true
    $estado = 'Pendiente de consulta y revisión'
    if ($ConsultarDirectorio) {
        # Se usa un filtro de script con valor validado; no se evalúa código del CSV.
        $existente = Get-ADUser -Filter { SamAccountName -eq $aliasLab } `
            -Server 'dc01.ad.aula.test'
        $estado = if ($existente) { 'Ya existe: revisar, no recrear' } else { 'No localizado' }
    }
    $plan += [PSCustomObject]@{
        Alias = $aliasLab
        Nombre = $nombreLab
        GrupoPropuesto = $grupoLab
        Dominio = 'ad.aula.test'
        Accion = 'Propuesta: crear cuenta deshabilitada y revisar pertenencia'
        Estado = $estado
    }
}

$plan
