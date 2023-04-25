# 6dposeest
Repository for my thesis, Extracting a texture using 6D Pose Estimation. 6D Pose Estimation by Singleshotpose Buğra Tekin.
Um den Code zum laufen zu kriegen, muss der Singleshotpose Ansatz von Bugra Tekin vorbereitet werden. 
https://github.com/Microsoft/singleshotpose

Sobald das Evironment erfolgreich aufgebaut ist gibt es folgende Dinge zutun:

1.) Generierung der Daten.
	- Mithilfe von Blender können Daten mit ihren Bounding Boxes als Labels gespeichert werden
	- Dafür muss die blender_automate.py Datei im Python Blender Skript ausgeführt werden
		- Wichtig: Den path anpassen, an das 3d Modell, welches genutzt werden soll
		- Ebenfalls den Ausganspfade der Labels und der Bilder spezifizieren
	- Unter LINEMOD/legobrick1_1/ findet man eine prep.py Datei mit welcher die Masken generiert werden, sowie die Labels die richtige Form bekommen
	- So können die Labels dort auf 4 Keypoints angepasst werden
	- LINEMOD/legobrick1_1/labels_test.py ist ein Programm, um die Labels von Blender zu testen
	- Erstelle in cfg/ eine neue .data Datei mit den benötigten Informationen

2.) Training
	- Um das Training Daten zu starten, kann entweder der original Code  genutzt werden (9 Keypoints) oder 
		diese mit den Dateien in diesem Ordner ausgetsaucht werden (4 Keypoints)
	- Die Epochen können in train.py angepasst werden, in der cfg/yolo-pose Datei kann die Batchsize verändert werden
	- beim Training mit 4 Keypoints muss die yolo-pose4K Datei genutzt werden. 
	- Um eine kaum vortrainierte Gewichten zu nutzen, sollte cfg/darknet19_448.conv.23 genutzt werden
	- möglicher Trainingscode:
	
	python train.py --datacfg cfg/legobrick1_1.data --modelcfg cfg/yolo-pose.cfg --initweightfile cfg/darknet19_448.conv.23 --pretrain_num_epochs 15

3.) Validierung
	- Hierfür muss die valid.py Datei genutzt werden. Für die Automatische Texturextraktion muss valid.py vom oringall ausgetasucht werden
	- Beachte hier die Definition ob 9 keypoints oder 4
	- möglicher Validierungscode:
	python valid.py --datacfg cfg/legobrick1_1.data --modelcfg cfg/yolo-pose4K.cfg --weightfile backup/legobrick1_1/model.weights

Special thanks  to Bugra Tekin!
Bei Fragen oder ähnlichem bin ich unter 1415430@uni-wuppertal.de erreichbar.
