pipeline 
	{ 
	agent any
		triggers
		{
 			pollSCM('* * * * *')
			cron('20 17 * * *')
		}
		stages 
		{ 
			stage("Compile") 
			{ 
				steps 
				{
				//pip install requirements.txt 
				echo "Python compile done" 
				} 
			} 
			stage("Unit test") 
			{ 
				steps 
				{ 
				sh "python sample.py" 
				} 
			} 
		}	 	
	} 