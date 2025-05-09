# Portfolio Project 5 - Mildew Detection in Cherry Leaves

---

# Contents

* [Contents](#contents)
* [Important note](#important-note)
* [Dataset](#dataset-content)
* [Business Requirements](#business-requirements)
* [Hypothesis](#hypothesis)
  * [how to validate](#how-to-validate)
* [Project Rationale](#project-rationale)
  * [business goals](#business-goal)
  * [problem context](#problem-context)
  * [desired outcome](#desired-outcome)
  * [performance metrics](#performance-metrics)
  * [heuristics](#heuristics)
  * [dataset](#dataset)
* [Machine Learning Business Case](#machine-learning-business-case)
* [Epics and User Stories](#epics-and-user-stories)
* [Dashboard design](#dashboard-design)
* [Project constraints and Bugs](#project-constraints-and-bugs)
* [Deployment](#deployment)
* [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
* [Credits](#credits)
  * [Content](#content)
  * [Author's Note](#authors-note)
  * [Acknowledgements](#acknowledgements)

[Top](#contents)

---

# Important Note

Farmy and Foods is a ficticious, hypothetical agricultural company. Created to fulfill the requirements of **Specialisation Project - Portfolio Project 5 - Predictive Analytics** where predictive analytics can be applied in a real project in the workplace for Code Institute.

In the real world, specifically in relation to the Non-Disclosure Agreement. This project would be conducted in a private repository and shared with only the relevant professionals.

However for assessment purposes this portfolio project is in a public repository.

[Top](#contents)

---

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).

* The dataset contains 4208 images taken from the client's crop fields, which have been resized from 256px x 256px to 100px x 100px for efficient hosting.
  
* The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species.

[Top](#contents)

---

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew.

An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew present, the employee applies a specific compound to kill the fungus.

The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an Machine Learning system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew.

A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

[Top](#contents)

---

## Hypothesis

The author's hypothesis for this project is as follows:

I hypothesize that a **Convolutional Neural Network (CNN)** based image classifier can accurately distinguish between **Healthy** and **Powdery Mildew-Infected** cherry leaves by learning and identifying **distinct visual features** (biological markers) associated with the powdery mildew infection.

## How to validate?

To validate this author's hypothesis, a convolutional neural network based image classifier, machine learning model was created and trained as prototype to see if the desired outcome of 97% minimum accuracy was generated.

The objective of this project is to develop a machine learning model that can be deployed live to a user friendly web application whilst adhering to the Non-Disclosure Agreement (NDA) that was written up by Farmy and Foods.

To adhere to the NDA, only a small sample of images are available for use of supporting evidence. The main aim of this project was to aid growers and agricultural specialists for early disease detection of powdery mildews in cherry leaves, with potential to branch out to other diseases in the future.

This outlines the scientific hypothesis and project goal driving the machine learning solution generated within this project.

[Top](#contents)

---

## Project Rationale

We aim to develop a machine learning model that predicts whether a plant leaf is healthy or infected with powdery mildew, using historical image data. This is a supervised, binary classification task, where each image is labeled as either “healthy” or “powdery mildew.”

### Business Goal

Enable farmers and agricultural technicians to quickly and reliably detect powdery mildew in plants using smartphone images.

### Problem Context

Manual inspection of leaves is labor-intensive and requires expert knowledge. Visual symptoms of powdery mildew can be subtle in early stages, leading to delayed diagnosis and crop loss. Small farms and remote regions often lack access to plant pathology experts.

### Desired Outcome

Deploy a real-time prediction system via a Streamlit-based web application. Users can upload a leaf image and instantly receive a diagnosis flag (“infected” or “healthy”) with the associated confidence score.

### Performance Metrics

* Model must achieve at least 97% accuracy.
* Additional evaluation includes the confusion matrix, classification report, and ROC-AUC curve to assess balance between precision and recall as well as a sample predictions showing predicted and true values.

### Heuristics

* Powdery mildew detection currently relies on subjective visual inspection under field conditions, which can be inconsistent. An image-based ML model could serve as a decision support tool to augment field assessments.

### Dataset

* The dataset contains 4208 images which got split into three subsets of data reduced from 256px x 256px to 100px x 100px to accomodate hosting limitations.
* The training data consists of a curated subset of processed '.PNG' images organized into two classes: “healthy” and “powdery mildew.”
* The dataset was been augmented and split for training, validation, and testing at ratios of 0.7, 0.15, 0.15 summing up to 1.0.

[Top](#contents)

---

## Machine Learning Business Case

### What are the business requirements?

* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Is there any business requirement that can be answered with conventional data analysis?

* Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

### Does the client need a dashboard or an API endpoint?

* The client needs a dashboard.

### What does the client consider as a successful project outcome?

* A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
* Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.

### Can you break down the project into Epics and User Stories?

* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.

### Ethical or Privacy concerns?

* The client provided the data under an NDA (non-disclosure agreement), therefore the data should only be shared with professionals that are officially involved in the project.

### Does the data suggest a particular model?

* The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.

### What are the model's inputs and intended outputs?

* The input is a cherry leaf image and the output is a prediction of whether the cherry leaf is healthy or contains powdery mildew.

### What are the criteria for the performance goal of the predictions?

* We agreed with the client a degree of 97% accuracy.

### How will the client benefit?

* The client will not supply the market with a product of compromised quality.

[Top](#contents)

---

### Epics and User Stories

**Epic 1 - Information Gathering and Data Collection.**

USER STORY

* As a Developer I can gather information so that I can perform a data collection.

Acceptance Criteria:

* Criteria one: Source information from the client to retrieve information.
* Criteria two: Source dataset from online data hosting platform.
* Criteria three: Download the dataset.

Tasks:

* Retrieve and review the business case document.
* Generate hypothesis.
* Locate data source from online hosting platform (Kaggle).
* Download and extract dataset in code space.

**Epic 2 - Data Visualization, Cleaning, and Preparation.**

USER STORY

* As a Developer I can Visualise Data Collection so that I can determine what data I'm working with.

Acceptance Criteria:

* Criteria one: visualise the data
* Criteria two: clean the data
* Criteria three: preparation of the data.
* Criteria four: generate an image montage

Tasks:

* Generate a sample image that shows what the original sized images are.
* Reduce the image size to 100px x 100px for smoother analysis
* Split the datasets into three subsets subsequently named Train, Validation and Test datasets.
* Augment data so that the sample size is large enough.
* Generate an image montage to satisfy business requirement one.

**Epic 3 - Model training, optimization and validation.**

USER STORY:

As a Developer I can Create a Machine Learning Model so that I can transform the analysis process from 30 minutes to merely seconds.

Acceptance Criteria:

* criteria one: generate a model.
* criteria two: train the model.
* criteria three: optimise the model.
* criteria four: validate the model.

Tasks:

* generate a model to aid in the analysis process.
* train the model using the train and validation datasets.
* optimise the model to gain the highest possible accuracy with minimum of 97% accurate.
* validate the model by using the test dataset and testing the model on "unseen" data.

**Epic 4 – Dashboard planning, designing, and development.**

USER STORY:

As a Developer I can Create an interactive dashboard so that the client can review findings.

Acceptance Criteria:

* Criteria one: Plan a multi-page dashboard.
* Criteria two: Design and create a multi-page dashboard
* Criteria three: Develop a multi-page dashboard

Tasks:

* Plan out the multi-page dashboard
* Generate a dashboard design document
* Create a multi-page dashboard using Python and Streamlit
* Develop the multi-page dashboard

**Epic 5 - Dashboard Deployment and Release.**

USER STORY:

As a Developer I can deploy the dashboard so that I can review my findings in a user friendly way.

Acceptance Criteria:

* Criteria one: deploy the dashboard using Streamlit and Heroku
* Criteria two: release the dashboard with only essential sections to comply with the NDA agreement

Tasks:

* Deploy the dashboard to Heroku
* Move files that need to be hidden to   `.gitignore` and `.slugignore`.
* Release only essential items on the dashboard that relate directly from findings ensuring that data protection is followed as stated in the Non-Disclosure Agreement was written up from the very start of the project.

[Top](#contents)

---

## Dashboard Design

### Page 1: Project Summary

* General Information
* Introduces Farmy and Foods adds a brief explanation as follows from the [RHS website](https://www.rhs.org.uk/disease/powdery-mildews)
* “Powdery mildews are a group of related fungi which attack a wide range of plants, causing a white, dusty coating on leaves, stems and flowers.”
* Powdery mildews are typically identified by biological markers that are visible when observing specific leaves.

### Project Dataset

* The available dataset contains 4208 images split into healthy and powdery mildew specimens the dataset can be found at [kaggle.com](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)
* Link to addition information
* Readme Information can be found on [Github](https://github.com/BeeBeeBethC/PP5-Cherry-Leaves)
  
* Business requirements
* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Image Visualizations

* It will answer business requirement 1
* Checkbox 1 - showing a difference between average and variability images for each class present (healthy or powdery mildew)
* Checkbox 2 - showing differences between average 'healthy' and average 'powdery mildew' leaves
* Checkbox 3 - Image Montage for each class with select box to select 'healthy' or 'powdery mildew'

### Page 3: Mildew Detector

* Business requirement 2 information - "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
* User Interface with a multi-file uploader widget
* The user is able to upload multiple cherry leaf images. It will display the image below along with a prediction statement, and probability graph indicating if the leaf is healthy or contains powdery mildew.
* Table with image name and prediction results.
* Button to download table.

### Page 4: Project Hypothesis and Validation

*	I hypothesize that a Convolutional Neural Network (CNN) based image classifier can accurately distinguish between Healthy and Powdery Mildew-Infected cherry leaves by learning and identifying distinct visual features (biological markers) associated with the powdery mildew infection.

### How to validate?

* To validate this author's hypothesis, a convolutional neural network based image classifier, machine learning model was created and trained as prototype to see if the desired outcome of 97% minimum accuracy was generated.
* The objective of this project is to develop a machine learning model that can be deployed live to a user friendly web application whilst adhering to the Non-Disclosure Agreement (NDA) that was written up by Farmy and Foods.
* The main aim of this project was to aid growers and agricultural specialists for early disease detection of powdery mildews in cherry leaves, with potential to branch out to other diseases in the future.
* This outlines the scientific hypothesis and project goal driving the machine learning solution generated within this project.

### Page 5: ML Performance Metrics

* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result

[Top](#contents)

---

## Project Constraints and Bugs

* Within this project, there is a significant constraint to this project and that is the ever evolving Machine Learning language libraries. These libraries frequently introduce new changes and at the same time deprecate older features.

* As a result of this, The project was developed and tested with the package versions listed in requirements.txt and as such using different versions may lead to compatibility issues in the future.

* whilst no known bugs are present. This author thought they would discuss a few reoccurring issues over the course of the project.

* From the start of the project, this author noticed that on re-running notebooks due to changes occurring within them, duplicate files and images where being produced.

* To combat this and prevent further confusion down the line when delving into the depths of model creation, this author ensured that all notebooks, files and directories were not duplicated or being overwritten. thus keeping the project directory cleaner and easier to navigate through to specific files.

* As a result of the above, by maintaining a clean workspace without overwritten and duplicated files, it ensured that the model was only using clean data and datasets.

* One of these such folders is the versioning file which shows 'v13' in outputs. This author's reasoning for this was to ensure that nothing was being overwritten and kept 'up to date' with the code used throughout the notebooks by creating an automatic version control which essentially retrieves files from all previous version folders and automatically moving them to the current versioning folder.

* Another example is cleaning up the outputs at the end of Jupyter Notebook 5, this is to ensure a clean and neat workspace labelled correctly whilst maintaining a non-duplicated file system.

* During the final notebook, issue after issue came up with the confusion metrics section. Specifically providing this author with the wrong and incorrect metrics.

* After lots of reviewing it turns out that this author had caused the metrics to use 'batch_size' instead of 'prediction_class' on clear up of this and refining code the confusion metrics worked as expected instead of throwing odd stats such as 47% when other tests stating a ~99% accuracy this author recognised something was a miss and on further test running and model tuning (as some library commands had depreciated during this model build) the overall accuracy settled at 98%.

[Top](#contents)

---

## Deployment

### Heroku

* The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

[Top](#contents)

---

## Main Data Analysis and Machine Learning Libraries

* Python - general purpose programming language, used in Data science and Machine Learning.
* Jupyter Notebooks - Allows users to combine code, output, visualizations, and narrative text in a single document.
* Git - version control.
* Github Codespaces - cloud-based development environment.
* Github - Stores the project repository.
* NumPy - For numerical computations and array operations.
* Pandas - For data manipulation and analysis, handling CSV files.
* Scikit-learn - For machine learning utilities and metrics.
* Matplotlib - Basic plotting library to create static
visualizations.
* Seaborn - Statistical data visualization built on matplotlib.
* Plotly - For interactive visualizations.
* Pillow - For image processing and manipulation.
* Tensorflow - Deep learning framework.
* Keras - High-level neural network API.
* Streamlit - For creating the web interface/dashboard.
* Joblib - For saving/loading machine learning models.

[Top](#contents)

---

## Credits

### Content

* [RHS Website](https://www.rhs.org.uk/disease/powdery-mildews) - providing the text for the project summary page.
* [Streamlit's Official Youtube Channel](https://www.youtube.com/@streamlitofficial)  - used for better clarity and understanding
* [Streamlit Official Docs](https://docs.streamlit.io/) - used for information on streamlit web app build.
* [Streamlit Emoji Shortcodes](https://share.streamlit.io/streamlit/emoji-shortcodes) - provided the shortcode for the icon in the tabs bar.
* [Tech with Tim](https://www.youtube.com/watch?v=o8p7uQCGD0U&t=755s) was really helpful in understanding the principles and concepts of creating a streamlit app.
* [IBM's Nicholas Renotte](https://www.youtube.com/watch?v=jztwpsIzEGc&t=36s) gave this author a better perspective on how to create an image classifier using Convolutional Neural Network application, source code for this project included in the video can be found [here](https://github.com/nicknochnack/ImageClassification)
* [Chanin Nantasenamat aka DataProfessor](https://www.youtube.com/@DataProfessor) youtube channel helped this author clarify and understand streamlit. link to DataProfessor's [Github](https://github.com/dataprofessor/) can be found for various projects.
* [Walkthrough Project - 1](https://github.com/Code-Institute-Solutions/WalkthroughProject01) - used for some sections of code throughout the Mildew Detection notebooks
* [Walkthrough Project - 2](https://github.com/Code-Institute-Solutions/churnometer#readme) - used as guidance initially to get a blank multipage app placeholder online and hosted in heroku. also used for readme layout.
* [Idamariesofie - PP5 Project](https://github.com/idamariasofie/mildew-detection) for guidance on app_pages layout, some code used and adapted and to gain a better initial understanding of what Portfolio Project 5 entails.
* [linx02 - Gender Prediction Project](https://github.com/linx02/image-classifier-cnn/tree/main) Code used to generate `.CSV` files.
* [Stack Overflow](https://stackoverflow.com/questions/78996520/import-tensorflow-keras-preprocessing-image-could-not-be-resolvedpylancereport) - used for reworking Pylance error.
* Code Institute's Slack Hub - Used for moral support and to be able to work through known bugs such as those on deployment to heroku and image sizing, also src folders and defining issues.
* Code from above sources was reviewed and adapted to suit the requirements of this author's project.

[Top](#contents)

---

### Author's Note

This author has been through an incredible learning journey which I am extremely grateful to have had the privilage to complete.

Portfolio Project 5 has been challenging yet so rewarding. Overall, this author has thoroughly enjoyed every aspect of building a machine learning model from conception to completion.

### Acknowledgements

First and foremost a huge Thank You to Luke Buchanan, my mentor, who has been exceptional not only throughout this project but throughout all my past projects.

To all the Staff and Assessors at Code Institute and Awarding Bodies.

To all my fellow peers particularly George Small who has continued to support throughout the course.

To my family and my wonderful partner who have been an invaluable support network throughout this past year of learning.

Thank You all for your support.

[Top](#contents)

---
