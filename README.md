# Glyphilator

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
<!-- ![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/scottydocs/README-template.md?style=social)
![GitHub forks](https://img.shields.io/github/forks/scottydocs/README-template.md?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/scottydocs?style=social) -->

The Glyphilator is a tool that allows researchers to do visualize massive amounts of data.

Automatically creates visualizations for the open-source software GaiaViz[https://gaiaviz.com/] (Formerly A.N.T.Z). Features include:
* Upload your own text data
* Curate a list of URLs to scrape text data
* Search Pubmed[https://pubmed.ncbi.nlm.nih.gov/], and visualize the results
* Connect Gmail account, and visualize Google News Alerts

<!-- ## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
<!-- * You have installed the latest version of `<coding_language/dependency/requirement_1>`
* You have a `<Windows/Linux/Mac>` machine. State which OS is supported/which is not.
* You have read `<guide/link/documentation_related_to_project>`. --> -->
![Visualization Example](/readme_images/antzScreenshot.png)
## Installing <Glyphilator>

To install <Glyphilator>, 

download and unzip the latest version in the [google drive](https://drive.google.com/drive/folders/1oKKRnuR-Q5Yn3ie5e7jKuaxTFoybBXaM?usp=sharing)

Add run commands and examples you think users will find useful. Provide an options reference for bonus points!

## Using <Glyphilator> ##
1. launch with gui.exe

   read on based on the source of your data you want visualized


<details>
  <summary><b>Data From Gmail</b></summary>

  ### Data From Gmail  
  1. Press "sign in" button  
  2. Select what Google Alert you want glyphilated  
  3. Select the time range of articles to be glyphilated, using either the dropdown for quick access or selecting a beginning and end date to glyph the text from every link in the Google Alerts between two dates.  
  4. Press "Retrieve Gmail Articles" button at the bottom right of the window.  

  ![Visualization Example](/readme_images/gmail_step123.png)
</details>



<!-- ### Data from Custom URL List, or Local Files ###
1. create an empty text (.txt) file in your working directory. This will be our searchlist file.
 For any URLs you want glyphed, copy and paste the URL into the searchlist file, separated by a new line. If you know any absolute filepaths for .txt files you want glyphed, add them separated by a new line as well.
2. Click "other text options", then click the "upload searchlist" button, and select the searchlist you just created.
3. if there are any .txt files you want to append to the searchlist file, you can also add them by browsing your filesystem. Press "Browse Files" button, and select however many text files you want to add, using shift or ctrl. 
4. collect the data in the searchlist file by pressing "Collect Searchlist Data" -->
<details>
  <summary><b>Data from Custom URL List, or Local Files</b></summary>

  ### Data from Custom URL List, or Local Files  
  1. create an empty text (.txt) file in your working directory. This will be our searchlist file.
  For any URLs you want glyphed, copy and paste the URL into the searchlist file, separated by a new line. If you know any absolute filepaths for .txt files you want glyphed, add them separated by a new line as well.
  2. Click "other text options", then click the "upload searchlist" button, and select the searchlist you just created.
  3. if there are any .txt files you want to append to the searchlist file, you can also add them by browsing your filesystem. Press "Browse Files" button, and select however many text files you want to add, using shift or ctrl. 
  4. collect the data in the searchlist file by pressing "Collect Searchlist Data"
  ![Visualization Example](/readme_images/customList_1234.png)
</details>


<details>
  <summary><b>Data from Pubmed</b></summary>

  ### Data from Pubmed  
  1. click "other text options" button.
  2. enter your Pubmed search query into the entry bar, just like you would on the website.
  3. enter how many results you want glyphed in your visualization, up to 200.
  4. press "confirm search" to lock in search parameters.
  5. press "execute search" to scrape pubmed and pull the data down
  ![Visualization Example](/readme_images/pubmed12345.png)

</details>

2. Select a wordlist group by clicking on it. You may use a premade wordlist group in groups 1,2,3 or 4. You can find the wordlist .txt files in your installation in GmailGlyphilatorV_n/wordlists/group_n. They can be edited directly there, or you may use the "delete" or "browse" buttons on the bottom right of the wordlist panel to browse to your own wordlist.txt file and add it to the group you have currently selected. You may also delete a wordlist.txt file from a group you have currently selected. 

3. press "count words" button on the bottom right of the window. That will count up every time every word from a wordlist was used in your collected text media. To increase or decrease the strictness of  how close a word has to be for it to be "counted" can be modulated by the "search fuzziness" slide bar.

4. press "create viz" button on the bottom right of the window. You may change viz parameters, like how words are counted or scaled, or what shape to use by changing the settings on the bottom left of the window.

5. Finally press "view in A.N.T.Z." button to open a visualization of your data.
![Visualization Example](/readme_images/general2345.png)


### Advanced features:

<details>
  <summary><b>Loading Old Mediasets/Wordcounts</b></summary>

  ### Loading old data  
  1. data is automatically saved in the autosaved_data folder in your installation for later use. 
  2. If you want to create a new wordcount set using new wordlists for the same media set, press the "upload" button above the "retrieve gmail articles" button. Navigate to autosaved_data/*whatever_mediaset*/articleData.json to load the data.
  3. If you want to create another visualization with different using the same wordcounts as in a previous search, press the "upload" button above the "count words" button on the bottom right. Then navigate to autosaved_data/*whatever_mediaset*/*date*_group_n/wordcount.json to load the wordcount.

</details>

<details>
  <summary><b>CSV Data Glyphing</b></summary>

  ### Loading CSV data  
  1. Make sure that the data you're trying to glyph is exclusively numerical. Other than the first row and first column (if you want pre-made tags) the data should be either floats or integers. Each row in the dataset will be a glyph, with each column being a branch node. The ideal dataset structure is illustrated in the image below:
  ![Visualization Example](/readme_images/CSV_data_structure.png)

  2. CSV options can be found by pressing "Other Text Options" button on the main screen. Start by pressing "Upload CSV" and navigate to your CSV of interest. The program assumes that the first row and column are headers, and don't have data in them. If your first row or column has data, uncheck the box "first row header" or "first column header" depending on your use case.
  
  3. The rest of the interface has dropdowns that allow users to change how glyphs are arranged. By default, they will be arranged in a grid, and they can be changed by using the "Glyph Pattern" dropdown in the main page. Of course, there are no wordlists in a CSV, so wordlist_axes is not a valid choice. <br /><br /> Otherwise, the X,Y,Z displacement column dropdowns can choose a column, and the glyph will move based upon that row's value compared to the rest of the dataset. Based on the example data above, say I want to order my cities in X based upon average temperature, and in Y by average rainfall (mm), and no Z displacement.<br /><br /> The root color can be changed based on the value of data. For example, If I want the color to change from red to blue in cities with high population, getting more blue with cities of lower population, I can make selections as shown in the images below:
  ![Visualization Example](/readme_images/CSV_selection_columns.png)
  

  4. Press the "Collect CSV Data" button to finalize selections made above. Then Press the "create Viz" button on the main window to construct the visualization. Preview below.

  ![Visualization Example](/readme_images/CSV_example_viz_notags.png)
  ![Visualization Example](/readme_images/CSV_example_viz_tags.png)

  
    

  ### Geospatial CSV Glyphing
  1.  As with standard CSV Glyphing, the data needs to be all integers and floats, with the exception of the header row and column, if any.<br /> 

  Note that The **latitude and longitude must be in their own columns,** as in the sample data below.
  ![Visualization Example](/readme_images/CSV_data_structure.png)

  2. If you plan on using Geospatial Glyph placement, all column dropdowns are available to you as with regular CSV glyphing, with the exception of X and Y Displacement. 

  3. Next you need an API key from Mapbox. They need a credit card, but the free limit is 50,000 maps, so there is really no risk running out of free use. Once you have an API key, you may copy/paste it into the "Mapbox API Key" field. <br /><br /> If you want your API key to autofill into the field on startup, place a file named "mapbox.txt" containing nothing but the api key in the "api_keys" folder in your Glyphilator installation.
  ![Visualization Example](/readme_images/mapbox_api_install.png)

  4. Select your column containing latitude/longitude in the CSV in the "latitude column" and "longitude column" dropdowns respectively. Make sure that X and Y displacement columns have "None" selected.

  5. Press "Collect CSV Data" button, followed by "create Viz" button in main window.
  ![Visualization Example](/readme_images/geo_example_notags.png)
  ![Visualization Example](/readme_images/geo_example_tags.png)

  
</details>


<details>
  <summary><b>Hyper-Histoglyphilation</b></summary>

  ### Hyper-Histoglyphilator  
  ![Visualization Example](/readme_images/Histoglyphilator_steps.png)
  1. Upload CSVs to a wordlist group on the main glyphilator.exe window. It is assumed there is a header row that contains all the column names. It is assumed that there is no row identifiers. In other words, the first column is assumed to be data.
  2. Set the scaling of each bar on the histoglyphs. By default, the minimum is less than the maximum, so that small data corresponds to a small bar. The minimum can be a larger float than the maximum, which would result in large numbers in data being represented as small bars on the histogram.
  3. Press the "Open Colors" button to open the colors window. Every bar of every histoglyph can be configured to have its own color gradient. First select the csv you want to apply colors to in the top dropdown (step 3.1). Next Select using shift + ctrl which columns of the csv should have a color applied to them (step 3.2). Select which color gradient to apply, chosen from the default [list of gradient options](https://matplotlib.org/stable/gallery/color/colormap_reference.html) from the Python Matplotlib library (step 3.3). Finally apply the color gradient to either the columns selected in step 3.2, or every column of every csv in the visualization, using the buttons at the bottom of the colors window (step 3.4)
  4. Press the "Create Viz" button to generate the GaiaViz visualization. It may take a few seconds to a minute or two to complete based on the size of the dataset.
  5. Press the "View in ANTZ" Button on the main GlyphSearch window to open your new vizualization.
  ![Visualization Example](readme_images\hyper-histoglyphilator_screenshot.png)
  
</details>
