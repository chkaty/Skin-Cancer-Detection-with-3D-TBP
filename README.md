# ISIC 2024 - Skin Cancer Detection with 3D-TBP

## Competition Overview
[ISIC 2024 - Skin Cancer Detection with 3D-TBP](https://www.kaggle.com/competitions/isic-2024-challenge/overview) is a Kaggle competition focused on developing image-based algorithms for the accurate binary classification between malignant and benign skin lesions. The competition utilizes histologically confirmed skin cancer cases and single-lesion crops from 3D total body photos (TBP) that resemble close-up smartphone-quality images to train and evaluate models for accurate and reliable skin cancer detection.

The competition addresses the challenge of early skin cancer detection, particularly in underserved populations with limited access to specialized dermatologic care, by improving triage and enabling timely clinical intervention.

Overall, submissions will be assessed using a partial area under the ROC curve (pAUC) above 80% true positive rate (TPR) for binary classification of malignant examples.

## Data Description
The dataset provided consists of supervised training data with two types of labeled images:

1. **Labeled Photos of Skin Lesions**: Zoomed-in and cropped skin lesion images (~401,000 images of 15x15 mm lesions) collected over nine years across nine different institutions on three continents.
2. **Metadata Files**: CSV files containing patient information and characteristics related to the lesion photos.

The target variable is a binary identifier indicating whether a given skin lesion is benign or malignant. Key features for classification will be determined using CNN and XGBoost algorithms.

### Challenges
- **Large Dataset**: 400,000 images totaling 2GB compressed, which increases training time.
- **Severe Class Imbalance**: Less than 0.1% of the training data consists of positive cases, making the task highly imbalanced.
- **Potential Data Artifacts**: All lesions are identified by AI, introducing potential hallucinations in the dataset.

### Techniques for Addressing Challenges
- **Imbalanced Data**: Class weighting, duplicating, and transforming anomaly images.
- **Image Variability**: Resizing and normalization.
- **Large Dataset Handling**: Partial dataset per epoch, reducing image size and resolution.

## Methodology and Evaluation Plan
We will implement a hybrid approach combining CNN and XGBoost:

1. **CNN (Convolutional Neural Network using ResNet)**: Well-suited for anomaly detection in image datasets.
2. **XGBoost**: Incorporates metadata (age, gender, location, etc.) into the final decision-making process for improved accuracy.

These techniques are widely used and well-documented, making them ideal choices for this task.

### Model Evaluation
- **Metric**: Partial Area Under the ROC Curve (pAUC) with a focus on high true positive rates (TPR), prioritizing correct malignant case detection.
- **Cross-Validation**: The dataset will be split into balanced parts, ensuring the same proportion of cancer and non-cancer cases in each fold.
- **Final Validation**: The hidden test set (~500k samples) will be used for final performance confirmation.

## Project Timeline
| Date   | Task |
|--------|------|
| Mar. 1 | Data exploration, create sampling function |
|        | - Split dataset into train (75%) and test (25%) |
|        | - Data augmentation (transform/multiply malignant cases for training) |
|        | - Normalize images |
| Mar. 7 | Model development and evaluation |
| Mar. 14 | Draft report in Jupyter Notebook |
| Mar. 22 | Start preparing presentation |
| Apr. 2 | Finalize presentation |
| Apr. 4 | Presentation day |

---

