#Gathering installed software
Get-ChildItem HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall
Get-ChildItem HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

New-PSDrive -PSProvider Registry -Name HKU -Root HKEY_USERS
$tempRawData = Get-ChildItem HKU:\*\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
ForEach($entry in $tempRawData)
{
    $tempName = $entry.Name -replace "HKEY_USERS","HKU:"
    Get-ChildItem $tempName
}

#SDDL
Get-Acl .\example.txt | Format-List
ConvertFrom-SddlString -Sddl

#Systeminfo
Systeminfo
Get-ComputerInfo

#Net name cache
Nbtstat -c

#Network statistics
Netstat
Get-NetTCPConnection

#Configuration of network devices
Ipconfig -all

#Running processes
Tasklist /svc
Get-Process

#Running services
sc.exe query
Get-Service

#Scheduled tasks
Schtasks /query
Get-ScheduledTask
Get-ScheduledTask -TaskName TaskName | Get-ScheduledTaskInfo

#Shared resources
Net Share
Get-SmbShare

#Prefetch files
Get-ChildItem C:\Windows\Prefetch

#Event log
Get-EventLog

#Windows events
Get-WinEvent

#Get active sessions
Get-CimInstance Win32_LoggedOnUser
Get-Process -IncludeUserName | Select-Object UserName,SessionId | Sort-Object SessionId -Unique

#Last ran apps in Win+R
Get-ItemProperty -path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU"

#Recent files in MMC
Get-ItemProperty -path "HKCU:\SOFTWARE\Microsoft\Microsoft Management Console\Recent File List"

#Recent files opened in paint
Get-ItemProperty -path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Applets\Paint\Recent File List"

#Recent modified files
$data = (Get-ItemProperty -path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" -name recent | select recent).recent
Get-ChildItem $data | Sort-Object lastwritetime

#Last connected USB devices
$usbDevices = Get-ChildItem -path "HKLM:\SYSTEM\CurrentControlSet\Enum\USB"
ForEach($entry in $usbDevices)
{
    $temp = $entry.Name -replace "HKEY_LOCAL_MACHINE","HKLM:"
    Get-ChildItem $temp
}

#Last connected USB storage devices
$usbDevices = Get-ChildItem -path "HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR"
ForEach($entry in $usbDevices)
{
    $temp = $entry.Name -replace "HKEY_LOCAL_MACHINE","HKLM:"
    Get-ChildItem $temp
}

#Last connected Bluetooth devices
$bluetoothDevices = Get-ChildItem -path "HKLM:\SYSTEM\CurrentControlSet\Enum\BTHLE"
ForEach($entry in $bluetoothDevices)
{
    $temp = $entry.Name -replace "HKEY_LOCAL_MACHINE","HKLM:"
    Get-ChildItem $temp
}
