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


* Advanced features:

<details>
  <summary><b>Loading Old Mediasets/Wordcounts</b></summary>

  ### Loading old data  
  1. data is automatically saved in the autosaved_data folder in your installation for later use. 
  2. If you want to create a new wordcount set using new wordlists for the same media set, press the "upload" button above the "retrieve gmail articles" button. Navigate to autosaved_data/*whatever_mediaset*/articleData.json to load the data.
  3. If you want to create another visualization with different using the same wordcounts as in a previous search, press the "upload" button above the "count words" button on the bottom right. Then navigate to autosaved_data/*whatever_mediaset*/*date*_group_n/wordcount.json to load the wordcount.

</details>



<!-- ## Contributing to <project_name>
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
<!-- To contribute to <project_name>, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request). --> -->

<!-- ## Contributors

Thanks to the following people who have contributed to this project:

* [@scottydocs](https://github.com/scottydocs) 📖
* [@cainwatson](https://github.com/cainwatson) 🐛
* [@calchuchesta](https://github.com/calchuchesta) 🐛

You might want to consider using something like the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).

## Contact

If you want to contact me you can reach me at <your_email@address.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

<!-- This project uses the following license: [<license_name>](<link>). --> -->
