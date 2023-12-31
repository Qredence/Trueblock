
![visualblock](https://github.com/Qredence/Trueblock/assets/60674042/5a114a47-3244-4dd4-aacf-585006c0af09)
# TrueBlock
# Part 1: Visual Node for Trulens in a Notebook
##  Objective
To develop a custom visual node that can be seamlessly integrated into Jupyter notebooks or similar environments.
To provide users with an intuitive, drag-and-drop interface for incorporating Trulens analytics into their data pipelines.

## Features
### Interactive UI: A user-friendly interface allowing for easy manipulation and configuration of data analysis parameters.
Real-Time Data Visualization: Instant visual feedback on data processing and analysis, aiding in quicker insights.
Seamless Integration: Effortlessly embeddable in popular data science notebooks.


### Customization: Users can tailor the node to suit specific project needs.
##Impact
###Enhanced Accessibility: Makes advanced data analytics more accessible to a broader range of users, including those with limited coding skills.
Increased Productivity: Streamlines the process of data analysis, allowing for more efficient exploration and interpretation of data.
Educational Value: Offers a valuable tool for educational purposes, helping students and newcomers understand complex data analysis concepts visually.


```bash
const NODE_SPEC = {
  "id": "trulens-node",
  "name": "Trulens Node",
  "category": "processor",
  "outputSpecs": [
    {
      "name": "detections",
      "type": "object"
    }
  ],
  "inputSpecs": [
    {
      "name": "image",
      "type": "object",
      "editorSpec": {
        "type": "image_input"
      }
    }
  ],
  "propertySpecs": [
    {
      "name": "model_path",
      "type": "string",
      "editorSpec": {
        "type": "text_input"
      }
    },
    {
      "name": "score_threshold",
      "type": "number",
      "editorSpec": {
        "type": "number_input"
      }
    },
    {
      "name": "max_boxes",
      "type": "number",
      "editorSpec": {
        "type": "number_input"
      }
    }
  ]
};
```

###[WORK IN PROGRESS ] 
```bash
https://visualblocks.withgoogle.com/#/demo?project_json=https://lqffwmrfmlarkbjzejia.supabase.co/storage/v1/object/sign/avatars/Trul.json?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJhdmF0YXJzL1RydWwuanNvbiIsImlhdCI6MTcwMzU2ODA1MywiZXhwIjoxNzM1MTA0MDUzfQ.Y6sBjhsmZMT5xbTINlTzUhBL696E7NxbIjhODqxm1i8&t=2023-12-26T05%3A20%3A54.048Z
```


# Part 2: RAG on Trulens Documentation
![Illustration](https://github.com/Qredence/Trueblock/assets/60674042/0db405c2-79ee-434a-a4ee-ea8529647a00)

# Ask Trueblock for guidance to add Trulens into your project now : https://chat.qlaus.app/embedded/public/87c92de2-cc30-4702-801f-07a8b4b3d97e

## Objective
To develop a comprehensive Robustness, Assurance, and Guidance (RAG) system for Trulens documentation.
To provide users with a clear, structured, and detailed understanding of Trulens’ functionalities and best practices.

## Features
### Robustness Check:
Ensuring that the documentation covers all features and use cases of Trulens comprehensively.

### Assurance Guidelines:
Providing users with confidence in applying Trulens to their data, including troubleshooting and problem-solving guides.

### Guidance System: 
Step-by-step tutorials, examples, and best practices to optimize the use of Trulens in various scenarios.

## Impact
### Improved User Experience: 
Makes it easier for users to navigate and utilize Trulens documentation.

### Enhanced Learning Curve: 
Helps new users to quickly get up to speed with the platform’s capabilities.
Quality Assurance: Ensures that the documentation remains current, accurate, and user-friendly.


# Ask Trueblock for guidance to add Trulens into your project now : https://chat.qlaus.app/embedded/public/87c92de2-cc30-4702-801f-07a8b4b3d97e
