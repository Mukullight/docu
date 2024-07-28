# Loading and Processing
### Loading and processing 
The module contains loader file that reads the file as csv, xml, xls, xlsx, json and the loaded file is saved as a data frame 


load_to_df(file_path):

file_path = "path to the directory of the file"

return --> df (dataframe)


![loader](https://github.com/Mukullight/docu/blob/main/assets/loader.jpg){ align=left }





### nulls and outs
The nulls and the outs function identifies the indexes of the locations of the nulls or out values and effective numerical methods are utilized to identify the most relevant method is utilized.

nulls_and_outs(dataframe, q1, q3):

(dataframe, q1=0.05, q3=0.95): are default values

q1 and q3 can be replaced with different values based on the requirements

![nulls and outs](https://github.com/Mukullight/docu/blob/main/assets/nulls-and-outs.jpg){ align=left }

