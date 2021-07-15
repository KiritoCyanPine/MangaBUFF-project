Set WshShell_a = CreateObject("WScript.Shell")
Set WshShell_b = CreateObject("WScript.Shell")
WshShell_a.Run chr(34) & "D:\programming\Tutorial_Django\MangaBUFF-project\bin\MangaBUFF_server.bat" & Chr(34), 0
WshShell_b.Run chr(34) & "D:\programming\Tutorial_Django\MangaBUFF-project\bin\MangaBUFF_FileServer.bat" & Chr(34), 0
Set WshShell_a = Nothing
Set WshShell_b = Nothing