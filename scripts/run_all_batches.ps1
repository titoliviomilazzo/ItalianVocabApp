# =============================================================
# Gemini/Imagen API Image Batch Generation - batch5 ~ batch142
# =============================================================
# Usage:
#   $env:GEMINI_API_KEY = "your_key"
#   cd "J:\my drive\Code\ItalianVocabApp\scripts"
#   .\run_all_batches.ps1
#   .\run_all_batches.ps1 -UseImagen -Fallback
#   .\run_all_batches.ps1 -StartBatch 10 -EndBatch 20
# =============================================================

param(
    [int]$StartBatch = 5,
    [int]$EndBatch = 142,
    [float]$Delay = 5,
    [int]$Retry = 3,
    [switch]$UseImagen,
    [switch]$Fallback
)

$ProjectDir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$ScriptPath = Join-Path $ProjectDir "scripts\generate_images_gemini.py"

# Check API key
if (-not $env:GEMINI_API_KEY) {
    Write-Host "[ERROR] API key not set!" -ForegroundColor Red
    Write-Host '  $env:GEMINI_API_KEY = "your_api_key_here"' -ForegroundColor Yellow
    Write-Host "  Get key at: https://aistudio.google.com/apikey" -ForegroundColor Cyan
    exit 1
}

$modelLabel = if ($UseImagen) { "imagen-3.0-generate-002" } else { "gemini-2.5-flash-image" }
if ($Fallback) { $modelLabel += " (+fallback)" }

Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host "[START] Gemini Image Batch Generation" -ForegroundColor Green
Write-Host ("  Range: batch{0} ~ batch{1}" -f $StartBatch, $EndBatch) -ForegroundColor White
Write-Host ("  Model: {0}" -f $modelLabel) -ForegroundColor White
Write-Host ("  Delay: {0}s" -f $Delay) -ForegroundColor White
Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host ""

$totalBatches = $EndBatch - $StartBatch + 1
$completedBatches = 0
$failedBatches = @()
$overallStart = Get-Date

for ($i = $StartBatch; $i -le $EndBatch; $i++) {
    $promptFile = Join-Path $ProjectDir ("genspark_prompts_batch{0}.txt" -f $i)
    $outputDir = Join-Path $ProjectDir ("assets\images\batch{0}" -f $i)

    # Check file exists
    if (-not (Test-Path $promptFile)) {
        Write-Host ("[SKIP] batch{0}: prompt file not found" -f $i) -ForegroundColor Yellow
        continue
    }

    $completedBatches++
    Write-Host "-------------------------------------------" -ForegroundColor DarkGray
    Write-Host ("[{0}/{1}] Processing batch{2}..." -f $completedBatches, $totalBatches, $i) -ForegroundColor Cyan
    Write-Host ("  Input: genspark_prompts_batch{0}.txt" -f $i) -ForegroundColor DarkGray
    Write-Host ("  Output: assets/images/batch{0}/" -f $i) -ForegroundColor DarkGray

    $batchStart = Get-Date

    $extraArgs = @()
    if ($UseImagen) { $extraArgs += "--use-imagen" }
    if ($Fallback) { $extraArgs += "--fallback" }

    python $ScriptPath `
        --prompt-file $promptFile `
        --output-dir $outputDir `
        --delay $Delay `
        --retry $Retry `
        @extraArgs

    $exitCode = $LASTEXITCODE
    $batchElapsed = (Get-Date) - $batchStart
    $mins = [math]::Round($batchElapsed.TotalMinutes, 1)

    if ($exitCode -ne 0) {
        Write-Host ("  [WARN] batch{0} error (exit code: {1})" -f $i, $exitCode) -ForegroundColor Red
        $failedBatches += $i
    }
    else {
        Write-Host ("  [OK] batch{0} done ({1} min)" -f $i, $mins) -ForegroundColor Green
    }

    # Wait 10s between batches to avoid rate limit
    if ($i -lt $EndBatch) {
        Write-Host "  Waiting 10s before next batch..." -ForegroundColor DarkGray
        Start-Sleep -Seconds 10
    }
}

# Summary
$overallElapsed = (Get-Date) - $overallStart
$hours = [math]::Round($overallElapsed.TotalHours, 1)

Write-Host ""
Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host "[DONE] All batches finished!" -ForegroundColor Green
Write-Host ("  Total time: {0} hours" -f $hours) -ForegroundColor White
Write-Host ("  Batches processed: {0}" -f $completedBatches) -ForegroundColor White

if ($failedBatches.Count -gt 0) {
    $failedList = $failedBatches -join ', '
    Write-Host ("  [WARN] Failed batches: {0}" -f $failedList) -ForegroundColor Red
    Write-Host "  To retry failed batches:" -ForegroundColor Yellow
    foreach ($fb in $failedBatches) {
        Write-Host ("    .\run_all_batches.ps1 -StartBatch {0} -EndBatch {0}" -f $fb) -ForegroundColor Yellow
    }
}
else {
    Write-Host "  All batches successful!" -ForegroundColor Green
}
Write-Host "=============================================================" -ForegroundColor Cyan
