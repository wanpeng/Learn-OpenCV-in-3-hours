opencv_traincascade -data Resources/train/data -vec x2_positive_samples.vec -bg x2_negative_samples.txt  -numStages 2 -w 40 -h 40  -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 5   -numNeg 5  -mode ALL
pause