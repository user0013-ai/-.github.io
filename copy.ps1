$files = Get-ChildItem 'C:\Users\ASUS\Downloads' -Filter '*.jpg' | Where-Object { $_.Name -like '*webwx*' }
if ($files) {
    $files[0] | Copy-Item -Destination 'C:\Users\ASUS\Desktop\test\avatar.jpg' -Force
    Write-Host "OK: $($files[0].Name) -> avatar.jpg"
} else {
    Write-Host 'No matching file found in Downloads'
    Get-ChildItem 'C:\Users\ASUS\Downloads' -Filter '*.jpg' | Select-Object -First 5 Name | Format-Table -AutoSize
}