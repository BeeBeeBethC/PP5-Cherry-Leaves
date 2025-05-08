# Portfolio Project 5 - Mildew Detection in Cherry Leaves

---

# Important Note

Farmy and Foods is a ficticious, hypothetical agricultural company. Created to fulfill the requirements of **Specialisation Project - Portfolio Project 5 - Predictive Analytics** where predictive analytics can be applied in a real project in the workplace for Code Institute.

In the real world, specifically in relation to the Non-Disclosure Agreement. This project would be conducted in a private repository and shared with only the relevant professionals.

However for assessment purposes this portfolio project is in a public repository.

---

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).

- The dataset contains 4208 images taken from the client's crop fields, which have been resized from 256px x 256px to 100px x 100px for efficient hosting.
  
- The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species.

---

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew.

An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew present, the employee applies a specific compound to kill the fungus.

The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an Machine Learning system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew.

A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

---

## Hypothesis

The author's hypothesis for this project is as follows:

I hypothesize that a **Convolutional Neural Network (CNN)** based image classifier can accurately distinguish between **Healthy** and **Powdery Mildew-Infected** cherry leaves by learning and identifying **distinct visual features** (biological markers) associated with the powdery mildew infection.

## How to validate?

To validate this author's hypothesis, a convolutional neural network based image classifier, machine learning model was created and trained as prototype to see if the desired outcome of 97% minimum accuracy was generated.

The objective of this project is to develop a machine learning model that can be deployed live to a user friendly web application whilst adhering to the Non-Disclosure Agreement (NDA) that was written up by Farmy and Foods.

To adhere to the NDA, only a small sample of images are available for use of supporting evidence. The main aim of this project was to aid growers and agricultural specialists for early disease detection of powdery mildews in cherry leaves, with potential to branch out to other diseases in the future.

This outlines the scientific hypothesis and project goal driving the machine learning solution generated within this project.

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

- Model must achieve at least 97% accuracy.
- Additional evaluation includes the confusion matrix, classification report, and ROC-AUC curve to assess balance between precision and recall as well as a sample predictions showing predicted and true values.

### Heuristics

Powdery mildew detection currently relies on subjective visual inspection under field conditions, which can be inconsistent. An image-based ML model could serve as a decision support tool to augment field assessments.

### Dataset

- The dataset contains 4208 images which got split into three subsets of data reduced from 256px x 256px to 100px x 100px to accomodate hosting limitations.
- The training data consists of a curated subset of processed '.PNG' images organized into two classes: “healthy” and “powdery mildew.”
- The dataset has been augmented and split for training, validation, and testing at ratios of 0.7, 0.15, 0.15 summing up to 1.0.
- This equates to 2,946 for training subset, 631 for validation subset and 631 for the testing subset.

---

## Machine Learning Business Case

### What are the business requirements?

- The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Is there any business requirement that can be answered with conventional data analysis?

- Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

### Does the client need a dashboard or an API endpoint?

- The client needs a dashboard.

### What does the client consider as a successful project outcome?

- A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.

### Can you break down the project into Epics and User Stories?

- Information gathering and data collection.
- Data visualization, cleaning, and preparation.
- Model training, optimization and validation.
- Dashboard planning, designing, and development.
- Dashboard deployment and release.

### Ethical or Privacy concerns?

- The client provided the data under an NDA (non-disclosure agreement), therefore the data should only be shared with professionals that are officially involved in the project.

### Does the data suggest a particular model?

- The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.

### What are the model's inputs and intended outputs?

- The input is a cherry leaf image and the output is a prediction of whether the cherry leaf is healthy or contains powdery mildew.

### What are the criteria for the performance goal of the predictions?

- We agreed with the client a degree of 97% accuracy.

### How will the client benefit?

- The client will not supply the market with a product of compromised quality.

---

## Dashboard Design

### Page 1: Project Summary

- General Information
- Introduces Farmy and Foods adds a brief explanation as follows from the [RHS website](https://www.rhs.org.uk/disease/powdery-mildews)
- “Powdery mildews are a group of related fungi which attack a wide range of plants, causing a white, dusty coating on leaves, stems and flowers.”
-	Powdery mildews are typically identified by biological markers that are visible when observing specific leaves.

### Project Dataset

- The available dataset contains 4208 images split into healthy and powdery mildew specimens the dataset can be found at [kaggle.com](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)
- Link to addition information
- Readme Information can be found on [Github](https://github.com/BeeBeeBethC/PP5-Cherry-Leaves)
  
- Business requirements
- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Image Visualizations

- It will answer business requirement 1
- Checkbox 1 - showing a difference between average and variability images for each class present (healthy or powdery mildew)
- Checkbox 2 - showing differences between average 'healthy' and average 'powdery mildew' leaves
- Checkbox 3 - Image Montage for each class with select box to select 'healthy' or 'powdery mildew'

### Page 3: Mildew Detector

- Business requirement 2 information - "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
- User Interface with a multi-file uploader widget
- The user is able to upload multiple cherry leaf images. It will display the image below along with a prediction statement, and probability graph indicating if the leaf is healthy or contains powdery mildew.
- Table with image name and prediction results.
- Button to download table.

### Page 4: Project Hypothesis and Validation

-	I hypothesize that a Convolutional Neural Network (CNN) based image classifier can accurately distinguish between Healthy and Powdery Mildew-Infected cherry leaves by learning and identifying distinct visual features (biological markers) associated with the powdery mildew infection.

### How to validate?

- To validate this author's hypothesis, a convolutional neural network based image classifier, machine learning model was created and trained as prototype to see if the desired outcome of 97% minimum accuracy was generated.
- The objective of this project is to develop a machine learning model that can be deployed live to a user friendly web application whilst adhering to the Non-Disclosure Agreement (NDA) that was written up by Farmy and Foods.
- The main aim of this project was to aid growers and agricultural specialists for early disease detection of powdery mildews in cherry leaves, with potential to branch out to other diseases in the future.
-	This outlines the scientific hypothesis and project goal driving the machine learning solution generated within this project.

### Page 5: ML Performance Metrics

- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result

---

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

---

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

### Acknowledgements

- Thank the people who provided support throughout this project.
