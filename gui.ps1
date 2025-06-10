$url = "https://raw.githubusercontent.com/shayelorgelly/school-automation/refs/heads/main/script.py"
$output = "script.py"
Invoke-WebRequest -Uri $url -OutFile $output
python $output
