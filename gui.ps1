$url = "https://example.com/script.py"
$output = "script.py"
Invoke-WebRequest -Uri $url -OutFile $output
python $output
