$densities = @(1.0,1.1)
$radius = 2.0

 foreach ($density in $densities) 
 {
  python main.py "input3.txt" $radius $density f >> test.tsv
 }
