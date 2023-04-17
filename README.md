# BIL587-FINAL

The repository is currently compatible with `tensorflow-2.0` and makes use of the Keras API using the `tensorflow.keras` library.

* First, clone the repository and enter the folder

```bash
git clone https://github.com/okanexe/BIL587-FINAL.git
cd Emotion-detection
```

* Download the [FER-2013 dataset](https://www.kaggle.com/datasets/deadskull7/fer2013?resource=download) inside the `src` folder.

* If you want to train this model, use:  

```bash
cd src
python detection.py --mode train
```

* Then run the video capture mode: 

```bash
cd src
python detection.py --mode display
```

* The folder structure is of the form:  
  src:
  * data (folder)
  * `emotions.py` (file)
  * `haarcascade_frontalface_default.xml` (file)
  * `model.h5` (file)
