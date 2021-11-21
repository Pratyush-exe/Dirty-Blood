# Dirty-Blood

[Click here for Demo](https://dirty-blood.herokuapp.com/)

## Inspiration
Classification of cells has always been a human oriented task. This is time taking process that requires labour. So I thought I can combine my knowledge of Computer Vision and little bit of biology to overcome this problem. The web App created automates this stuff by predicting between any of the four Blood Cell types by just looking at the images i.e. Eosinophil, Lymphocyte, Monocyte, or Neutrophil.
## What it does
The web app takes the image from the user from local storage or can be clicked using mobile phone. Then it predicts weather the blood contains any of the four type of cells Eosinophil, Lymphocyte, Monocyte, or Neutrophil.
## How we built it
Image Data was collected from kaggle: [Kaggle Dataset](https://www.kaggle.com/paultimothymooney/blood-cells). Then a simple CNN based model was created and was trained to predict and classify the type of cell.
## Challenges we ran into
Biggest challenge I faced while creating this project was to gain accuracy, ultimately I achieved a Training Accuracy of 90% and Validation accuracy of 84% whereas earlier I was getting lesser. I wish to increase the accuracy more by complicating the CNN model for better predictions.
## Accomplishments that we're proud of
It's obviously the accuracy and the web app, it was difficult to pull this off in such short amount of time.
## What we learned
I learnt some new techniques of Computer Vision and a little bit about types of blood cells while I was googling about them.
## What's next for Dirty Blood : a blood cell classifier app
I wish to increase the accuracy and create a mobile app for better use. I also wish to use YOLO algorithm for counting the number of cells and predicting and classifying wider range of blood cell types. And ultimately reach out to people and aware them about my app

