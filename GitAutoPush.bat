:loop
	cd C:\Users\정다운\Desktop\Pythonwork\dwj

	git init
	
	git pull
	
	git add --all
	
	git commit -m "auto push"
	
	git push

	echo Complete. Relaunching...
	
	TIMEOUT 3600

goto loop