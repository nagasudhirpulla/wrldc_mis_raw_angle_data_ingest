call nssm.exe install mis_pair_angles_service "%cd%\run_server.bat"
call nssm.exe set mis_pair_angles_service AppStdout "%cd%\logs\mis_pair_angles_service.log"
call nssm.exe set mis_pair_angles_service AppStderr "%cd%\logs\mis_pair_angles_service.log"
call sc start mis_pair_angles_service
rem call nssm.exe edit mis_pair_angles_service