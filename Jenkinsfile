pipeline 
	{ 
	agent any
		triggers
		{
 			pollSCM('* * * * *')
			cron('0 0 * * *')
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