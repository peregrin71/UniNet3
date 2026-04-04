param(
    [string]$InputDir = "$(Join-Path $PSScriptRoot '..\papers\paper1')",
    [string]$OutputFile = "$(Join-Path $PSScriptRoot '..\papers\paper1\paper1.md')"
)

$ErrorActionPreference = 'Stop'

$resolvedInputDir = (Resolve-Path $InputDir).Path
$resolvedOutputFile = [System.IO.Path]::GetFullPath($OutputFile)
$outputName = [System.IO.Path]::GetFileName($resolvedOutputFile)

function Read-MarkdownFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    $utf8 = New-Object System.Text.UTF8Encoding($false, $true)
    $reader = New-Object System.IO.StreamReader($Path, $utf8, $true)

    try {
        return $reader.ReadToEnd()
    }
    finally {
        $reader.Dispose()
    }
}

if (-not (Test-Path $resolvedInputDir)) {
    throw "Input directory does not exist: $resolvedInputDir"
}

$sourceFiles = Get-ChildItem -Path $resolvedInputDir -File -Filter '*.md' |
    Where-Object {
        $_.Name -ne $outputName -and
        $_.Name -notmatch '^uninet_paper_v[\d\.]+\.md$'
    } |
    Sort-Object Name

if ($sourceFiles.Count -eq 0) {
    throw "No source markdown files found in: $resolvedInputDir"
}

$sb = New-Object System.Text.StringBuilder

for ($i = 0; $i -lt $sourceFiles.Count; $i++) {
    $file = $sourceFiles[$i]
    $content = Read-MarkdownFile -Path $file.FullName
    $content = [System.Text.RegularExpressions.Regex]::Replace(
        $content,
        '(?m)^<!--\s*(BEGIN|END): .*?-->\s*\r?\n?',
        ''
    )

    [void]$sb.AppendLine($content.TrimEnd())

    if ($i -lt $sourceFiles.Count - 1) {
        [void]$sb.AppendLine()
        [void]$sb.AppendLine('---')
        [void]$sb.AppendLine()
    }
}

$parentDir = Split-Path -Parent $resolvedOutputFile
if (-not (Test-Path $parentDir)) {
    New-Item -Path $parentDir -ItemType Directory | Out-Null
}

[System.IO.File]::WriteAllText($resolvedOutputFile, $sb.ToString(), [System.Text.Encoding]::UTF8)

Write-Host "Merged $($sourceFiles.Count) files into: $resolvedOutputFile"
