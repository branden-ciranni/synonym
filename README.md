# :ghost: Synonym

## Stop seeing ghosts, start seeing data!

https://synonym.streamlit.app/

![synonym_gif_2](https://github.com/user-attachments/assets/9bfae2a8-3828-42cd-8fa2-489892d64ce5)


This app will be updated in real time as updates are made to this github repository!

Synonym is a tool to help you compare datasets. It can help you identify differences between two datasets, and help you understand why those differences exist.
        
### How to use Synonym

1. **Load Datasets**:
     - Upload two datasets you would like to compare.
     - You can upload datasets in CSV or Excel format.

2. **Supply Read Options**
     - If your dataset requires special pandas read options, you can supply them in JSON format.
     - This is useful if your dataset has a non-standard delimiter, encoding, or other special requirements.

3. **Compare Datasets**
     - Click the "Compare datasets" button to compare the two datasets.
     - Select the **Key** columns to compare the datasets by.
          - This could be a unique identifier, such as a:
               
               - `user_id`
               - `order_id`
               - `transaction_id`
               - `department_id`
          
               or maybe a combination of columns, such as:

               - `first_name` and `last_name`
               - `street_address` and `city`
               - `product_name` and `product_category`
               - `product_id` and `department_id`
          
               anything that uniquely identifies a row in the dataset.
          - Provide those columns, otherwise we'll look in the dataset order, row by row.
          - **It is Highly recommended to provide join columns**.
     - Synonym will compare the datasets column by column and row by row.
     - If there are any differences, Synonym will explain why they exist.

4. **Interpret Results**
     - Synonym will show you the differences between the datasets, in a set of 12 different metrics.
     - If the datasets are identical, Synonym will let you know.
     - If the datasets are not identical, Synonym will explain why.

5. **Export Results**
     - You can export the results of the comparison to a CSV file.
     - Hover over the top right corner of the comparison results and click the download button.
