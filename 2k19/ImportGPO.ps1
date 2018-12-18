param
(
    [Parameter(Mandatory)]
    [String]$domain
)

Foreach ($piece in $domain.split('.')) {
    $baseDN += 'dc=' + $piece + ','
}

$baseDN = $baseDN.Substring(0, $baseDN.Length -1)
$gpoLocation = Join-Path -Path $PSScriptRoot -ChildPath 'AwinguGPO'

Expand-Archive AwinguGPO.zip -DestinationPath $PSScriptRoot
import-gpo -BackupGpoName AwinguGPO -TargetName AwinguGPO -path $gpoLocation -CreateIfNeeded -Domain $domain
New-GPLink -Target $baseDN -Domain $domain -Name AwinguGPO -Enforced Yes

gpupdate /force

return $true


